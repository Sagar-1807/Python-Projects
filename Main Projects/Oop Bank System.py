# BANKING SYSTEM USING OOP

#USER-PARENT CLASS-DETAILS OF USER
class User():
    def __init__(self,name,age,gender):
        self.name=name                          #1
        self.age=age                            #2 (These all called attributes.)
        self.gender=gender                      #3

    def user_details(self):
        print("Personal details:")
        print("--User Name:",self.name)
        print("--Age:",self.age)
        print("--Gender:",self.gender)

#CHILD CLASS

class bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)   #super= to avoid writing 1,2,3 attributes
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance + self.amount
        print("Your Account balnce is Rs.=",self.balance),print("")

    def withdraw(self,amount):
        self.amount=amount
        if self.amount > self.balance:
            print("insufficient balance! \n Available balance is=",self.balance)
        else:
            self.balance=self.balance - self.amount
            print("Now u can withdraw.!\nAvailable balance is=", self.balance)

    def viewbal(self):
        print("balance is:", self.balance)

person=bank('sagar',32,'male')
print(person.user_details())
person.deposit(5000)
# print(person.withdraw(400))
print(person.viewbal())
















