class Return_roi():
    
    def __init__(self):
        self.current_user = None
        self.name = input("What is your name? ").title()
        self.portfolio = ['dummy']
        self.income = {}
        self.expenses = {}
        self.cashflow = []
        self.roi = {}
    
    def __str__(self):
        return self.name
    
    def create_portfolio(self):
        self.portfolio.append(self.name)
        self.current_user = self.name
        print(f"Welcome {self.name}! Your portfolio has been created. Let's calculate your ROI. ")
    def get_income(self):
        print("We are now going to calculate your total income, please enter your income stream in numbers.")
        self.rental_income = input(f"How much is your rental income, {self.name}? ")
        self.income["rental income"]=int(self.rental_income)
        self.laundry_income = input("Income from laundry? ")
        self.income["laundry"]=int(self.laundry_income)
        self.storage_income = input(f"Alright {self.name}, now What about storage? ")
        self.income["storage"]=int(self.storage_income)
        self.additional_income = input("If you have any more additional income, please list the value here. ")
        self.income["additional income"]=int(self.additional_income)
        income_stream = [val for val in self.income.values()]
        self.total_income = sum(income_stream)
        self.list_of_incomes = [key for key in self.income]
        self.final_list_of_incomes = (', '.join(self.list_of_incomes))
        print(f"{self.name}. From {self.final_list_of_incomes} your total rental income is: ${self.total_income}.")

    def get_expenses(self):
        print("For the following questions, please enter your expenses in numbers, and enter '0' if you do not occur any of these expenses.")
        self.taxes = input("Now, how much do you pay in taxes per month? ")
        self.expenses["taxes"] = int(self.taxes)
        self.insurance = input("Insurance? ")
        self.expenses["insurance"] = int(self.insurance)
        self.utilities = input(f"How about utilities {self.name}? Please consider water, electricity, gas, etc. ")
        self.expenses["utilities"] = int(self.utilities)
        self.hoa = input("Homeowner association fees? ")
        self.expenses["HOA"] = int(self.hoa)
        self.capital_expenditure = input("Please list how much you set aside for your capital expenditure. ")
        self.expenses["capital expenditure"] = int(self.capital_expenditure)
        self.mortgage = input("How much is your mortgage per month? ")
        self.expenses["mortgage"] = int(self.mortgage)
        self.repair = input("Please average how much you spend on repairs each month. ")
        self.expenses["repair"] = int(self.repair)
        self.vacancy = input("Roughly how much does your vacancy cost you? ")
        self.expenses["vacancy"] = int(self.vacancy)
        self.extraexpense = input(f"Finally {self.name}, please enter in any additional expenses we might've missed. ")
        self.expenses["extra expenses"] = int(self.extraexpense)
        expense_stream = [val for val in self.expenses.values()]
        self.total_expenses = sum(expense_stream)
        self.list_of_expenses = [key for key in self.expenses]
        self.final_list_of_expenses = (', '.join(self.list_of_expenses))
        print(f"{self.name}, with your monthly expenses being\n{self.final_list_of_expenses}.\nThey total up to ${self.total_expenses}.")
    
    def get_annual_cashflow(self):
        self.monthly_cashflow = self.total_income - self.total_expenses 
        self.annual_cashflow = self.monthly_cashflow*12
        print(f"{self.name} With your monthly cashflow being ${self.monthly_cashflow}, your annual cashflow is ${self.annual_cashflow}")
        
    
    def get_roi(self):
        print("We're almost done, let's figure out what you've invested so we can calculate your ROI percentage.")
        self.downpayment = input("How much did you invest as down payment?")
        self.roi["down payment"] = int(self.downpayment)
        self.closingcosts = input("How much did you pay for closing?")
        self.roi["closing costs"] = int(self.closingcosts)
        self.repaircosts = input("Repairs?")
        self.roi["repairs"] = int(self.repaircosts)
        self.finalcosts = input(f"Finally {self.name}, please enter in any additional investments you've made.")
        investment_stream = [val for val in self.roi.values()]
        self.total_investment = sum(investment_stream)
        self.list_of_investment= [key for key in self.roi]
        self.final_list_of_investment = (', '.join(self.list_of_investment))
        print(f"{self.name}, with your inititial investments being\n{self.final_list_of_investment}.\nThey total up to ${self.total_investment}.")
        self.roi_percentage = self.annual_cashflow/self.total_investment
        print(f"Through calculations, your return on investment percentage is {self.roi_percentage:.2f}%. Thank you for trusting us with your calculation!")
        
    def view_roi(self):
        print(f"With all the calculations, your current percentage is {self.roi_percentage:.2f}%.")

    
def run_roi():
    client = Return_roi() 

    client.create_portfolio()
    client.get_income()
    client.get_expenses()
    client.get_annual_cashflow()
    client.get_roi()

    option = input("Would you like to edit:\n1. Income\n2. Expenses\n3. Quit\n")
    while option not in {'1' ,'2', '3'}:
        option = input("Invalid option. Please choose 1, 2, or 3")
    if option == "1":
        print("We will update your information on your rental income.")
        client.get_income()
        print(f"Your income has been updated.")
    elif option == "2":
        print("We will update your information on your rental expenses")
        client.get_expenses()
    elif option == "3":
        pass
    print("Thanks for trying us out!")

run_roi()
    