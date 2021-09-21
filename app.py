from bs4 import BeautifulSoup as bs4
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from Webscrapper.Calculator import calculateDown, calculateCost, calculateMortgage, \
    calculateExpense, calculateProfit, calculateRoi
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

        ##sheetsUpd(price, down, rent, expense, tax, interest)
        downPayment = calculateDown(price, down)
        totalCost = calculateCost(price,downPayment)
        mortgage = calculateMortgage(price, downPayment, interest)

        #array of size 2, [0] = worst case, [1] = best case
        monthExp = calculateExpense(rent, expense, mortgage, tax)
        monthWorstCaseExp = monthExp[0]
        monthBestCaseExp = monthExp[1]
        print(monthWorstCaseExp)
        print(monthBestCaseExp)

        monthProfit = calculateProfit(rent, monthExp)
        monthWorstProfit = monthProfit[0]
        monthBestProfit = monthProfit[1]

        roi = calculateRoi(monthProfit, totalCost)

        roiWorst = roi[0]
        roiBest = roi[1]


        print(mortgage)
        print(monthWorstProfit)
        print(monthBestProfit)
        print(totalCost)
        print (roiWorst)
        print(roiBest)



        return render_template("analyse.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
