from flask import Flask
import requests
from firebase import firebase
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
firebase = firebase.FirebaseApplication("https://postman-api-4245b-default-rtdb.firebaseio.com/",None)

from app import routes
