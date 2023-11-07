from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # main point of reference for application. Flask app initialization
CORS(app) # CORS middleware
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mctbnnrv:VN6WTy7mEtsCkM31stIbfMFwVXDmoYh7@trumpet.db.elephantsql.com/mctbnnrv'
db = SQLAlchemy(app)

from application import routes # route works using app variable so can't import it above flask app

