####1)Python program to Swap Keys and Values in Dictionary.
##dict1={1:"mayur",2:"rashu",3:"priyu",4:"sunil"}
##dict2=dict([(value,key) for key,value in dict1.items()])
##print(dict2)

####2)Write program to implement Selection sort.
##list1=[5,2,3,1,0]
##print("Unsoreted list",list1)
##for i in range(len(list1)):
##    min_val=min(list1[i:])
##    min_index=list1.index(min_val)
##    list1[i],list1[min_index]=list1[min_index],list1[i]
##print("soreted list",list1)

####3)Write program to implement Insertion sort.
##def InsertionSort(my_list):
##    for index in range(1,len(my_list)):
##        current_element=my_list[index]
##        pos=index
##        while current_element < my_list[pos-1] and pos>0:
##            my_list[pos]=my_list[pos-1]
##            pos=pos-1
##        my_list[pos]=current_element
##my_list=[5,1,2,3,4]
##InsertionSort(my_list)
##print(my_list)


####4)Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
####Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
####Sub List to be added = ["h", "i", "j"]
####Expected output:-
####['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
##list1[2][1][2].extend(["h","i","j"])
##print(list1)


####5)Access the value of key “history”
####sampleDict = { 
####   "class":{ 
####      "student":{ 
####         "name":"Mike",
####         "marks":{ 
####            "physics":70,
####            "history":80
####         }
####      }
####   }
####}
####Expected output: 80
sampleDict = { "class":{ "student":{ "name":"Mike","marks":{ "physics":70,"history":80}}}}
print(sampleDict['class']['student']['marks']['history'])
