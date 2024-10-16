# def average (*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print('Average is', sum/len(numbers))

# average (5,6,4)

# def name(**name):
#     print('hello',name['fname'],name['mname'],name['lname'])
#     #return is calling function


# name(fname ='Neeraj',lname='yadav',mname='kumar')

# marks=[1,2,3,4,5,6,7,8,'Jashan']
# print(type(marks))
# print(marks[1])
# print(marks[-3])
# print(marks[5-3]) # 2=>3
# print(marks[5-7]) #-2=>7

# if 5 in marks :
#     print('pass')
# else:
#     print('Fail')
# j=marks[-1]
# if 'as' in j:
#     print ('yes')
# print(marks[1:-1])

# lst = [i for i in range(5)]
# print(lst)

# lst = [i for i in range(5)if i%2==0]
# print(lst)

# l= [1,92,43,64,75,86,7,8]
# print(l)
# l.append(9)  #add no. in the list
# l.sort(reverse=True)
# print(l) 
# l.sort() #arrange in the order
# print(l)
# l.reverse() # reverse arrangement of list 
# print(l.index(7)) #place value of the no. 
# print(l.count(1)) #no. of occurance of certain no. 
# m = l.copy()
# m[0]= 0
# print(m)
# l.insert(1,898) # insert a no. in list
# print(l)
# m = [900,456,456]
# m.extend(l)  #1st wali list ke age 2nd wali list add kr do
# print(m)
# k =l + m  #Dono list jud jayengi
# print(k)

# tup = (1,5,6,7)
# print(type(tup),tup)
# print(tup[0])
# temp = list(tup)
# temp.append(8) #add item
# temp.pop(3)   #remove the item
# temp[2] = '20'  #change the item
# tup = tuple(temp)
# print(tup)
# print(temp)
# print(tup.count(5))
# print(tup.index(5))

##### KBC Quiz ###
# Q1='Q1, Who is the 1st prime minister of india?'
# a1='a1) Narender Modi'
# b1='b1) Pandit Jawahar lal nehru'
# c1='c1) Atal bihari vajpai'
# d1='d1) Rahul Gandhi'
# print(Q1,a1,b1,c1,d1)
# A1=str(input('Enter your answer here(in the form of a1,b1,c1&d1): '))
# if A1 == 'b1':
#     print('Your answer is correct.''You win 10k')
#     Q2='Q2, Who is the current prime minister of india?'
#     a1='a2) Narender Modi'
#     b1='b2) Pandit Jawahar lal nehru'
#     c1='c2) Atal bihari vajpai'
#     d1='d3) Rahul Gandhi'
#     print(Q2,a1,b1,c1,d1)
#     A2=str(input('Enter your answer here(in the form of a2,b2,c2&d2): '))
#     if A2 == 'a2':
#         print('Your answer is correct. You win 20k')
# else:
#     print('wrong answer. Good Bye Game over')


# letter = 'hey my name is {1} and i am from {0}' ## no. is for indexing
# country='India'
# name='Jashan'
# # print(letter.format(name, country))
# # print(letter.format(country,name)) #varible value is 0,1,2,3,.....
# print(f'hey my name is {name} and i am from {country}') #f-string is used to directly put values in string

# txt = 'for only {price:.2f} dollars!'
# print(txt.format(price = 49.0999))

# print(f'{2*30}') #answer is in form of string
# print(type(f'{2*30}')) #answer is in form of string


# print(f'hey my name is {{name}} and i am from {{country}}') #extra brackets covert it into a comment and print raw f-string.

######## Docstring(help us to understand type of documents) & PEP8 ###########
# def square(n):
#     '''Takes in a no. n, returns the square of n '''  ###line ki next line mai jo likha h sirf wahi doc string hogi agar next line mai humne code likh diya toh doc string none output degi
#     print(n**2)
# square(5)
# print(square.__doc__) ##.__doc__ tells us about function of program or modules

####Zen of python run it into terminal by writing python then import this 
### import this
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

#recursion
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return (n * factorial(n-1))
# n=3
# print(factorial(n))

#Quick Quiz of Fibonacci series..
# def Fib(n):
#     if n<0:
#         print('Input is incorrect')
#     elif n == 0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return Fib(n-1)+Fib(n-2)
# n = 8
# print(Fib(n))

### set ###
# s1 = {2, 3, 6, 4, 5, 4, 7, 8, 7, 9 } #In set, order maintainance and does not repeat same value, and are immutable.
# print(s1)
# harry ={}
# print(type(harry))
# for value in s1:
#     print(value)
# s2 ={3,4,8,5,13}
# print(s2.union(s1)) #join s1 and s2 and form a comman set.
# print(s1,s2)
# s1.update(s2) ## update add values of s2 in s1. 
# print(s1)
# s3 = s1.intersection(s2) #jo dono mai hogi common print kr dega.
# print(s3)
# s4 = s1.symmetric_difference(s2) # jo dono mai common nhi hai
# print(s4)
# s5 = s1.difference(s2) #jo sirf main mai hai usko hi print krega baki agr 1st or 2nd mai kuch common hoga toh use hata dega
# print(s5)
# s6 = s1.isdisjoint(s2) ## pair of sets which does not have any common element are called disjoint sets
# print(s6) 
# s7 = s1.issuperset(s2) #check if all the items of a particular set are present in the original set.
# print(s7)
# s8 = s2.issubset(s1) # kya jo 1st wala h wo 2nd wala ka subset hai??
# print(s8)
# s1.add(18)
# print(s1)
# s1.remove(18) #remove or discaed mai difference ye hai ki agar remove wala item list mai nhi hua toh program error dega or agar discard wala item nhi hua toh program error nhi dega bas age wali line run kr dega  
# s2.discard(13)
# print(s1,s2)
# num = s1.pop()
# print(num)
# del s1 #not defined show krega kyuki pura set delete ho chuka hai
# (print(s1))
# s1.clear() #set khali kr dega but sirf item delete krega na ki set ko toh error nhi ayega
# print(s1) 
#### if and else statement can also used in sets


########Dict is used for mapping and storing information.
# dict ={
    # 'Jashan':'Human being',
    # 'Spoon': 'Object',
    # 'Classroom':'Place'
# }
# print(dict['Jashan'])
# dic = {
#     122024:'Jashan',
#     122042:'Deepali',
#     122012:'Dhruv'
# }
# print(dic[122012])
# info = {'Name':'Jashan','Age':19,'Eligible':True }
# print(info)
# print(info['name2'])  ## if key does not exist then it give error
# print(info.get('name2')) ## if the key is not exist then it print 'NONE'
# for key in info.keys():
#     print(f'The value corresponding to the key {key} is {info[key]}')
# print(info.items())  #gives all the keys and info pairs.
# info2 ={'Name':'Jashan','Age':20,'Eligible':True }
# info.update(info2) ##update the 1st one with other
# print(info)
# info2.clear() #clear the dictonary
# print(info2)
# empt={} #empt form an empty dictonary
# print(empt)
# info.pop('Age') # pop remove the items in dictonary
# print(info)
# del info #delete the whole dict and give error
# print(info) #show error 
# del info['Age'] #this tag delete specific items
# print(info)
# info.popitem()
# print(info)

### for-else combination
# for i in range (7):
#     print(i)
#     if i==3:
#         break    ##break ka use hone pr age ka program ruk ajyega is case mai
# else:
#     print('Sorry no i')

# i = 0
# while i<7:
#     print(i)
#     i = i + 1
#     if i == 4:
#         print('Remove 4')
#         continue
# else:
#     print('sorry no i')

###--Exception handling--###

# a = input('Enter the no. ')
# try:
#     print(f'Multiplication table of {a} is:')
#     for i in range(1,11):
#         print(f'{int(a)} X {i}= {int(a)*i}')
# except Exception as e:
#     # print(e)
#     print('sorry some error occur. because of invalid input!!')
# print('End of the program')

# try:
#     num = int(input('Enter An Integer: '))
#     a = [6,3,4,5,7]
#     print(a[num])
# except ValueError:
#     print('Number Entered is not an integer. ')
# except IndexError:
#     print('Index error occur!!')
###Finally key uses###
# def func1():
#     try:
#         l =[1,2,3,4,4,5,7]
#         i = int(input('Enter the index: '))
#         print(l[i])
#     except:
#         print('some error occured!!!')
#     finally:
#         print('I am always excueted')
#     # print('I am excuted')
# x = func1()
# print(x)

# ###Custom errors### Raising error as early as possible!!!
# a = int(input('Enter the value from 5 to 9: '))
# if (a<5 or a>9):
#     raise ValueError('Value should be in 5 and 9')

# ############KAUN BANEGA CROREPATI#########
# questions =[
#     ['Who is Founder of facebook?',
#     'Jeff','Modi ji','Mark','Bill Gates','None',3],

#     ['Who is Founder of Amazon?',
#     'Jeff','Modi ji','Mark','Bill Gates','None',1],

#     ['Who is Founder of Microsoft?',
#     'Jeff','Modi ji','Mark','Bill Gates','None',4],

#     ['Who is Founder of Disney?',
#     'Jeff','Modi ji','Mark','Bill Gates','None',5],

#     ['Who is Home minister of india?',
#     'Amit Shah','Modi ji','Mark','Bill Gates','None',2],

#     ['Who is Prime minister of India?',
#     'Jeff','Modi ji','Mark','Bill Gates','None',3],

#     ['Who is Father of nation?',
#     'Gandhi ji','Modi ji','Mark','Bill Gates','None',2]
# ]
# levels = [1000,2000,3000,4000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000]
# money=0
# i = 0
# for i in range(0, len(questions)):
#     question = questions[i]
#     print(f'Question for Rs.{levels[i]}')
#     print(f'Q.{question[0]}')
#     print(f'a.{question[1]}')                      
#     print(f'b.{question[2]}')
#     print(f'c.{question[3]}')                      
#     print(f'd.{question[4]}')
#     print(f'd.{question[5]}')
#     reply = int(input('Enter your answer(1-5) or 0 to QUIT:'))
#     if(reply == 0):
#         money = levels[i-1]
#         break
#     if(reply == question[-1]):
#         print(f'Correct answer, You have won RS.{levels[i]}')
#     elif(i == 4):
#         money = 1000
#     elif(i == 9):
#         money = 10000
#     elif(i == 11):
#         money = 100000
#     else:
#         print('Wrong Answers!!')
#         break    
# print(f'You take money to home is{money}')

# ######## Short If & Else statement only used for small####
# a = 330 
# b = 3033
# print('A') if a > b else print('=') if a ==b else print ('B')
# ##Else likhna important hai warna syntax error aa jayega!!
# print(9) if a>b else''
# c = 5 if a>b else 0
# print(c)

# #####Enumerate Function(easy way to get index with value)####
# a = [12,34,35,98,56,13]

# # index =0
# # for mark in a:
# #     print(mark)
# #     if (index == 3):
# #         print('Jashan, You R OSM!!')
# #     index +=1

# for index, mark in enumerate(a):
#     print(mark)
#     if (index == 3):
#         print('Jashan, You R OSM!!')
#     index +=1