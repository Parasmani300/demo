
from flask import Flask
from config import Config
from pyrebase import pyrebase
app = Flask(__name__)

app.config.from_object(Config)

firebaseConfig = {
    'apiKey': "AIzaSyDf0dXPrdtkUNm21XaseVVBPEA_DXeGSUQ",
    'authDomain': "demoapp-8bd99.firebaseapp.com",
    'databaseURL': "https://demoapp-8bd99.firebaseio.com",
    'projectId': "demoapp-8bd99",
    'storageBucket': "demoapp-8bd99.appspot.com",
    'messagingSenderId': "359623902890",
    'appId': "1:359623902890:web:7b049e2908ccda97b6b2d3",
    'measurementId': "G-ZJR8E2L75K"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()

from application import routes


if __name__ == "__main__":
    app.run()
