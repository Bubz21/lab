import unittest
from account import *

class MyTestCase(unittest.TestCase):
    def test___init__(self):
        self.account1 = account('Bob') # creates an account with the name bob 
        self.account2 = account('Sally') # creates an account with the name sally 

    def test_deposit(self):
        self.asserEqual(self.account1.deposit(200), 200) # adds 200 to the deposit
        self.asserEqual(self.account1.deposit(0), 200) # nothing is added because 0
        self.asserEqual(self.account1.deposit(-100), 200) # can not add a negative number
        
        self.asserEqual(self.account2.deposit(400), 400) # adds 400 to the deposit
        self.asserEqual(self.account2.deposit(0), 400) # nothing is added because 0
        self.asserEqual(self.account2.deposit(-100), 400) # can not add a negative number
        
    def test_withdraw(self):
        self.asserEqual(self.account1.deposit(100), 100) # subtracts 100 from the deposit
        self.asserEqual(self.account1.deposit(0), 200) # nothing is subtracted because 0
        self.asserEqual(self.account1.deposit(-100), 200) # can not add a negative number
        
        self.asserEqual(self.account2.deposit(200), 200) # subtracts 200 from the deposit
        self.asserEqual(self.account2.deposit(0), 400) # nothing is subtracted because 0
        self.asserEqual(self.account2.deposit(-100), 400) # can not add a negative number


if __name__ == '__main__':
    unittest.main()
