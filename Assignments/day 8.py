####1.Write a program to implement Constructor with Variable Number of Arguments.
##class Demo:
##    def __init__(self,name,list1):
##        print(name)
##        print(list1)
##
##name=input("Enter the name")
##list1=[1,2,3,4]
##obj=Demo(name,list1)


####Q.2.Create a menu driven program for library management. It will include 6 options :-
####    1 - student registration
####    2 - lend book to student
####    3 - return book to library
####    4 - display available books
####    5 - display all books issued to students
####    6 - exit
####We will have 2 classes, i.e student and library. These class will have following mandatory methods. 
####Student class will have methods registration, requestBook and returnBook
####Library class will have methods displayAllBooks, lendBook,addNewBook
####(If required, you can write additional methods as well.)
##import sys
##class Library:
##    issued_books=[]
##    def __init__(self,TotalBooks):
##        self.TotalBooks=TotalBooks
##        
##    def displayAllBooks(self):
##        n=1
##        print("All books are----->")
##        if self.TotalBooks !=[]:
##            for i in self.TotalBooks:
##                print(n,".",i)
##                n+=1
##        else:
##            print("All books are issued")
##
##    def issuedBooks(self):
##        n=1
##        for i in Library.issued_books:
##            print(n,".",i)
##            
##    def lendBook(self):
##        lbook=input("Enter the book name:")
##        if lbook not in self.TotalBooks and self.TotalBooks==[]:
##            print("All books are issued.Sry u cant lend book")
##        else:
##            Library.issued_books.append(lbook)
##            self.TotalBooks.remove(lbook)
##
##    def addNewBook(self):
##        abook=input("Enter the book name:")
##        self.TotalBooks.append(abook)
##
##class Student(Library):
##    def __init__(self,students):
##        self.students=students
##        
##    def registration(self):
##        self.name=input("Enter the name:")
##        if self.name not in self.students:
##            self.students.append(self.name)
##        else:
##            print("This name already exists")
##
##    def removeRegistration(self):
##        self.name=input("Enter the name:")
##        if self.name in self.students:
##            self.students.remove(self.name)
##        else:
##            print("This name is not there in the registry")
##
##    def requestBook(self):
##        self.registration()
##        rbook=input("Enter the book name:")
##        if rbook in self.TotalBooks:
##            print(rbook,"can be issued")
##        else:
##            print(rbook,"cannot be issued")
##
##    def returnBook(self):
##        self.regstration()
##        rbook=input("Enter the book name:")
##        if rbook in Library.issued_books():
##            rbook.self.TotalBooks.append(rbook)
##            rbook.Library.issued_books.remove(rbook)
##        else:
##            print("This book is not issued to any one or it is invalid book")
##
##    def studentInfo(self):
##        n=1
##        for i in self.students:
##            print(n,".",i)
##            n+=1
##        
##
##        
##allbooks=["Pirates of Carabeean","Harry Potter","The 5a.m. Club"]
##list_of_registered_students=["mayur","rashika","priyanka","sunil","ujwala"]
##lib=Library(allbooks)
##stu=Student(list_of_registered_students)
##c="Yes"
##while c=="Yes":
##    print("--------------Choose the option u want to perform--------------")
##    print("1.Registration\n2.Display All Books\n3.Lend Book\n4.Add new Book\n5.Request Book\n6.Return Book\n7.Student Information\n8.Remove Registration\n9.Issued Books\n10.Exit")
##    print()
##    n=int(input("Choose the number:"))
##    if n==1:
##        stu.registration()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==2:
##        lib.displayAllBooks()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==3:
##        lib.lendBook()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==4:
##        lib.addNewBook()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==5:
##        stu.requestBook()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==6:
##        stu.returnBook()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==7:
##        stu.studentInfo()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==8:
##        stu.removeRegistration()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==9:
##        lib.issuedBooks()
##        print()
##        c=input("Do you want to continue type Yes or No:")
##    elif n==10:
##        print("Thanks for using library")
##        sys.exit()
##    else:
##        print("Choose the correct option")
##        c=input("Do you want to continue type Yes or No:")
        
####3)Write a program to implement multiple inheritance.
##class Demo1:
##    def test1(self):
##        self.name="Mayur"
##        print("This is Demo1 with test1 function")
##        print(self.name)
##
##class Demo2:
##    def test2(self):
##        self.name="Rashika"
##        print("This is class Demo2 with Test2 function")
##        print(self.name)
##
##    def test1(self):
##        self.name="Mayur"
##        print("This is Demo2 with test1 function")
##        print(self.name)
##
##
##
##class Demo3(Demo2,Demo1):
##    def test3(self):
##        self.name="Sunil"
##        print("This is class Demo3 with Test3 function")
##        print(self.name)
##
##obj=Demo3()
##obj.test1()


####4)Write a program to implement operator overloading in python.
##class A:
##    def __init__(self, a):
##        self.a = a 
##  
##    def __add__(self, other): 
##        return self.a + other.a  
##ob1 = A(11) 
##ob2 = A(22) 
##ob3 = A("mayur") 
##ob4 = A("chaudhari") 
##print(ob1 + ob2) 
##print(ob3 + ob4) 




####5)Write a Python program to square and cube every number in a given list of integers using Lambda. 
##def square(list1):
##    print(list1)
##    l=list(map(lambda x:x*x,list1))
##    print(l)
##
##def cube(list1):
##    print(list1)
##    l=list(map(lambda x:x**3,list1))
##    print(l)
##    
##list1=[1,2,3,4,5]
##square(list1)
##print()
##cube(list1)

    
    


