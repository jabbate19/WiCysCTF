from os import environ as env, urandom

# Flask config
IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', '127.0.0.1:8080')
PREFERRED_URL_SCHEME = env.get('PREFERRED_URL_SCHEME', 'https')

# DB Info
SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///webstorage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

JWT_SECRET = 'starwars'

SECRET_KEY = urandom(32)

