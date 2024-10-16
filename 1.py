# # a=input(str("Enter your name"))
# # b=input(str('enter your name'))
# # print(a,b)
# print("hello \nmy name is jashan \nhow are you?") #\n escape character- next words are print in next line
# a=float(input('Enter 1st no.: '))
# b=float(input('Enter 2nd no: '))
# o=input(('Enter the Operator:(%,*,+,-,/) '))
# if o=='%':
#     print(a%b)
# elif o=='*':
#     print(a*b)
# elif o=='+':
#     print(a+b)
# elif o=='-':
#     print(a-b)
# elif o=='/':
#     print(a/b)
# else:
#     print ('Invalid no. or operator')
# a= '1'
# b='2'
# a= int(a)
# b= int(b) #explicite type casting
# print(a+b)
# #implicit type casting
# c= 1.9
# d = 4 # automatically convert int to float
# print(c+d)

# a=('gytgdhctfdhgvhufhygfhjgkjhjhflgdtyyfdjhbmnn,vg fy6jhggcsc gfdhkudf ssdtffdfghhgufgyhbbkjdckancvbxczfy78dyfoiduoojxxvbzmnn,mzzjlakoswiureuy')
# # for character in a:
# #     print(character)
# name='jashan'
# print(len(a))
# print(a[0:8],a[-3:-1])#last se type krega
# print(name[-4:-2])

#Clock With greeting: using time module
# import time
# timestamp= time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp= time.strftime('%H')
# print(int(timestamp))
# if timestamp <= '12':
#     print('Good morning Sir')
# elif timestamp >='12' and timestamp <= '16':
#     print('Good afternoon sir')
# else:
#     print('Good evening sir')

# x= 5
# match x:
#     case 1 : print("one")
#     case 2 : print("two")
#     case 3 :print("more than two")
#     case _ :print(x)

# uname= str(input('enter your name: '))
# name = str(input('enter your friend name: '))
# for i in name:
#     print(i)  ## i used for iterating object or single words 
#     if(i == 'b'):
#         print('b is here')

# colors = ['red','blue','green','black','white']
# for x in colors:  #x is used for elements of list 
#     print(x)
#     for i in x:
#         print(i)

# for k in range(1,100):  ## range always print one no. less then final alotted number. k is used for number 
#     print(k)
#     print(k+1)

# for k in range(1,160,3): ### 3rd number put space between 2 words
    # print(k+1)

# i = int(input('Enter your 3 digit number as password in integer: '))  ##har bar last se dobara code padhta h while loop or use excute krta hai
# while(i!=101):
#     print(i)
#     print('Wrong password please enter correct password!!')
#     i = int(input('Enter your password again as integer: '))
# print('Your password is done correct. welcome to era😈😈')

# count = 5 
# while(count > 0):
#     print(count)
#     count = count - 1
# else:
#     print('I am inside else.')

####emulate do while loop.

# c = 1000
# while (c > 0):
#     print('hello buddy!!')
#     c= c-1

# def name(n): 
# 	if n != 0: 
# 		name(n-1) 
# 		print("name") 
# name(5)

# name = "Hello" 
# print((name + " ") * 10)




#for i in range(15):
#    i=i+1
#    if(i==10):
#        print('skip the loop!!')
#        continue
#    print('5x',i, '=' , 5*i )

# i = 0  ###Do-while loop- atleast runs one 
# while True:
#     print(i)
#     i=i+1
#     if(i % 100 == 0):
#         break

######::::----Function----:::######

#def calculateGmean(a,b):
#    mean = (a*b)/(a+b)
#    print(mean)

#def greatnum(a,b):
#    if ( a > b):
#        print('First NO. is greater')
#    elif(a==b):
#        print('First NO. is equal to Second no.')
#    else:
#        print('Second NO. is greater')
#    pass   #pass this help to write down by others coder



#c=int(input('Enter the 1st number '))
#d=int(input("Enter the 2nd no. "))
#calculateGmean(c,d)
#greatnum(c,d)  #greatnum is used to call the function  


