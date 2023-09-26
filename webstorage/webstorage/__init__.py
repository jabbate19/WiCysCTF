import os
from flask import Flask, request, make_response, render_template, send_from_directory, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import jwt

# Setting up Flask and csrf token for forms.
app = Flask(__name__, static_url_path='/static', static_folder='static')
csrf = CSRFProtect(app)
csrf.init_app(app)
# Get app config from absolute file path
if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

db = SQLAlchemy(app)

from webstorage.models import User, Note
from webstorage.forms import LoginForm, NoteForm

@app.route('/', methods=['GET'])
def index():
    auth = request.cookies.get('auth')
    if auth is None:
        print("No auth")
        return redirect(url_for('login'))
    try:
        auth_data = jwt.decode(auth, app.config['JWT_SECRET'], algorithms=['HS256'])
        user = User.query.get(auth_data['username'])
        if not user:
            return redirect(url_for('login'))
        notes = Note.query.filter_by(owner=auth_data['username']).all()
        return render_template('index.html', notes=notes, username=auth_data['username'])
    except Exception as e:
        print(e)
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user and user.is_valid(form.password.data):
            resp = make_response(redirect(url_for('index'))) 
            resp.set_cookie('auth', jwt.encode({'username': user.username}, app.config['JWT_SECRET'], algorithm='HS256'))
            return resp
        form.password.errors.append('Invalid username or password')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user:
            form.password.errors.append('User already exists')
            return render_template('register.html', form=form)
        new_user = User(form.username.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
        resp = make_response(redirect(url_for('index'))) 
        resp.set_cookie('auth', jwt.encode({'username': new_user.username}, app.config['JWT_SECRET'], algorithm='HS256'))
        return resp
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    resp = make_response(redirect("/", 302))
    resp.delete_cookie('auth')
    return resp

@app.route('/newnote', methods=['GET', 'POST'])
def newnote():
    auth = request.cookies.get('auth')
    if auth is None:
        print("No auth")
        return redirect(url_for('login'))
    try:
        auth_data = jwt.decode(auth, app.config['JWT_SECRET'], algorithms=['HS256'])
        user = User.query.get(auth_data['username'])
        if not user:
            return redirect(url_for('login'))
        form = NoteForm()
        if form.validate_on_submit():
            new_note = Note(auth_data['username'], form.key.data, form.content.data)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('newnote.html', form=form, username=auth_data['username'])
    except Exception as e:
        print(e)
        return redirect(url_for('login'))
