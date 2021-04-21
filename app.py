from bs4 import BeautifulSoup as bs4
import requests
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/analyse")
def analyse():
    prices=[]
    url = request.args.get("url")
    newurl = requests.get(url)
    soup = bs4(newurl.text, 'html.parser')

    for tags in soup.findAll(attrs={"class" : "d-text d-fontSize--larger"}):
        #soup = soup.findAll(attrs={"class" : "d-text d-fontSize--larger"}).getText()
        price = tags.getText()
        prices.append(price)
    # print(soup1)
    return render_template("analyse.html", name=prices)


if __name__ == '__main__':
    app.run()
