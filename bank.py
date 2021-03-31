class BankAccount:
  def __init__(self):
    self.balance = 0
  def __str__(self):
    return f'my bank acc has a balance of ${self.balance}'

  def deposit(self, amount):
    if(amount <= 0):
      return False
    self.balance += amount

  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * .02)

  def withdraw(self, amount):
    if(amount <= 0):
      return False
    self.balance -= amount

class ChildrensAccount(BankAccount):
  def accumulate_interest(self):
    self.balance += 10
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self):
    self.overdraft_penalty = 40
    super().__init__()
  
def withdraw(self, amount):
  result = self.balance - amount
  if result < 0: 
    self.balance -= self.overdraft_penalty
    return False
  super().withdraw(amount)
# my_account = BankAccount()
# deposit = my_account.deposit(-3200)
# print(deposit)
# print(my_account)



try:
  basic_account = BankAccount()
  basic_account.deposit(600)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.withdraw(17)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.accumulate_interest()
  print("Basic account has ${}".format(basic_account.balance))
  print()
except Exception as e:
  print(e)

try:
  childs_account = ChildrensAccount()
  childs_account.deposit(34)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.withdraw(17)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.accumulate_interest()
  print("Child's account has ${}".format(childs_account.balance))
  print()
except Exception as e:
  print(e)
  

try:
  overdraft_account = OverdraftAccount()
  overdraft_account.deposit(12)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.withdraw(17)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.accumulate_interest()
  print("Overdraft account has ${}".format(overdraft_account.balance))
except Exception as e:
  print(e)
