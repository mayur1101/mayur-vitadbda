####1.	Python Program to Read a Number n And Print the Series “1+2+…..+n= “
####sample:
####Case 1:
####Enter a number: 4
####1 + 2 + 3 + 4 = 10 
####Case 2:
####Enter a number: 5
####1 + 2 + 3 + 4 + 5 = 15
##n=int(input("Enter the number:"))
##res=0
##list1=[]
##for i in range(1,n+1):
##    res=res+i
##    list1.append(str(i))
##print("+".join(list1),"=",res)

####Write a Python program to count the number of even and odd numbers from a series of numbers.

##Sample numbers :
##numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##Expected Output :
##Number of even numbers : 4
##Number of odd numbers : 5
##numbers=[1,2,3,4,5,6,7,8,9]
##cnt=0
##cnt1=0
##print(numbers)
##for i in numbers:
##    if i%2==0:
##        cnt+=1
##    else:
##        cnt1+=1
##print("Number of even numbers:",cnt)
##print("Number of odd numbers:",cnt1)

####3).Write a Python program to create the multiplication table (from 1 to 10) of a number
##n=int(input("Enter the number:"))
##for i in range(1,11):
##    print(n,"*",i,"=",n*i)
    
####4)Given the triangle of consecutive odd  number.
##Above triangle is given Calculate Sum row wise 
##Example we call function :- row_sum_odd_numbers(2)
##Result will be=3 + 5 = 8
##if user give 4 then ur output is 13 + 15 + 17+ 19 = 64
##def row_sum_odd_numbers(n):
##    list1=[]
##    for i in range(n):
##        list1.append([])
##
##    a=1
##    for i in range(n):
##        for p in range(1,i+2):
##            list1[i].append(a)
##            a=a+2
##        
##    return sum(list1[n-1]),list1
##n=int(input("Enter the number"))
##s,l=row_sum_odd_numbers(n)
##l2=[]
##for i in l[n-1]:
##    l2.append(str(i))
##print("+".join(l2),"=",s)

####5)5.Write python program to print the pattern given below
##Note: Take input from user
##1
##2 2
##3 3 3
##4 4 4 4
##5 5 5 5 5
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
    





