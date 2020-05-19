#1)Write a Python program to sum all the items in a list.
##list=[3,23,7,12,55]
##print(sum(list))

#2)Write a Python program to multiplies all the items in a list.
##list=[1,2,3,4,5]
##mul=1
##for i in list:
##    mul=mul*i
##print("multiplication odf all numbes is:",mul)

#3)Write a Python program to get the largest number from a list.
##list=[1,4,2,7,8]
##print(max(list))

#4)Write a Python program to get the smallest number from a list.
##list=[34,21,67,21,90]
##print(min(list))

#5)Write a Python program to count the number of strings where the string length
#is 2 or more and the first and last character are same from a given list of strings. 
##def match_words(word):
##    cnt=0
##    for i in word:
##        if len(i)>1 and i[0]==i[-1]:
##            cnt=cnt+1
##    print("count",cnt)
##
##match_words(['mayum','priya','rashu','uju'])


#6)Write a Python program to get a list,
#sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
##def last(n):
##    return n[-1]
##def sort_list_last(tuples):
##  return sorted(tuples, key=last)
##
##print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7)Write a Python program to remove duplicates from a list.
##list=[2,4,7,2,3]
##list1=set(list)
##print(list)
##print(list1)

#8)Write a Python program to check a list is empty or not.
##def check(list):
##        if len(list)==0:
##            return 1
##        else:
##            return 0
##
##list=[]
##if check(list):
##    print("list is empty")
##else:
##    print("list is not empty")

#9)Write a Python program to clone or copy a list.
##list=[2,3,89,3,6,7]
##list1=list.copy()
##print(list)
##print(list1)

#10)Write a Python program to find the list of words that are longer than n from a given list of
#words.
##def check_word(n,list):
##     for i in list:
##         if len(i)>n:
##             print(i)
##
##check_word(3,['i','am','mayur','chaudhari'])

#11)Write a Python function that takes two lists and returns True if they have at least one
#   common member. 
##def common_data(list1,list2):
##    result=False
##    for i in list1:
##        for j in list2:
##            if i==j:
##                result=True
##                return True
##
##c=common_data([1,2,3,4,5],[2,3,4,1])
##if (c):
##    print("Lists have common member")
##else:
##    print("No common")
    
#12)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.     
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
##def remove(list):
##    for i in list:
##        if i==Red or i==White or i==Yellow:
##            list.remove(i)
##            
##
##
##remove(['Red','Green','White','Black','Pink','Yellow'])


#13)Write a Python program to generate a 3*4*6 3D array whose each element is *.
##array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
##print(array)

#14) Write a Python program to print the numbers of a specified list after removing
#even numbers from it. 
##def remove(list):
##    list1=[]
##    for i in list:
##        if i%2==1:
##            list1.append(i)
##    return list1
##
##list1=remove([1,2,3,4,5])
##print(list1)


#15)Write a Python program to shuffle and print a specified list.
##from random import shuffle
##list=[2,4,1,5,7,7]
##shuffle(list)
##print(list)

#16)Write a Python program to generate and print a list of first and last 5 elements where the
#values are square of numbers between 1 and 30 (both included). 
##def printValues():
##	l = list()
##	for i in range(1,31):
##		l.append(i**2)
##	print(l[:5])
##	print(l[-5:])
##
##printValues()

#17)Write a Python program to generate and print a list except for the first 5 elements,
#where the values are square of numbers between 1 and 30 (both included). 
##def printValues():
##	l = list()
##	for i in range(1,21):
##		l.append(i**2)
##	print(l[5:])
##
##printValues()

#18)Write a Python program to generate all permutations of a list in Python.
##import itertools
##print(list(itertools.permutations([1,2,3])))

#19)Write a Python program to get the difference between the two lists.
##list1 = [1, 2, 3, 4]
##list2 = [1, 2]
##print(list(set(list1) - set(list2)))

###20)Write a Python program access the index of a list.
##nums = [5, 15, 35, 8, 98]
##for num_index, num_val in enumerate(nums):
##    print(num_index, num_val)

###21)Write a Python program to convert a list of characters into a string.
##s = ['a', 'b', 'c', 'd']
##str1 = ''.join(s)
##print(str1)

###22) Write a Python program to find the index of an item in a specified list.
##num =[10, 30, 4, -6]
##print(num.index(30))

###23)Write a Python program to flatten a shallow list.
##import itertools
##original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
##new_merged_list = list(itertools.chain(*original_list))
##print(new_merged_list)

###24)Write a Python program to append a list to the second list.
##list1 = [1, 2, 3, 0]
##list2 = ['Red', 'Green', 'Black']
##final_list = list1 + list2
##print(final_list)

###25)Write a Python program to select an item randomly from a list.
##import random
##color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
##print(random.choice(color_list))

###26)Write a python program to check whether two lists are circularly identical.
##list1 = [10, 10, 0, 0, 10]
##list2 = [10, 10, 10, 0, 0]
##list3 = [1, 10, 10, 0, 0]
##
##print('Compare list1 and list2')
##print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
##print('Compare list1 and list3')
##print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

###27)Write a Python program to find the second smallest number in a list.
##list=[2,5,1,3,4,6]
##l1=sorted(list)
##print("SECOND SMALLEST NUMBER IS:",l1[1])

###28)Write a Python program to find the second largest number in a list.
##list=[3,5,13,45,32]
##l1=sorted(list)
##print("SECOND LARGEST NUMBER IS:",l1[-2])

###29)Write a Python program to get unique values from a list.
##list1=[2,4,2,4,5]
##print(list1)
##l1=set(list1)
##l2=list(l1)
##print("UNIQUE LIST:",l2)

###30)Write a Python program to get the frequency of the elements in a list.
##list1=[2,4,2,5,3,4,1]
##list_set=set(list1)
##for i in list_set:
##    print(i,"------>",list1.count(i))
    

###31)Write a Python program to count the number of elements in a list within a specified range. 
##def count_range_in_list(li, min, max):
##	ctr = 0
##	for x in li:
##		if min <= x <= max:
##			ctr += 1
##	return ctr
##
##list1 = [10,20,30,40,40,40,70,80,99]
##print(count_range_in_list(list1, 40, 100))
##
##list2 = ['a','b','c','d','e','f']
##print(count_range_in_list(list2, 'a', 'e'))

###32)Write a Python program to check whether a list contains a sublist.
##def is_Sublist(l, s):
##	sub_set = False
##	if s == []:
##		sub_set = True
##	elif s == l:
##		sub_set = True
##	elif len(s) > len(l):
##		sub_set = False
##
##	else:
##		for i in range(len(l)):
##			if l[i] == s[0]:
##				n = 1
##				while (n < len(s)) and (l[i+n] == s[n]):
##					n += 1
##				
##				if n == len(s):
##					sub_set = True
##
##	return sub_set
##
##a = [2,4,3,5,7]
##b = [2,4,3]
##c = [3,7]
##print(is_Sublist(a, b))
##print(is_Sublist(a, c))

###33)Write a Python program to generate all sublists of a list.
##from itertools import combinations
##def sub_lists(my_list):
##	subs = []
##	for i in range(0, len(my_list)+1):
##	  temp = [list(x) for x in combinations(my_list, i)]
##	  if len(temp)>0:
##	    subs.extend(temp)
##	return subs
##l1=[10,20,30]
##print(sub_lists(l1))

###34)Write a Python program using Sieve of
###Eratosthenes method for computing primes upto a specified number.
###Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους,
###kóskinon Eratosthénous) one of a number of prime number sieves, is a simple,
###ancient algorithm for finding all prime numbers up to any given limit.
##def prime_eratosthenes(n):
##    prime_list = []
##    for i in range(2, n+1):
##        if i not in prime_list:
##            print (i)
##            for j in range(i*i, n+1, i):
##                prime_list.append(j)
##
##print(prime_eratosthenes(100));

###35)Write a Python program to create a list by concatenating a given list which range goes from
###1 to n. 
###Sample list : ['p', 'q']
###n =5
###Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
##my_list = ['p', 'q']
##n = 4
##new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
##print(new_list)

###36) Write a Python program to get variable unique identification number or string.
##x = 100
##print(format(id(x), 'x'))
##s = 'w3resource'
##print(format(id(s), 'x')) 

###37)Write a Python program to find common items from two lists.
##color1 = ["Red", "Green", "Orange", "White"]
##color2 = ["Black", "Green", "White", "Pink"]
##common_Colors=set(color1) & set(color2)
##print(list(common_Colors))


###38) Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
###Sample list: [0,1,2,3,4,5]
###Expected Output: [1, 0, 3, 2, 5, 4]
##def change_pos(my_list):
##    for i in range(0,len(my_list),2):
##        my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
##    return my_list
##
##my_list=[0,1,2,3,4,5]
##
##print(change_pos(my_list))

###39)Write a Python program to convert a list of multiple integers into a single integer. 
###Sample list: [11, 33, 50]
###Expected Output: 113350
##L = [11, 33, 50]
##print("Original List: ",L)
##x = int("".join(map(str, L)))
##print("Single Integer: ",x)


###40)Write a Python program to split a list based on first character of word.
##from itertools import groupby
##from operator import itemgetter
##
##word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
##     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
##
##for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
##    print(letter)
##    for word in words:
##        print(word)

###41)Write a Python program to create multiple lists.
##obj = {}
##for i in range(1, 21):
##    obj[str(i)] = []
##print(obj)

####42)Write a Python program to find missing and additional values in two lists. 
####Sample data : Missing values in second list: b,a,c
####Additional values in second list: g,h
##list1 = ['a','b','c','d','e','f']
##list2 = ['d','e','f','g','h']
##print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
##print('Additional values in second list: ', ','.join(set(list2).difference(list1)))

####43)Write a Python program to split a list into different variables. 
##color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
##         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
##var1, var2, var3 = color
##print(var1)
##print(var2)
##print(var3)

####44)Write a Python program to generate groups of five consecutive numbers in a list.
##l = [[5*i + j for j in range(1,6)] for i in range(5)]
##print(l)

####45)Write a Python program to convert a pair of values into a sorted unique array. 
##L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
## (7, 8), (9, 10)]
##print("Original List: ", L)
##print("Sorted Unique Data:",sorted(set().union(*L)))


####46)Write a Python program to select the odd items of a list.
##l=[1,2,3,4,5,6,7,8]
##for i in l:
##    if i%2!=0:
##        print(i)

####47)Write a Python program to insert an element before each element of a list. 
##color = ['Red', 'Green', 'Black']
##print("Original List: ",color)
##color = [v for i in color for v in ('c', i)]
##print("Original List: ",color)

####48)Write a Python program to print a nested lists (each list on a new line) using the print() function.
##colors = [['Red'], ['Green'], ['Black']]
##print('\n'.join([str(lst) for lst in colors]))

##for i in colors:
##    print(i)

####49)Write a Python program to convert list to list of dictionaries. 
##Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
##Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
##color_name = ["Black", "Red", "Maroon", "Yellow"]
##color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
##print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])


####50)Write a Python program to sort a list of nested dictionaries.
##my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
##print("Original List: ")
##print(my_list)
##my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
##print("Sorted List: ")
##print(my_list)

##from operator import itemgetter   
### Initializing list of dictionaries 
##lis = [{ "name" : "Nandini", "age" : 12},  
##{ "name" : "Manjeet", "age" : 20 }, 
##{ "name" : "Nikhil" , "age" : 19 }] 
### using sorted and itemgetter to print list sorted by age  
##print("The list printed sorting by age:")
##print(sorted(lis, key=itemgetter('age')))

####51)Write a Python program to split a list every Nth element. 
####Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
####Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
##C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
##def splitlist(l1,step):
##    return[l1[i::step] for i in range(step)]
##print(splitlist(C,4))

####52)Write a Python program to compute the similarity between two lists.
##from collections import Counter
##color1 = ["red", "orange", "green", "blue", "white"]
##color2 = ["black", "yellow", "green", "blue"]
##counter1 = Counter(color1)
##counter2 = Counter(color2)
##print("Color1-Color2: ",list(counter1 - counter2))
##print("Color2-Color1: ",list(counter2 - counter1))

##list1 = ["red", "orange", "green", "blue", "white"]
##list2 = ["black", "yellow", "green", "blue"]
##print("Color1-Color2",list(set(list1) - set(list2)))
##print("Color2-Color1",list(set(list2) - set(list1)))

####53)Write a Python program to create a list with infinite elements.
##def infinitenumbers():
##    count = 0
##    while True:
##        print(count)
##        count += 1
##infinitenumbers()

##import itertools
##arithmetic_progression = itertools.count(0,1)
##print(arithmetic_progression)

####54)Write a Python program to concatenate elements of a list.
##l1=['a','b','c','d']
##l2=['e','f','g','h']
##l1=l1+l2
##print(l1)

####55)Write a Python program to remove key values pairs from a list of dictionaries.
##test_list = [{"id" : 1, "data" : "HappY"}, 
##             {"id" : 2, "data" : "BirthDaY"}, 
##             {"id" : 3, "data" : "Rash"}] 
### printing original list  
##print ("The original list is : " + str(test_list)) 
##  # using del + loop  
### to delete dictionary in list 
##for i in range(len(test_list)): 
##    if test_list[i]['id'] == 2: 
##        del test_list[i] 
##        break
### printing result 
##print ("List after deletion of dictionary : " +  str(test_list))

####56)Write a Python program to convert a string to a list.
##s1="hii im mayur"
##s2=s1.split(" ")
##print(list(s2))

##s1="hii im mayur"
##print(list(s1.split(" ")))

####57)Write a Python program to check whether all items of a list is equal to a given string.
##def checklist(l1):
##    ele=l1[0]
##    chk=True
##    for i in l1:
##        if ele!=i:
##            chk=False
##            return chk
##            break
##    return chk
##c=checklist([1,1,1,1])
##if c==True:
##    print("equal")
##else:
##    print("not equal")

####58)Write a Python program to replace the last element in a list with another list.
##l1=[1,2,3,4]
##l2=[8,5,6,7]
##ul1=[list(l1[0:len(l1)-1]) + list(l2)]
##print(ul1)

####59)Write a Python program to check whether the n-th element exists in a given list.
##def check(l1,ele):
##    chk=False
##    for i in l1:
##        if ele==i:
##            return True
##            break
##    return chk
##
##n=int(input("Enter the element: "))
##c=check([1,2,3,4],n)
##if c==True:
##    print("Exists")
##else:
##    print("Not Exists")

####60)Write a Python program to find a tuple, the smallest second index value from a list of tuples.
##t=[(1,2),(3,4),(4,5)]
##res=min(t)[1],max(t)[1]
##print(res)

####61)Write a Python program to create a list of empty dictionaries.
##n=int(input("Enter the number:"))
##res=[{} for i in range(0,n)]
##print(res)

####62)Write a Python program to print a list of space-separated elements.
##n=int(input("Enter the number of elements:"))
##res=[i for i in range(0,n)]
##print(res)

####63)Write a Python program to insert a given string at the beginning of all items in a list. 
##Sample list : [1,2,3,4], string : emp
##Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
##l=[1,2,3,4]
##res=['emp{0}'.format(i) for i in l]
##print(res)

####64)Write a Python program to iterate over two lists simultaneously.
##l1=[1,2,3,4]
##l2=[5,6,7,8]
##for (a,b) in zip(l1,l2):
##    print(a,b)

####65)Write a Python program to access dictionary keys element by index.
##dic={'mayur':40,'rashika':60,'sunil':50}
##print(list(dic)[0])

####66)Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
##Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
##Expected Output: [10, 11, 12]
##l=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
##print(max(l,key=sum))

####67)Write a Python program to find all the values in a list are greater than a specified number.
##l=[3,5,6,7,1,4]
##n=int(input("Enter the number:"))
##for i in l:
##    if i>n:
##        print(i)

####68)Write a Python program to extend a list without append. 
##Sample data: [10, 20, 30]
##[40, 50, 60]
##Expected output : [40, 50, 60, 10, 20, 30]
##l1=[10,20,30]
##l2=[40,50,60]
##l1=l2+l1
##print(l1)

####69)Write a Python program to remove duplicates from a list of lists. 
##Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
##New List : [[10, 20], [30, 56, 25], [33], [40]]
l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(set(l))





















