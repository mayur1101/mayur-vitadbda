'''
import matplotlib.pyplot as plt 

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Wow! We Got Our First Bar Graph')
plt.show()

'''

import pandas as pd 
import matplotlib.pyplot as plt 
  
# create 2D array of table given above 
data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
  
# dataframe created with 
# the above data array 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'] ) 
'''  
# create histogram for numeric data 
df.hist() 
'''

'''
df.plot.bar() 
# show plot 
plt.show() 
'''

'''  
# plot between 2 attributes 
plt.bar(df['Age'], df['Sales'],color='g') 
plt.xlabel("Age") 
plt.ylabel("Sales") 
plt.show()
'''

'''
# For each numeric attribute of dataframe 
df.plot.box()
plt.show()
'''

'''
# individual attribute box plot 
plt.boxplot(df['Income']) 
plt.show()
'''

'''
plt.pie(df['Age'], labels = {"A", "B", "C", 
                             "D", "E", "F", 
                             "G", "H", "I", "J"}, 
                               
autopct ='% 1.1f %%', shadow = True) 
plt.show() 
'''

'''
plt.pie(df['Income'], labels = {"A", "B", "C", 
                                "D", "E", "F", 
                                "G", "H", "I", "J"}, 
                                  
autopct ='% 1.1f %%', shadow = True) 
plt.show() 
'''  

'''
plt.pie(df['Sales'], labels = {"A", "B", "C", 
                               "D", "E", "F", 
                               "G", "H", "I", "J"}, 
autopct ='% 1.1f %%', shadow = True) 
plt.show() 
'''

'''
plt.scatter(df['Income'], df['Age']) 
plt.show()
'''

'''
# scatter plot between income and sales 
plt.scatter(df['Income'], df['Sales']) 
plt.show() 
'''

'''
# scatter plot between sales and age 
plt.scatter(df['Sales'], df['Age']) 
plt.show() 
'''


