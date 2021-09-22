class Calculations:
    downP = 0
    totalCash = 0
    mortgageAmount = 0
    monthExpense = []
    monthProfit = []
    roi = []
    def __init__(self, price, down, rent, expense, tax, interest):
        self.price = price
        self.down = down
        self.rent = rent
        self.expense = expense
        self.tax = tax
        self.interest = interest


#call calculator functions
#must convert variables from string to int
    def downPayment(self):
    #calculate downpayment
        self.downP = self.price * self.down / 100
        return self.downP

    def totalCost(self):
        #calculate closing and total cash needed
        closing = self.price*0.02
        self.totalCash = self.downP + closing
        return self.totalCash

    def mortgageCost(self):
        principal = self.price - self.downP
        #monthly interest
        m_int = self.interest/12/100
        #compound interest
        #term in months = 25 years * 12 month = 300
        c_int = (1 + m_int)**300
        self.mortgageAmount = (principal*m_int*c_int)/(c_int-1)
        return self.mortgageAmount

    def monthlyExpense(self):
        ##calculate worst and best case expense
        #Expense is array w 2 elements, entry [0] = worst case, entry [1] = best case
        reMa = 0.05 * self.rent
        vac = 0.03 * self.rent
        capExp = 0.05 * self.rent
        proMang = 0.07 * self.rent
        insurance = 1500

        self.monthExpense.append(reMa + vac + capExp + proMang + self.expense + self.tax / 12 + self.mortgageAmount + insurance / 12)
        self.monthExpense.append(self.expense+ self.tax/12+ self.mortgageAmount+ insurance/12+ proMang)

        return self.monthExpense

    def profit(self):
        self.monthProfit.append(self.rent - self.monthExpense[0])
        self.monthProfit.append(self.rent - self.monthExpense[1])

        return self.monthProfit

    def roiPercent(self):
        self.roi.append(self.monthProfit[0] * 12 / self.totalCash * 100)
        self.roi.append(self.monthProfit[1] * 12 / self.totalCash * 100)

        return self.roi