class PersonAccount:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self,source,income):
        self.incomes[source]=income

    def show_incomes(self):
        return self.incomes

    def add_expense(self,source,amount):
        self.expenses[source]=amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (
            f"Name: {self.firstname} {self.lastname}\n"
            f"Total Income: ₹{self.total_income()}\n"
            f"Total Expense: ₹{self.total_expense()}\n"
            f"Account Balance: ₹{self.account_balance()}"
        )


man = PersonAccount("Aditya", "Verma")

# Incomes
man.add_income("Salary", 50000)
man.add_income("Freelancing", 12000)
man.add_income("Bonus", 5000)
man.add_income("Investment", 3000)

# Expenses
man.add_expense("Rent", 15000)
man.add_expense("Food", 7000)
man.add_expense("Internet", 1200)
man.add_expense("Electricity", 2500)
man.add_expense("Entertainment", 3000)
man.add_expense("Travel", 4500)

print(man.show_incomes())   # Optional
print(man.account_info())