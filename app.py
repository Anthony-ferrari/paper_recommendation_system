from flask import Flask, redirect, url_for, render_template, request
# from db_connector.db_connector import connect_to_database, execute_query
# from datetime import datetime 
app = Flask(__name__)
# index
@app.route("/")
def index():
    return render_template("index.html")
# home
@app.route("/home")
def home():
    return render_template("home.html")