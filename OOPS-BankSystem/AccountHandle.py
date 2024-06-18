# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    #debit method

    def debit(self, amount):
        self.balance -= amount
        print("From", self.account_no , "Rs",amount , "was debited. ")
        print("-------------------------------------------------")
        print("Total balance is Rs", self.get_balance(),"\n")

    #creadit method

    def credit(self, amount):
        self.balance += amount
        print("**************************************************")
        print("To", self.account_no ,"Rs", amount , "was credited. ","\n")
        print("-------------------------------------------------")
        print("Total balance is Rs", self.get_balance(),"\n")
        print("**************************************************")

    #Total balance method

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 343278912342)
acc1.debit(2000)
acc1.credit(4000)

acc2 = Account(90000, 399978918924 )
acc2.debit(10000)
acc2.credit(2000)

acc2 = Account(30000, 376578911199 )
acc2.debit(30000)
acc2.credit(20000)