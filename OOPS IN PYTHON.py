####OOPS
###have two components Properties(color , cost, size) and Behaviour(do work, make call,play games)
### class is a user defined data type
### object are specific instant of class
### CREATING CLASS
##class Phone:  ###Creating the 'Phone' class
##    def make_call(self):
##        print('Making call')
##
##    def play_game(self):
##        print('playing game')
##
##
##
##p1=Phone() ###instantiating the 'p1' object
##p1.make_call() ###Invoking methods through object
##p1.play_game()

##Adding parameters
##class Phone:
##    def set_color(self,color):
##        self.color=color
##    def set_cost(self,cost):
##        self.cost=cost
##    def show_color(self):
##        return self.color
##    def show_cost(self):
##        return self.cost
##    def make_call(self):
##        print('Making phone call')
##    def play_game(self):
##        print('Playing game')
##
##p1=Phone()
##p1.set_cost('100000')
##p1.set_color('Black')
##p1.make_call()
##print(p1.show_color())
##print(p1.show_cost())

######Creating Class with constructor(__init__ method act as constructor)
##class Employee:  ###self is important for instantiating an object
##    def __init__(self,name,age,salary,gender):
##        self.name = name
##        self.age = age
##        self.salary = salary
##        self.gender = gender
##    def employee_details(self):
##        print(f'The name of employeee is {self.name}')
##        print(f'The age of employeee is {self.age}')
##        print(f'The salary of employeee is {self.salary}')
##        print(f'The gender of employeee is {self.gender}')
##
##
##e1 = Employee('Jashan','23','5200', 'Male')
####print(e1.name)
####print(e1.age)
####employee_details(e1) if i def employee_details outside the class then this will show the details
####e1.employee_details() if i def employee_details inside the object then this will show the details


#####INHERITANCE
##class Vehicle:###Parent class
##    def __init__(self,milage,cost):
##        self.milage = milage
##        self.cost = cost
##    def show_d(self):
##        print('i am a Vehicle')
##        print(f'mileage of vehicle is {self.milage}')
##        print(f'Cost of the vehicle is {self.cost}')
##class car(Vehicle): ##creating the child class
##    def show_car(self):
##        print('i am a car')
##
##v1= Vehicle(500,5000) ##initating the object from the base class
##v1.show_d()
##c1 = car(300,40000) ##instantiating the object for child class
##c1.show_d()
##c1.show_car() ##Invoking the child class method

####OVER_RIDING INIT method
class Vehicle:###Parent class
    def __init__(self,milage,cost):
        self.milage = milage
        self.cost = cost
    def show_d(self):
        print('i am a Vehicle')
        print(f'mileage of vehicle is {self.milage}')
        print(f'Cost of the vehicle is {self.cost}')
class Car(Vehicle):
    def __init__(self,milage,cost,tyres,hp):
        super().__init__(milage,cost)  ###super(). is overriding the method
        self.tyres = tyres
        self.hp = hp
    def show_c_d(self):
        print('I am the car')
        print(f'Number of tyres are {self.tyres}')
        print(f'value of horse power is {self.hp}')
c1 = Car(200,200000,4,30)
c1.show_d()
print('Hello')
c1.show_c_d()
#####Their are 4 types of inheritance - multiple inheritance, multilevel inheritance,





















