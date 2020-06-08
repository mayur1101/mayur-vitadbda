####1)Write a function to compute divide by zero and use try/except to catch the exceptions.
##try:
##    num1=int(input("Enter the number 1:"))
##    num2=int(input("Enter the number 2:"))
##    num3=num1/num2
##    print(num3)
##except Exception as arg:
##    print("Exception raised:",arg)
##else:
##    print("Exception not raised")

####2)Write python program to check  that given number is valid mobile number or not?
##import re
##regex="^[0-9]{10}$"
##def check(mobilenum):
##    if re.search(regex,mobilenum):
##        print("Valid mobile number")
##    else:
##        print("Invalid mobile number")
##
##mobilenum=input("Enter the mobile number to check:")
##check(mobilenum)

####3)Write python program to check  that given email address is valid   or not?
##import re
##regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
##def check(emailid):
##    if re.search(regex,emailid):
##        print("Valid emailid")
##    else:
##        print("Invalid emailid")
##    
##emailid=input("Enter the email address to check:")
##check(emailid)

####4)Write a python program to check given car registration number is valid Maharashtra state registration number or not?
##import re
##regex="[MH]+[19]+[A-Z]+[0-9]"
##def check(carno):
##    if re.search(regex,carno):
##        print("Valid registration number")
##    else:
##        print("Invalid registration number")
##    
##carno=input("Enter the email address to check:")
##check(carno)

####5)Write a python program to decorate arithmetic operations.
##def div(a,b):
##    print(a/b)
##
##def smart_div(func):
##
##    def inner(a,b):
##        if a<b:
##            a,b=b,a
##            return func(a,b)
##
##    return inner
##
##div=smart_div(div)
##div(2,4)

####6)Write a python program to generate Fibonacci Numbers upto 100 using generator.
##def fibonacci(n):
##    a, b, counter = 0, 1, 0
##    while True:
##        if (counter > n): return
##        yield a
##        a, b = b, a + b
##        counter += 1
##f = fibonacci(5)
##for x in f:
##    print(x)

