from flask import Flask
import os,socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! How are you'
