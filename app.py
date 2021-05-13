from bs4 import BeautifulSoup as bs4
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from googleAPI import sheetsUpd
import gspread
import requests
import os

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


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

        #spreadsheet_id = '1ag4C3fVMZRnoBeE3maBOB1nygAbNWF3uQYyi5P43l5M'
        #gc = gspread.service_account(filename='credentials.json')
        #sh = gc.open_by_key(spreadsheet_id)
        #analysis_worksh = sh.sheet1

        #analysis_worksh.update_cell(2,3, "test2")
        #price = request.form["prop_price"]
        #analysis_worksh.update_cell(2, 3, price)
        #return render_template("analyse.html")


        #prices=[]
        #url = request.args.get("url")
        #newurl = requests.get(url)
        #soup = bs4(newurl.text, 'html.parser')

        #for tags in soup.findAll(attrs={"class" : "d-text d-fontSize--larger"}):
            #price = tags.getText()
            #prices.append(price)
        # print(soup1)
        #return render_template("analyse.html", name=prices)


if __name__ == '__main__':
    app.debug = True
    app.run()
