#import flask
from flask import render_template, request, Flask, session, redirect, send_from_directory, jsonify, url_for
from bd import DBConsults
import time
import hashlib

app = Flask(__name__)
app.secret_key = "123456"
"""
ROUTING
"""
#request.form[atributo]
#request.method = metodo (GET, POST etc)

#### Home ####
@app.route("/", methods = ["GET", "POST"])
def homepage():
	return "hola"
    #return render_template("index.html")

@app.route("/get_parking_number")
def get_parking_number():
	return 0