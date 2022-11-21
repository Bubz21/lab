class Account:
  """
  A class repressing details for an account
  """
  def __init__(self,name):
    """
    Constructor to create initial state of an account object
    :param name: Person's first name
    :param balance: total amount of balance
    """
    self.__account_name = name
    self.__account_balance = 0
  
  def deposit(self,amount):
    """
    Method to add to the account's balance
    :return: True if the transaction is sucussesful
    :return: False if the transaction is unsucussesful
    """
    if amount > 0:
      self.__account_balance = self.__account_balance + amount # adds the amount to the current balance
      return True
    else:
      return False
    
  def withdraw(self,amount)
  """
  Method to remove from the account's balance
  :return: True if the transaction is sucussesful
  :return: False if the transaction is unsucussesful
  """
    if (amount > 0) and (amount < account_balance):
      self.__account_balance = self.__account_balance - amount # subtracts the amount from the current balance
      return True
    else:
      return False
    
  def get_balance(self):
    """
    Method to access the account balance
    :return: The account's balance
    """
    return self.__account_balance
    
  def get_name(self):
    """
    Method to access the account name
    :return: The account's name
    """
    return self.__account_name
