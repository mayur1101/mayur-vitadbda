####1)Find the max of three numbers.
##no1=int(input("Enter the number 1:"))
##no2=int(input("Enter the number 2:"))
##no3=int(input("Enter the number 3:"))
##if no1>no2:
##    print(no1)
##elif no2>no3:
##    print(no2)
##else:
##    print(no3)

####2)Write a Python program to detect the number of local variables declared in a function.
##def localvar():
##    a=[1,2,3,4]
##    b=8
##    c=4.8
##    d="Mayur"
##    print(len(locals()))
##localvar()
    
####3)Write a recursive function to calculate the sum of numbers from 0 to 10
####Expected output: 55
##def sum(n):
##    if n<1:
##        return n
##    else:
##        return n+sum(n-1)
##print(sum(10))

####4)Create a function showStudent() in such a way that it should accept student id
####,name,and it’s college name  and if the id and college name is missing in function
####call it should show it as by default id is 1 and college name  is VITA.
##def showStudent(name,colid=1,colname="Vita"):
##    print(name," ",colid," ",colname," ")
##showStudent("mayur")

####5)Write a Python function that takes a list and returns a new list with unique elements of the first list.
####Sample List : [11,22,22,33,33,33,44,55,55,66]
####Unique List : [11, 22,33, 44, 55,66]
##l1=[11,22,22,33,33,33,44,55,55,66]
##print("Sample list:",l1)
##l2=set(l1)
##print("Unique list:",sorted(l2))

####6)Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
####1st for first digit
####2nd for last digit
####Example:
#### Input:  5424
####Output: 9
def first(n):
    l1=[]
    while n!=0:
        d=n%10
        l1.append(d)
        l1.reverse()
        n=n//10
    for i in range(0,1):
        return l1[i]
        
def last(n):
    d=n%10
    return d
n=int(input("Enter the number:"))
c=first(n)
d=last(n)
c=c+d
print("Sum of 1st and last digit is:",c)







