##What is numpy?
##-->Numpy is a module in python.as python is a general purpose language because it is application based programming language like
##others.Due to the numpy,scipy,pandas python is special because it can store process the data in one dimension two dimenion multi
##dimension i.e. it is used for data analysis and also used by machine learning algorithms AI algo becuase of these modules
##.As we processes data in one,two and multi dimensional.this can be achieved as array but array is the static i.e. the size is fixed
##and python is the dynamic programming language it contains dynamic data structure like set,list..so to achieve arrays concept in
##python numpy module is used for storing and processing the one,two and multiple dimension effectively.
##   It stands for numerical python and it is developed by jim hugunin.It is used for
##  Mathematical and logical operations on arrays.
##• Fourier transforms and routines for shape manipulation.
##• Operations related to linear algebra. NumPy has in-built functions for
##linear algebra and random number generation.

import numpy as np
##my_list=[1,2,3,4,5]
##arr=np.array(my_list)
##print(arr)
   
####how to get the properties of array.
##l1=[10,20,30,40,50]
##arr=np.array(l1)
##print("array:",arr)
##print("Size :",arr.size)          #arr.size is not the object it is the dynamic variables of numpy which is applied on object i.e
##print("Datatype:",arr.dtype)      #attributes.
##print("Dimension:",arr.ndim)
##print("Shape:",arr.shape)

##l1=[[10,20,30],[40,50,60],[70,80,90]]
##matrix=np.array(l1)
##print("array:",matrix)
##print("Size :",matrix.size)       #arr.size is not the object it is the dynamic variables of numpy which is applied on object i.e
##print("Datatype:",matrix.dtype)   #attributes.
##print("Dimension:",matrix.ndim)
##print("Shape:",matrix.shape)

####Printing all elements in one dimensional array
##l1=[10,20,30,40,50]
##arr=np.array(l1)
##print("Elements:")
##for ele in arr:
##    print(ele)
##print(arr)


##l1=[[10,20,30],[40,50,70],[60,70,80]]
##matrix=np.array(l1)
##print(matrix)
##print()                            #for printing all elements in the matrix it will show in the orm of two dimensional array.
##print("Elements:")                 #printing matrix in the form of each row
##for row in matrix:                
##    print(row)
##print()
##print("Elements:")                 #printing element by element from matrix
##for row in matrix:
##    for ele in row:
##        print(ele)
##print("Elements:")                 #printing proper 2 dimensional matrix
##for row in matrix:
##    for ele in row:
##        print(ele,end=' ')
##    print()

####################################sub matrix from matrix using slicing###########################################3
#Indexing means to process the elements one by one and slicing means within the given bound we can get the elements.
##l1=[[10,20,30],[40,50,70],[60,70,80]]
##matrix=np.array(l1)
##print(matrix)      
##print()
##res=matrix[ : , : ]             #[row_low:row_upp,col_low:col_upp]
##print(res)
##print()
##res=matrix[0:3,0:3]
##print(res)
##print()
##res=matrix[0:2,0:3]
##print(res)
##print()
##res=matrix[0:3,0:2]
##print(res)
##print()
##res=matrix[1:3,1:3]
##print(res)
##print()

####################################################creating one dimensional array#####################################3
#Enter the size of elements enter the elements and print it in the form of matrix.
##n=int(input("Enter the size:"))
##arr=np.ndarray(shape=(n),dtype=int)
##print("Enter %d elements:" %n)
##for i in range(n):
##    arr[i]=int(input())
##print("Array:",arr)

####If we dont specify dtype as int then it will by defauld has float type
##n=int(input("Enter the size:"))
##arr=np.ndarray(shape=(n))
##print("Enter %d elements:" %n)
##for i in range(n):
##    arr[i]=input()
##print("Array:",arr)

##########################################3creating two dimensional array###########################################
##n=int(input("Enter the rows size:"))
##m=int(input("Enter the columns size:"))
##matrix=np.ndarray(shape=(n,m),dtype=int)
##print("size:",matrix.size)
##print("dimension:",matrix.ndim)
##print("shape:",matrix.shape)
##print("Enter the %d elements in %dx%d matrix:" %(n*m,n,m))
##for i in range(n):
##    for j in range(m):
##        matrix[i][j]=int(input())
##print("matrix %dx%d is:" %(n,m))
##print(matrix)


#######################################Creating multidimensional array#############################################
##arr=np.ndarray(shape=(3,3,3),dtype=int)
##x=arr.shape[0]
##y=arr.shape[1]  
##z=arr.shape[2]
##var=1
##for i in range(x):
##    for j in range(y):
##        for k in range(z):
##            arr[i][j][k]=var
##            var=var+1
##print(arr)
            
####################################RESHAPE function##############################################################
##arr=np.array([10,20,30,40,50,60])
##print(arr)
##print()
##res=arr.reshape(2,3)
##print(res)

##arr=np.array([10,20,30,40,50,60,70,80])
##print(arr)
##print()
##res=arr.reshape(2,2,2)
##print(res)

################################ARANGE function##############################################################
##arr=np.arange(1,10)
##print(arr)
##
##arr1=np.arange(1,10,2)
##print(arr1)
##
##arr1=np.arange(1,10,1)
##print(arr1)
##
##arr1=np.arange(0,10,2)
##print(arr1)
##
##arr1=np.arange(1,10)
##res=arr1.reshape(3,3)
##print(res)


##############################ADDITION,SUBSTRACTION,MULTIPLICATION,DIVISION OF ARRAY###########################
##a=np.array([1,2,3,4])
##b=np.array([1,2,3,4])
##c=a+b
##d=a*b
##e=a-b
##f=a/b
##g=a//b
##print("1st array:")
##print(a)
##print("2nd array:")
##print(b)
##print("Addition:")
##print(c)
##print("multiplication:")
##print(d)
##print("substraction:")
##print(e)
##print("division:")
##print(f)


##############################CONCATENATE FUNCTION############################################################
##a=np.array([1,2,3,4])
##b=np.array([5,6,7,8])
##c=np.concatenate([a,b])
##d=np.concatenate([b,a])
##e=np.concatenate([a,c])
##print(c)
##print(d)
##print(e)

##a=np.array([1,2,3,4])
##b=np.array([5,6,7,8])
##c=np.vstack([a,b])
##print(c)


#############################ZEROS FUNCTION###################################################################
##help(np.zeros)
##arr=np.zeros(5)
##print(arr)

##arr=np.zeros((5,3),dtype=int)        #we can also take [5,3]
##print(arr)

############################ONES FUNCTION#####################################################################
##help(np.ones)
##arr=np.ones(5)
##print(arr)

##arr=np.ones((5,2),dtype=int)
##print(arr)

###########################LINSPACE FUNCTION#################################################################
##Linspace and arange function both include start and end points but the difference is arange function gives the
##difference in two values by specifying range.Linspace gives the number of values between the intervals.
##in Linspace if we dont mention the 'num' value it is by default 50.
##a=np.linspace(1,100,num=5)
##print(a)

##a=np.linspace(1,100,num=5,endpoint=False)      #it will exclude the endpoint from array and display 5 values
##print(a)

##a=np.linspace(1,100,num=5,dtype=int)            #printing integer value
##print(a)

##a=np.linspace(1,5)                             #by default it will take num=50.
##print(a)


#########################EYE FUNCTION########################################################################
##returns array filled with zeros except in the nth-diagonal,whose values are equal to one.
##by default k=0 where k is then kth diagonal of the martix
##a=np.eye(4)
##print(a)
##
##a=np.eye(4,2)
##print(a)
##
##a=np.eye(4,k=1)
##print(a)
##
##a=np.eye(4,4,k=-1)
##print(a)
##
##a=np.eye(4,dtype=int)
##print(a)
##
##a=np.identity(4,dtype=int)                    #same as eye function but limited parameters havin only np.identity(n,dtype)
##print(a)




#######################################PANDAS RANDOM MODULE##################################################
##returns a set of random values to the array
##rand-uniformly distributed values.
##randn-normally distributed values.
##ranf-uniformly distributed floating point numbers.
##randint-uniformly distributed intyegers in a given range.

##a=np.random.rand(5)
##print(a)

##a=np.random.rand(5,4)
##print(a)

##a=np.random.randn(5)
##print(a)

##a=np.random.ranf(4)
##print(a)

##a=np.random.randint(3,size=10)
##print(a)


#######################################PANDAS LINEAR ALGEBRA MODULE(linalg)##################################
####using all functions compulsary square matrix is needed otherwise error.
####calculate inverse of matrix
##a=np.array([[10,20],[50,60]])
##res=np.linalg.inv(a)                #compulsary it should be square matrix otherwise it will throw error.
##print(res)

####calculate power of matrix 
##a=np.array([[10,20],[50,60]])       #(a,n)--->where a is matrix and n is the power to ne taken
##res=np.linalg.matrix_power(a,2)     #if n=0--->we will get identity matrix
##print(res)                          #if n>0---->power is taken directly to compute and n<0--->matrix is inverse internally then
                                    #it will compute with the negative power.

####solve linear equations.
##a=np.array([[10,20],[30,40]])          #solving equations as  lets say 10x+20y=4 and 30x+40y=5
##b=([4,5])                              #then we get x=-0.3 and y=0.35 as output.
##res=np.linalg.solve(a,b)
##print(res)

####Find determinant of matrix.
##a=np.array([[10,20],[30,40]])
##res=np.linalg.det(a)
##print(round(res))













