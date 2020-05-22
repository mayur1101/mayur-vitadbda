####1)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
####between 2000 and 3200 (both included).
####The numbers obtained should be printed in a comma-separated sequence on a single line.
##str1=""
##start=int(input("Enter the start number"))
##end=int(input("Enter the end number"))
##for i in range(start,end+1):
##    if i%7==0 and i%5!=0:
##        str1=str1+str(i)+","
##print(str1[:-1])



####2)With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
####Suppose the following input is supplied to the program:
####8
####Then, the output should be:
####{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
####Hints:
####In case of input data being supplied to the question, it should be assumed to be a console input.
####Consider use dict()

##n=int(input("Enter the number to generate dictionary:"))
##dic=dict()
##for i in range(1,n+1):
##    dic[i]=i*i
##print(dic)



####3)Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
####Suppose the following input is supplied to the program:
####Hello world
####Practice makes perfect
####Then, the output should be:
####	HELLO WORLD
####	PRACTICE MAKES PERFECT

##list1=[]
##n=int(input("Enter the number of lines to be entered:"))
##for i in range(n):
##    t=input()
##    list1.append(t)
##for i in list1:
##    print(i.upper())



####4)Write a program to check wheather number is even or odd using if 
####Else statement…

##n=int(input("Enter the number"))
##if n%2==0:
##    print("even")
##else:
##    print("odd")



####5)program that grants access only to kids aged between 8-12
####using  if  else statement
####Hint::
####If aged between 8 to 12 then you are allowed… welcome!!
####Otherwise Sorry not allowed ..Bye!
n=int(input("Enter your age"))
if n>=8 and n<=12:
    print("You are allowed....welcome!!")
else:
    print("Sorry not allowed....Bye!!")


    
