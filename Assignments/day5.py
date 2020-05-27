####1.Write a Python program to sort a list of elements using the bubble sort Algorithm.
##def bubble_sort(l1):
##    temp=0
##    for i in range(len(l1)-1):
##        for j in range(len(l1)-1-i):
##            if l1[j]>l1[j+1]:
##                l1[j],l1[j+1]=l1[j+1],l1[j]
##    print(l1)           
##l1=[5,3,4,2,1]
##bubble_sort(l1)

####2)Write a Python program for sequential search (Linear search).
##def search(l1,n):
##      for i in range(len(l1)):
##          if n==l1[i]:
##              print(n,"number is present at index",i)
##              break
##      else:
##          print(n,"Number is not present")
##l1=[1,2,3,4,5]
##n=int(input("Enter the number to be searched"))
##search(l1,n)

####3)Write a Python program for Binary search.
##def binary_search(l1,n):
##    sl1=sorted(l1)
##    l=0
##    u=len(sl1)-1
##    flag=0
##    while l<=u:
##        m=(l+u)//2
##        if n > sl1[m]:
##            l=m+1
##        elif n < sl1[m]:
##            u=m-1
##        else:
##            flag=1
##            return flag
##l1=[5,2,4,5,8,3,2,1,9,10]
##n=int(input("Enter the number to be searched"))
##c=binary_search(l1,n)
##if c==1:
##    print("Number is found")
##else:
##    print("Number is not found")

####4)Write a python program to concatenate two lists index-wise.
####List1 = [“M”,”na”,”i”,”lak”]
####List2 = [“y”,”me”,”s”,”han”]
####Expected output:
####[“My”,”name”,”is”,”lakhan”]
##l1=["M","na","i","may"]
##l2=["y","me","s","ur"]
##l3=[]
##for i,j in zip(l1,l2):
##        l3.append(i+j)
##print(l3)

####5)Iterate a given list and check if a given element already exists in a dictionary as a key’s value if not delete it
####from the list.
##roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
##sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
def sortedlist(l1,sdic):
    for i in sdic:
        for j in l1:
            if j==sdic[i]:
                l1.remove(j)
    print(l1)
l1=[47,64,69,37,76,83,95,97]
sdic={"John":47,"Peter":64,"Mahi":37,"Maria":76}
sortedlist(l1,sdic)
