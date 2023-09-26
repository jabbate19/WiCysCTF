from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, Form, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(('Username'), validators=[DataRequired()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

    def validate(self, extra_validators=None):
        if not Form.validate(self):
            return False
        return True

class NoteForm(FlaskForm):
    key = StringField(('Key'), validators=[DataRequired()])
    content = StringField(('Content'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

    def validate(self, extra_validators=None):
        if not Form.validate(self):
            return False
        return True