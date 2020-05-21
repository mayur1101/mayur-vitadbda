#1.Write a Python program to create a set
'''
x={}
print(x)
a={1,3,4,0}
print(a)

'''

#2.Write a Python program to iteration over sets.
'''
z={1,2,9,7,4}
for i in z:
    print(i)
'''

#3.Write a Python program to add member(s) in a set.
'''
x={'a','b','c'}
x.add('s')
print(x)
x={0,1,2,3}
x.add(4)
print(x)
'''

#4.Write a Python program to remove item(s) from set
#pop removes last elemt from the set.
'''
x={'a','b','c','d','s'}
x.pop()
print(x)

'''
#5.Write a Python program to remove an item from a set if it is present in the set.
'''
x={'a','b','c','d','s'}
x.remove('b')
print(x)
or
x={'a','b','c','d','s'}
x.discard('b')
print(x)
'''

#6.Write a Python program to create an intersection of sets.
'''
setA={"red","green","blue"}
setB={"green","blue","pink"}
setC=setA & setB
print(setC)

or

setA={"red","green","blue"}
setB={"green","blue","pink"}
setC=setA.intersection(setB)
print(setC)
'''

#7.Write a Python program to create a union of sets.
'''
setx={0,1,2,3,4,5}
sety={9,3,0,1,7,3}
setc=setx.union(sety)
print(setc)

or

setx={0,1,2,3,4,5}
sety={9,3,0,1,7,3}
setc=setx | (sety)
print(setc)
'''

#8.Write a Python program to create set difference.
'''
setA={10,20,30,40,50}
setB={20,30,70,80,100}
setC=setA - setB
print(setC)

or

setA={10,20,30,40,50}
setB={20,30,70,80,100}
setC=setA.difference(setB)
print(setC)

#when A-B then ans is diff. & when B-A then ans is diff:
setA={10,20,30,40,50}
setB={20,30,70,80,100}
setC=setB - setA
print(setC)
'''

#9.Write a Python program to create a symmetric difference.
'''
setX={"R","A","S","H","U"}
setY={"M","A","Y","U","R"}
setZ=setX.symmetric_difference(setY)
print(setZ)

or

setX={"R","A","S","H","U"}
setY={"M","A","Y","U","R"}
setZ=setX ^ setY
print(setZ)
'''

#10.Write a Python program to issubset and issuperset
# For Superset:
'''
A={1,2,3,4,5}
B={2,3}
print(A.issuperset(B))

A={1,2,3,4,5}
B={2,3}
print(B.issuperset(A))
'''
'''
#For Subset:
A={1,2,3,4,5}
B={2,3}
print(B.issubset(A))

A={1,2,3,4,5}
B={2,3}
print(A.issubset(B))
'''

#11.Write a Python program to create a shallow copy of sets.
'''
import copy
setx={"red","green"}
sety=copy.copy(setx)
print(setx)
print(sety)
'''

#12.Write a Python program to clear a set.
'''
setx={'a','b','c','d','s'}
setx.clear()
print(setx)
'''

#13.Write a Python program to use of frozensets.
'''
A={1,2,3,4,5}
B=frozenset(A)
print(B)

A={"Name":"mayur",Age":24,"Salary":40000}
B=frozenset(A)
print(B)
'''

#14.Write a Python program to find maximum and the minimum value in a set
'''
setA={11,22,33,44,55}
print(min(setA))
print(max(setA))
'''

#15.Write a Python program to find the length of a set.
'''
setx={21,22,30,39,11,99}
print(len(setx))
'''





























