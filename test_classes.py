import unittest
from account import *

class MyTestCase(unittest.TestCase):
    def test___init__(self):
        self.account1 = account('Bob', 300)
        self.account2 = account('Sally', 500)

    def test_deposit(self):
        self.asserEqual(self.account1.deposit(200), 500)
        self.asserEqual(self.account1.deposit(0), 300)
        self.asserEqual(self.account1.deposit(-100), 300)
        
        self.asserEqual(self.account2.deposit(200), 700)
        self.asserEqual(self.account2.deposit(0), 500)
        self.asserEqual(self.account2.deposit(-100), 500)
        
    def test_withdraw(self):
        self.asserEqual(self.account1.deposit(200), 100)
        self.asserEqual(self.account1.deposit(0), 300)
        self.asserEqual(self.account1.deposit(-100), 300)
        
        self.asserEqual(self.account2.deposit(200), 300)
        self.asserEqual(self.account2.deposit(0), 500)
        self.asserEqual(self.account2.deposit(-100), 500)


if __name__ == '__main__':
    unittest.main()
