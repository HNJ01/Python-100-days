###########Map,filter and reduce in python#############map is used to apply a function to each item in an iterable
# def cube(x):
#     return x*x*x
# print(cube(2))
# l = [1,2,3,4,5,6,]
# newl = list(map(cube,l))
# print(newl)

######filter is used to filter out all the items in an iterable for which the function returns true
# l = [1,2,3,4,5,6,7,8,9]
# def filter_function(a):
#     return a>4
# newl = filter(filter_function,l)
# print(list(newl))

# ############REDUCE is used to apply a function cumulatively on all the items of an iterable
# from functools import reduce
# def mysum(x,y):
#     return x+y
# l = [1,2,3,4,5,6,7,8,9]
# sum = reduce(lambda x,y:x+y,l)
# print(sum)
# sum = reduce(mysum,l)
# print(sum)

#####  is vs == (comparison value)
# a = 4
# b = '4'
# print(a==b) #value
# print(a is int(b)) #compare exact location of object in memory

# c =[23,45,67]
# d =[23,45,67]
# print(c == d)
# print(c is d)

# f = 12
# g = 12
# print(f is g)
# print(f==g)

# ########OOPS--Object Oriented Programming################
# #####Class or objects##
# class Person:
#     name = 'Jashan'
#     age = 21
#     networth = 100
#     #self is an object pointer that points to the current instance of class. It is used to access the attributes and methods of the class.
#     def info(self):
#         print(f'{self.name} is {self.age} years old and has {self.networth} networth')

# a = Person()
# # a.name = 'Sam'
# a.age = 20
# a.info()

# b=Person()
# b.name='Akash'
# b.age=21
# b.info()

# #constructor in oops
# #constructor is a special method in python that is called when an object is created from a class. It is used to initialize the attributes of the object.
# class Person:
#     def __init__(self, name, age, networth):
#         self.name = name
#         self.age = age
#         self.networth = networth

# person1 = Person('John', 25, 1000)
# print(person1.name)
# #accessing attributes using dot operator (.)
# print(person1.age)
# # #accessing attributes using dict
# # print(person1['age'])
# # #accessing attributes using get
# # print(person1.get('age'))
# # #accessing attributes using dict
# # print(person1['networth'])

# def hello():
#     print('Hello')

# hello()

# def shout(text):
#     return text.upper()

# print(shout('Hello'))

# yell = shout
# print(yell('Hello'))

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am""")
#     print (greeting)

# greet(shout)
# greet(whisper)
# def greet(fx):
#     def mfx():
#         print('Good morning')
#         fx()
#         print('thanks for using this function')
#     return mfx


# @greet  ##@greet is used as decroter it just little bit modify the function
# def hello():
#     print('Hello')
# #@greet
# def add(a,b):
#     print(a+b)

# hello()
# add(9,10)

# #########Getters and Setters###
# class MyClass:
#     def __init__(self,value):
#         self._value = value

#     def show(self):
#         print(self._value)

#     @property
#     def ten_value(self):
#         return 10*self._value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10


# obj = MyClass(10)
# obj.ten_value = 67
# obj.show() ## 1st output
# print(obj.ten_value) 

# #Inheritance : When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id 

#   def showDetails(self):
#     print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee): #sub class of employee
#   def showLanguage(self):
#     print("The default langauge is Python")

# class python(Programmer): #sub class of programmer
#   def showfiletype(self):
#     print('The file type is python')

# e1 = Employee("Rohan Das", 400)
# e1.showDetails()
# e2 = Programmer("Harry", 4100)
# e2 = python("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()
# e2.showfiletype()


"""Access Specifiers/Modifiers{0/100}
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers
Public access modifier
Private access modifier
Protected access modifier

Public Access Specifier in Python
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

Private Access Specifier
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

Protected Access Specifier
In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.
"""
# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "JAshan"
# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())

# #####SNAKE WATER GUN####
# import random

# def check(comp, user):
# #in this case both tie
#     if comp == user:
#         return 0
# #in all the below cases you will loss else in return 1 u win
#     if(comp== 0 and user ==1):
#         return -1

#     if(comp== 1 and user ==2):
#         return -1

#     if(comp== 2 and user ==0):
#         return -1

#     return 1 ###in this case you will win

# comp=random.randint(0,2)
# user = int(input('0 for snake,1 for water, 2 for gun '))
# if(user <= 2 and user >=0): # so that no one enter value more than 2
#     pass
# else:
#     print('Enter valid input')
#     exit()


# score=check(comp,user)

# print('YOU: ',user)
# print('Computer: ', comp)

# if (score == 0):
#     print('Its a draw')

# if(score == -1):
#     print('YOU LOSE')

# if(score == 1):
#     print('YOU WIN')


# import random

# def check(comp, user):
#     # ... (same as before)

#     def play_round():
#         comp = random.randint(0, 2)
#         user = int(input('0 for snake, 1 for water, 2 for gun: '))
#         if user <= 2 and user >= 0:
#             pass
#         else:
#             print('Enter valid input')
#             return False

#     score = check(comp, user)

#     print('YOU:', user)
#     print('Computer:', comp)

#     if score == 0:
#         print('It\'s a draw')
#     elif score == -1:
#         print('YOU LOSE')
#     elif score == 1:
#         print('YOU WIN')

#     return True

# # Main game loop
#     for _ in range(3):
#         if not play_round():
#             break

############ 3 round of above game####
# import random

# def check(comp, user):
#     if comp == user:
#         return 0
#     if comp == 0 and user == 1:
#         return -1
#     if comp == 1 and user == 2:
#         return -1
#     if comp == 2 and user == 0:
#         return -1
#     return 1

# def play_round():
#     comp = random.randint(0, 2)
#     user = int(input('0 for snake, 1 for water, 2 for gun: '))
#     if user <= 2 and user >= 0:
#         pass
#     else:
#         print('Enter valid input')
#         return False

#     score = check(comp, user)

#     print('YOU:', user)
#     print('Computer:', comp)

#     if score == 0:
#         print('It\'s a draw')
#     elif score == -1:
#         print('YOU LOSE')
#     elif score == 1:
#         print('YOU WIN')

#     return True

# # Main game loop
# for _ in range(3):
#     if not play_round():
#         break



