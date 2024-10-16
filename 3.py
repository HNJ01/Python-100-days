####import##
# print(f'hello i am jashan')
# import pandas 
# pandas.read_csv()


# import math
# result = math.sqrt(9)
# result2 =math.cos(1)
# print(result)
# print(result2)
# from math import sqrt, pi
# result = sqrt(9) * pi
# print(result)
####'*' to import all function from module, try to not do this just import one function
# from math import *
# result = sqrt(9) * pi
# print(result)
# from math import sqrt as s
# result = s(9)
# print(result)
# import math as m
# r= m.sqrt(100)
# print(r)

# #####Dir is used to find all function###
# import math 
# print(dir(math))
# print(type(math.nan))

####import your own function from other files and learning '__main__' function uses
# import j
# j.welcome()


###OS module###
# import os 
# f = 
# os.mkdir('C:/Users/asus/Desktop/data')
# if(not os.path.exists('C:/Users/asus/Desktop/data')):
#     os.mkdir('C:/Users/asus/Desktop/data')

# for i in range(1,101):
    # if(not os.path.exists('C:/Users/asus/Desktop/data/Tutorial{i}')):
    #     os.mkdir(f'C:/Users/asus/Desktop/data/Day{i}')
    #     os.renames(f'C:/Users/asus/Desktop/data/Day{i}',f'C:/Users/asus/Desktop/data/Tutorial{i}')
#    folders = os.listdir('C:/Users/asus/Desktop/data')
# print(folders)  
# for folder in folders:
#     print(folder)
#     print(os.listdir(f'C:/Users/asus/Desktop/data/{folder}'))
    # print(os.getcwd())

# st = input('Enter the message: ')
# words =st.split(' ')
# coding = input('Enter yes(For coding) or no(for decoding): ').lower
# if coding == 'yes':
#     coding = True
# else:
#     coding = False
# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#             r1='dsf'
#             r2 ='jkr'
#             stnew =r1+ word[1:]+ word[0]+r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#             print(" ".join(nwords))
# else:
#     nwords = []
#     for word in words:
#         if(len(word)>=3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#             print(" ".join(nwords))

#####Secreat code language####
# st = input('Enter the message: ')
# words = st.split(' ')
# coding = input('Enter yes (For coding) or no (for decoding): ').lower()

# if coding == 'yes':
#     coding = True
# else:
#     coding = False

# if coding:
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             r1 = 'imt'
#             r2 = 'jkr'
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
# else:
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

###########Global variable vs local variable
# x = 4
# print(x)
# def hello():
#     global x ##global keyword is used to change global variable value inside a function
#     x = 5
#     print(f'The local x is here {x}')
#     print('hello j')

# print(f'the global x is {x}')

# hello()
# print(f'the global x is now {x}')

# #######File handling####

# # Reading file
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'r')
# print(f.read())
# f.close()
# # Writing file
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'w')
# f.write('Hello World')
# f.close()
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'r')
# print(f.read())
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'a')
# f.write('\nI am Jashan')
# f.close()
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'r')
# print(f.read())
# f.close()


#####read and realine method- to read the file...
# f = open ('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# f = open ('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f'marks of student {i} in maths is {m1}')
#     print(f'marks of student {i} in english is {m2}')
#     print(f'marks of student {i} in SST is {m3}')
#     print("End of File!")
# f.close()

# #####Write line methods(create a new file and write our data in it)
# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile2.txt', 'w')
# lines = ['1,2,3\n', '4,5,6\n', '7,8,9\n']
# f.writelines(lines)
# f.close()

# f = open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile2.txt', 'r')
# print(type(f))
# f.seek(10) # seek is used to jump to a particular position in a file
# print(f.tell()) # tell is used to find the current position in a file
# data = f.read(5)
# print(data)

# with open('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile2.txt', 'w') as f:
#     f.write('Hello, World!')
#     f.truncate(5) # used to truncate the file 5 characters from beginning

# with open ('C:\\Users\\asus\\atom\\.vscode\\100 days python\\myfile2.txt', 'r') as f:
#     print(f.read())

##############lamda function in python: Anonymous functions(functions without a name)used in mathematical function or only one liner######################
# def double(x):
#     return x * 2
# double = lambda x: x * 2
# cube = lambda x: x * x * x
# print(double(5))
# print(cube(10))

