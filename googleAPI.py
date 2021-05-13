import gspread
from flask import Flask, render_template, request

def sheetsUpd(price, down, rent, expense, tax, interest):
    #Call sheets API
    SPREADSHEET_ID = '1ag4C3fVMZRnoBeE3maBOB1nygAbNWF3uQYyi5P43l5M'
    SECRET_FILE = 'credentials.json'

    gc = gspread.service_account(filename= SECRET_FILE)
    sh = gc.open_by_key(SPREADSHEET_ID)
    analysis_worksh = sh.sheet1

    analysis_worksh.update_cell(4, 3, price)

    #for down payment user needs to write percentage and I need to use it to calculate the downpayment
    #analysis_worksh.update_cell(4, 3, down)
    analysis_worksh.update_cell(13, 3, rent)

    #for expense I need to allow user to write the type of expense and the amount and it show append in sheets
    analysis_worksh.update_cell(8, 12, expense)

    #for tax I need to give option to choose moncton or mtl and then for mtl they have 2 taxes to fill
    analysis_worksh.update_cell(15, 3, tax)

    #need to be able to put a decimal number
    analysis_worksh.update_cell(8, 3, interest)
    #return render_template("analyse.html")