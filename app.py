from bs4 import BeautifulSoup as bs4
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
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

    return render_template("analyse.html")
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
    app.debug=True
    app.run()
