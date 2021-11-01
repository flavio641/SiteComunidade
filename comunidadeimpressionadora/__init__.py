from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')


app.config['SECRET_KEY'] = '11f3ebe859a026ed558e54cb1a3cf33f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)


from comunidadeimpressionadora import routs


