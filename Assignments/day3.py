####1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
##list=[1,2,3,4]
##res=[i*i for i in list]
##print(res)

####2)From a list containing ints, strings and floats, make three lists to store them separately.
##l1=[1,3,"mayur",4.07,"rashu",5.85]
##string_list=[]
##integer_list=[]
##float_list=[]
##print(l1)
##for i in l1:
##    if isinstance(i,int):
##        integer_list.append(i)
##    if isinstance(i,str):
##        string_list.append(i)
##    if isinstance(i,float):
##        float_list.append(i)
##print(integer_list)
##print(string_list)
##print(float_list)

####3)Print the pattern
####1
####1 2 
####1 2 3
####1 2 3 4
####1 2 3 4 5
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()

####4)Accept data in two 3*3  matrix and calculate the sum of the matrices.
##import numpy as np
##l1=np.array([[1,2,3],[4,5,6],[7,8,9]])
##l2=np.array([[1,2,3],[4,5,6],[7,8,9]])
##l3=l1+l2
##print(l3)

####5)Write a Python program to check whether a given number is a narcissistic number or not
####For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
####153 = 13 + 53 + 33
####370 = 33 + 73 + 03
####407 = 43 + 03 + 73.
####There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
####1634 = 14+64+34+44
####8208 = 84+24+04+84
####9474 = 94+44+74+44
def check(n):
    s=0
    while n!=0:
        d=n%10
        s=s+(d*d*d)
        n=n//10
    return s
n=int(input("Enter the number:"))
c=check(n)
if c==n:
    print("narcissistic number")
else:
    print("not narcissistic number")
