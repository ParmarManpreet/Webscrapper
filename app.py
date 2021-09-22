from bs4 import BeautifulSoup as bs4
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from Webscrapper.Calculator import  Calculations
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
        #variables taken as strings
        price = int(request.form["prop_price"])
        down = int(request.form["prop_down"])
        rent = int(request.form["prop_rent"])
        expense = int(request.form["prop_expense"])
        tax = int(request.form["prop_tax"])
        interest = int(request.form["prop_interest"])

        calculationResults = Calculations(price, down, rent, expense, tax, interest)

        calculationResults.downPayment()
        ##sheetsUpd(price, down, rent, expense, tax, interest)

        #array of size 2, [0] = worst case, [1] = best case
        print(calculationResults.downPayment())
        print(calculationResults.totalCost())
        print(calculationResults.mortgageCost())
        print(calculationResults.monthlyExpense()[0])
        print(calculationResults.profit()[0])
        print(calculationResults.roiPercent()[0])
        print(calculationResults.monthlyExpense()[1])
        print(calculationResults.profit()[1])
        print(calculationResults.roiPercent()[1])


        return render_template("analyse.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
