#challenge 1 ----------------------------
class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sample_list = [self.x,self.y,self.z]
        result = [number ** 2 for number in sample_list]
        
        sum_of_result = sum(result)
        return sum_of_result

l = Point(1,3,5)
print(l.sqSum()) 

#challege 2----------------------------------------
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        a = self.num1 + self.num2
        print(a)
    def subtract(self):
        s = self.num1 - self.num2
        print(s)
    def multiply(self):
        m = self.num1 * self.num2
        print(m)
    def divide(self):
        d =self.num2 / self.num1
        print(d)

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide() 

#challenge 3---------------------------------------
class Student:

    def __init__(self,name,rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber


    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

x = Student('Anitha', 4)
print(x.getName())
x.setName('Anitha')
print(x.getRollNumber())
x.setRollNumber(4)        

#challenge 4-----------------------------------

class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
savings_account = SavingsAccount("Ashish", 5000, 5)

print(account)
print(savings_account)

#challenge 5-------------------------------

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title= None, balance= 0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100
    
demo1 = SavingsAccount("Ashish", 2000, 5)

demo1.deposit(500)
print(demo1.getBalance())  

demo1.withdrawal(500)
print(demo1.getBalance())  

print(demo1.interestAmount())