##1.Write python program to perform bank operations using class and objects.
##Conditions:
##a.Bank name should be static.
##b.Using menu driven program.
##1.Deposit
##2.Withdraw
##3.Exit

##class Bank:
##    bankname="MAYUR BANK"
##    def __init__(self):
##        self.balance=5000
##        print("Your current balance is ",self.balance)
##        
##    def Deposit(self):
##        amount=int(input("Enter the amount to be deposited:"))
##        self.balance=self.balance+amount
##        print()
##        print(amount,"is deposited to your account")
##        print("Your current balance is:",self.balance)
##
##    def Withdraw(self):
##        amount=int(input("Enter the amount to withdraw:"))
##        print()
##        if self.balance<amount:
##            print("Insufficient balance")
##        else:
##            self.balance=self.balance-amount
##            print(amount,"has been withdraw")
##
##    def Exit(self):
##        print()
##        print("Exited from your account")
##
##print("Welcome to",Bank.bankname)
##print("Enter your choice to select option:\n1)Deposit\n2)Withdraw\n3)Exit")
##n=int(input("Enter the number to select the option: "))
##mayur=Bank()
##if n==1:
##    mayur.Deposit()
##elif n==2:
##    mayur.Withdraw()
##elif n==3:
##    mayur.Exit()

####2)Write a Python class named Circle constructed by a radius and two
####methods which will compute the area and the perimeter of a circle.
##class Circle:
##    def __init__(self):
##        self.r=int(input("Enter the radius"))
##        
##    def Area(self):
##        area=3.147*self.r**2
##        print("Area of the circle is ",area) 
##
##    def Perimeter(self):
##        perimeter=2*3.147*self.r
##        print("Perimeter of the circle is",perimeter)
##
##c1=Circle()
##c1.Area()
##c1.Perimeter()

####3)Define a class named Shape and its subclass Square. The Square class has an init function which takes
####a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
####Hints:
####To override a method in super class, we can define a method with the same name in the super class.
##class Shape:
##    def area(self):
##        self.area=0
##        print("Area of shape is",self.area) 
##
##class Square(Shape):
##    def __init__(self,length):
##        self.length=length
##
##    def area(self):
##        super().area()
##        self.area=self.length**2
##        print("Area of square is",self.area)
##
##length=int(input("Enter the length: "))
##s1=Square(length)
##s1.area()

####4)Write a program to count how many reference variables in a program.
##import sys
##a="Hii mayur here"
##print(sys.getrefcount(a))
 
####5)write any program to achieve composition in Python
##class Salary:
##    def __init__(self,sal,bonus):
##        self.sal=sal
##        self.bonus=bonus
##
##    def annual_salary(self):
##        return self.sal*12+self.bonus
##
##class Employee:
##    def __init__(self,name,age,sal,bonus):
##        self.name=name
##        self.age=age
##        self.obj_salary=Salary(sal,bonus)
##
##    def cal_salary(self):
##        return self.obj_salary.annual_salary()
##
##emp1=Employee("Mayur",24,30000,5000)
##print(emp1.cal_salary())


    
        
