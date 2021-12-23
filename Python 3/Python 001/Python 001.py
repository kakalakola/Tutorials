#Python 3 - Tutorial 001
#Variables, and the "Print()" function
#By: Saad Azim
#Last Edit: 2021.12.23
#Released under GNU GPL 3.0

#This is a single-line comment. Python ignores these when running the code.
#It's used throughout the code to note things.

"""
    This is a multi-line comment. It's generally used for large blocks of text.

    Multi-line comments will not be frequeltly used in these tutorials.

"""

#The humble print function
print('Hello world!')

#A variable
name='Dave'
age=42

#Commas are used to join segments together with a " "
print('Hello',name) #Prints "Hello dave"
print('Hello',name,'age',age)           #Prints "Hello dave age 42"

#"+" can be used to join segments together
print('Hello '+name+', age:',age)       #Prints "Hello dave, age: 42"
                                        #**Note the extra space at the end of 'Hello '

#print('Hello '+name+', age: '+age)      #Prints an error message
#Strings like 'Dave' and integers/numbers like 42 can't be joined as is

print('Hello '+name+', age: '+str(age)) #Prints "Hello dave, age: 42"


#More variables and types
myStr='String'
myInt=42
myFloat=42.0
myList=['Apples','Oranges',9001]

#Printing variable types
print(type(myStr))                      #Prints "<class 'str'>"
#print('MyStr: '+type(myStr))            #Prints an error message

print('MyStr: '+str(type(myStr)))       #Prints "MyString: <class 'str'>"
print('myInteger: '+str(type(myInt)))
print('myFloat: '+str(type(myFloat)))
print('myList: '+str(type(myList)))
