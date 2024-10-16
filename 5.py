# ####Static methods###

# class Math:
#     def __init__(self,num):
#         self.num = num
    
#     def addtonum(self,n):
#         self.num = self.num + n


#     @staticmethod
#     def add(a,b):
#         return a+b



# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

#########instance variable vs class variable########

# class Employee:
#     noofEmployees = 0
#     def __init__(self, name, company, country):
#         self.name = name
#         self.raise_amount = '0.2%'
#         self.company = company
#         self.country = country
#         Employee.noofEmployees +=1
#     def showDetails(self):
#         print(f"The name of employee is {self.name}")
#         print(f"The raise amount is {self.raise_amount}")
#         print(f'Company name is {self.company}')
#         print(f'Country name is {self.country}')
#         print(f'Size of company is {self.noofEmployees}')


# emp1 = Employee('Harry','TATA','India')
# emp1.showDetails()
# Employee.showDetails(emp1)
# emp2 = Employee('Rohan','Apple','USA')
# emp2.raise_amount = '0.5%'
# emp2.showDetails()


# ###########class methods used to make custom data type
# class Employee:
#     company = 'Apple'
#     def show(self):
#         print(f'the name is {self.name} and company is {self.company}')
#     #@classmethod            ##### by using class method it get 1st instant as class otherwise it get it as a argumet
#     def changeCompany(cls, newCompany):  #cls can be change to anything but you have to change it in all code 
#         cls.company = newCompany
    
# e1 = Employee()
# e1.name = 'JASHAN'
# e1.show()
# e1.changeCompany('RNJ') ## it only change for defined person not for all
# e1.show()
# print(Employee.company) 

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary

#     @classmethod
#     def fromStr(cls, string):
#         return cls(string.split('-')[0],string.split('-')[1]) ##here me made a class method to split it
# e = Employee('Harry', 14000)
# print(e.name)
# print(e.salary)

# string = 'Jashan-12000'
# e2 = Employee(string.split('-')[0],string.split('-')[1]) ##split to convert string into a list
# print(e2.name)
# print(e2.salary)

# string2 = 'Vijay-13500'
# e3= Employee.fromStr(string2)
# print(e3.name)
# print(e3.salary)

# e4 = Employee.fromStr('John-14000')
# print(e4.name, e4.salary)

# #######_dic_,dir_,help_ methods
# #dir - this function returns a list of all the attributes and methods 
# x = (0,1,2)
# print(dir(x)) #######dir() returns a list of all attributes and methods (including dender methods)
# print(x.__add__)
# print(x.__dir__)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person('Jonh',35)
# print(p.__dict__) ####dict returns a dictionary representation of an object's attributes
# print(help(Person)) ###used to get help documentation for the object, including a description of its attribute and methods

# ####Super keywords####
# ####
# class ParentClass:
#     def parent_method(self):
#         print('This is the parent method.')

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print('Jashan K')
#     def child_method(self):
#         print('This is the child method.')
#         super().parent_method()   #######super(). 

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class Programmer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name,salary)
#         self.language = language

# rohan = Employee('Rohan',12000)
# sachin = Programmer('Sachin',15000,'Python')
# print(rohan.name, rohan.salary)
# print(sachin.name, sachin.salary, sachin.language)

# #####Dunder methods#####
# class Employee:
#     def __init__(self, name):
#         self.name = name
        
#     def __len__(self):
#         return len(self.name)
#     def __str__(self):
#         return (f'The name of employee is {self.name} str')

#     def __repr__(self):
#         return(f'The name is employee is {self.name} repr')

#     def __call__(self):
#         return(f'Hey i am good')

# e = Employee('Jashan')
# print(e.name)
# print(len(e.name))
# print(str(e))
# print(repr(e))
# # print(call(e))
# e( )



# '''
# __init__: Initializes an instance of a class.
# __str__: Returns a string representation of an object.
# __repr__: Returns a string representation of an object that is unambiguous.
# __len__: Returns the length of an object.
# __add__, __sub__, __mul__, __truediv__, etc.: Implement arithmetic operations for objects.
# __eq__, __ne__, __lt__, __gt__, __le__, __ge__: Implement comparison operations for objects.'''

# ####Method overriding#### agr ek pasand nhi aya toh super class lga do so that u can get right answer

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius,radius)


#     def area(self):
#         return 3.14* super().area()### here we use super area as method overrid

#     # def area(self):
#     #     return 3.14*self.radius*self.radius

# rec = Shape(3,5)
# print(rec.area())
# cir = Circle(10)
# print(cir.area())

# ####Operator Overloading####

# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f'{self.i}i + {self.j}j + {self.k}k'

#     # def __add__(self, x):          ###here we have to create an add operation beacuse python does not directy add two vector into there respective component 
#     #     return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
#     # This will give string as answer

#     def __add__(self, x):
#         return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
#     # This will give vector as answer


# v1 = Vector(2,3,4)
# print(v1)
# v2 = Vector(5,6,7)
# print(v2)
# print(v1+v2)
# print(type(v1+v2))

# #########Single inhertance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print('Generic sound')

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species='Dog')
#         self.breed = breed
    
#     def make_sound(self):
#         print('Bark!!')

# class Cat(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species='Cat')
#         self.breed = breed
    
#     def make_sound(self):
#         print('Meow!!')

# d = Dog('Dog','Doggerman')
# d.make_sound()
# c = Cat('Cat',"felcon")
# c.make_sound()
# print(d.name, d.breed, d.species)
# print(c.name, c.breed, c.species)
# a = Animal("Cat",'cat')
# a.make_sound()
# a = Animal("Dog","dog")
# a.make_sound()

# #####Multiple Inheritance ###
# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f'the name is {self.name}')


# class Dancer:
#     def __init__(self, dance):
#         self.dance
#     def show(self):
#         print(f'The dance is {self.dance}')


# class DancerEmployee(Dancer,Employee):
#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name


# o = DancerEmployee('Bhangra',"Jaspreet")
# print(o.name)
# print(o.dance)
# o.show()
# print(DancerEmployee.mro()) #mro is method resolution order-how the code serch (in order) for certain thing in different class 

#####Multilevel Inhertitance###
# class BaseClass:
# class DerivedClass1(BaseClass):
# class DerivedClass2(DerivedClass1):

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def show_details(self):
#         print(f'The name is {self.name} and the species is {self.species}')

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species='Dog')
#         self.breed = breed
    
#     def show_details(self):
#         Animal.show_details(self)
#         print(f'The breed is {self.breed}')

# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name,breed='Golden Retriever')
#         self.color = color

#     def show_details(self):
#         Dog.show_details(self)
#         print(f'The color is {self.color}')

# # o = GoldenRetriever('Tommy','Black') ##Print 3 lines
# o = Dog('Tommy','black')  ##Print 2 lins

# o.show_details()

# ##########Hybrid and Hierarchical Inhertance in python######
# ###Hybrid Inheritance- is a combination of multiple inhertance:
# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(Derived1, Derived2):
#     pass

# ####Hierarchical ineritance- where multiple subclasses are inherited from single base class
# class BaseClass():
#     pass
# class d1(BaseClass):
#     pass
# class d2(BaseClass):
#     pass

# class d3(d2):
#     pass












































