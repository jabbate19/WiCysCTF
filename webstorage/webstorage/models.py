from webstorage import db
from bcrypt import hashpw, gensalt, checkpw


class User(db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String, primary_key=True)
    pass_hash = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.pass_hash = hashpw(password.encode('utf-8'), gensalt(12))

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def is_valid(self, password):
        return checkpw(password.encode('utf-8'), self.pass_hash)

    def get_id(self):
        return self.id

class Note(db.Model):
    __tablename__ = 'note'

    note_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    owner = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def __init__(self, owner, key, content):
        self.owner = owner
        self.key = key
        self.content = content

    def __repr__(self):
        return '<id {}>'.format(self.note_id)

    def get_id(self):
        return self.note_id