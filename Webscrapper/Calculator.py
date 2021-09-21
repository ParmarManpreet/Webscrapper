
#call calculator functions
#must convert variables from string to int
def calculateDown(price, down):
    #calculate downpayment
    downP = price * down/100
    return downP

def calculateCost(price, downPayment):
    #calculate closing and total cash needed
    closing = price*0.02
    totalCash = downPayment + closing
    return totalCash

def calculateMortgage(price, downPayment, interest):
    principal = price - downPayment
    #monthly interest
    m_int = interest/12/100
    #compound interest
    #term in months = 25 years * 12 month = 300
    c_int = (1 + m_int)**300
    mortgage = (principal*m_int*c_int)/(c_int-1)
    return mortgage

def calculateExpense(rent, expense, mortgage, tax):
    ##calculate worst and best case expense
    #Expense is array w 2 elements, entry [0] = worst case, entry [1] = best case
    monthExpense = []
    reMa = 0.05 * rent
    vac = 0.03 * rent
    capExp = 0.05 * rent
    proMang = 0.07 * rent
    insurance = 1500

    monthExpense.append(reMa + vac + capExp + proMang + expense + tax / 12 + mortgage + insurance / 12)
    monthExpense.append(expense+tax/12+mortgage+insurance/12+proMang)

    return monthExpense

def calculateProfit(rent, monthExpense):
    monthProfit = []
    monthProfit.append(rent - monthExpense[0])
    monthProfit.append(rent - monthExpense[1])

    return monthProfit

def calculateRoi(monthProfit, totalCost):
    roi = []
    roi.append(monthProfit[0] * 12 / totalCost * 100)
    roi.append(monthProfit[1] * 12 / totalCost * 100)

    return roi