from bs4 import BeautifulSoup as bs4
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from googleAPI import sheetsUpd
import gspread
import requests
import os

app = Flask(__name__)
Bootstrap(app)

#FIRST PAGE
@app.route('/')
def index():
    return render_template("index.html")

#ANALYSIS PAGE
@app.route("/analyse", methods=['POST'])
def analyse():
    if request.method == 'POST':
        price = request.form["prop_price"]
        down = request.form["prop_down"]
        rent = request.form["prop_rent"]
        expense = request.form["prop_expense"]
        tax = request.form["prop_tax"]
        interest = request.form["prop_interest"]

        sheetsUpd(price, down, rent, expense, tax, interest)

        return render_template("analyse.html")

#THIS IS THE MAIN, FIRST THING THAT RUNS IN THE CODE
if __name__ == '__main__':
    app.debug = True
    app.run()
