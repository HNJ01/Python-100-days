# ###Time module##
# import time
# # print(time.time())
# import time

# def usingWhile():
#     i = 0
#     while i<5000:
#         i+=1 #or i=i+1
#         print(i)

# def usingFor():
#     for i in range(9000):
#         print(i)


# init = time.time()
# usingWhile()
# t1=time.time() - init
# usingFor()
# print(time.time() - init)
# print(t1)

# ###time.sleep()
# print(4)
# time.sleep(4)
# print('this will print after 4 second')

# t = time.localtime()
# formatted_time = time.strftime('%Y-%m-%d %H:%M:%S',t)
# print(formatted_time)

# #####Creating Command Line Utilities Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.
# ###DOBARA PADH LIYO JB WORK KRNA HO
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument('url',help = 'Url of the file to download')
# parser.add_argument('output',help = 'by which name do you want to save the file')

# args = parser.parse_args( )

# print(args.url)
# print(args.output)

###############WARLUS OPERATOR
# a = True
# print(a:=False)  #### ':=' is walnus operator

# numbers = [1,2,3,5,4]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())

# ###WITHOUT WALNUS
# foods = list()

# while True:
#     food= input( "What food do you like: ")
#     if food == "quit" :
#         print(foods)
#         break
#     foods.append( food )
    
# ###WITH WALNUS
# foods = list()
# while (food := input('What food do you like?: ')) != 'quit' :
#     foods.append(food)

# print(foods)

# ######SHUTIL MODULE
# import shutil
# import os
# #####shuttle._____(src(original location),dst(Final location))
# # shutil.copy('c:/Users/asus/atom/100 days python/1.py','c:/Users/asus/atom/100 days python/8.py')
# # shutil.copytree()  ###used to copy whole folder 
# # shutil.move() ##used to move the file from one location to another
# # os.remove('c:/Users/asus/atom/100 days python/8.py') ##used to delete some file

# #####REQUEST MODULE-important for practical work
# #####Detailed study later

# import requests
# response = requests.get('https://google.com')
# # print(response.status_code)
# # print(response.headers['content-type'])
# # print(response.encoding)
# # print(response.text) ###GIVE THE CODE OF WEBSITE

# ##############GENERATORS-####
# '''Generators in Python are special type of functions that allow you to create an iterable sequence of values. A
# generator function returns a generator object, which can be used to generate the values one-by-one as you iterate
# over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate
# the values on-the-fly, rather than having to create and store the entire sequence in memory.'''
# def my_generator():
#     for i in range(5):
#         yield i 
# #####yield returns a value from the generatorand suspends the excution of the function until the next value is requested.

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # for i in gen():
# #     print(i)

# ####Function caching
# import functools
# import time
# @functools.lru_cache(maxsize=None) 
# ###lru-cache is used to memoize the function so that it do not take much time to print next function
# def fx(n):
#     time.sleep(2)
#     return n*5



# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print('Done for 2')
# print(fx(6))
# print('Done for 6')

# ###already compute that's why it run so fast
# print(fx(20))
# print("Done for 20")
# print(fx(31))
# print('Done for 31')  ###not computed already that's why it run on same speed
# print(fx(2))
# print('Done for 2')
# print(fx(6))
# print('Done for 6')

# ###########Regular Expressions###
# import re
# # pattern = 'was'
# # # pattern = 'king'
# # text = 'I was reading a book, when i was in class in my college i was kidding in the group and like to do my work' 
# # match = re.search(pattern,text)
# # print(match)

# pattern = r'[A-Z]yclone'
# text = '''Intense Tropical Cyclone Dumazile was a strong tropical Dyclone that brought flooding to Madagascar and Réunion in early March 2018. Dumazile originated from an area of low pressure that formed in the South-West Indian Ocean near Agaléga on 27 February. The system concentrated into a tropical disturbance on 2 March and was named the next day, as it intensified into a tropical storm. Amid conditions conducive for intensification, Dumazile strengthened over the next two days and reached peak intensity on 5 March as an intense tropical Eyclone, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central pressure of 945 hPa (27.91 inHg). The system weakened steadily over the next couple days because of increasing wind shear as it tracked to the southeast. Dumazile became post-tropical on 7 March and eventually dissipated completely on 10 March near the Kerguelen Islands.'''
# matches = re.finditer(pattern,text)
# for match in matches:
#     # print(match.span) ##span tell us position
#     # print(type(match.span()))  ##type is tuple
#     # print(match.start()) ##start tell us the position
#     # print(match.group()) ##group tell us the word
#     # print(text[match.span()[0]:match.span()[1]])


# ######AsyncIO- used for high performance I/O operations in a concurrent & non-blocking manner. In Python, asynio module is used
# import asyncio
# import time
# import requests

# # async def func1():
# #     time.sleep(3)
# #     print('func1')
# #     return 'Boss'

# # async def func2():
# #     time.sleep(2)
# #     print('func2')
# #     return 'Man'

# # async def func3():
# #     time.sleep(1)
# #     print('func3')
# #     return 'Sir'

# # async def main():
# #     # task = asyncio.create_task(func1()) ##this allow other task to run on time
# #     # # await func1()
# #     # await func2()
# #     # await func3()
# #     L = await asyncio.gather(
# #         func1(),
# #         func2(),
# #         func3()
# #         )
# #     print(L)
# # asyncio.run(main())

# async def function1( ):
#     URL = "https://instagram.com/favicon.ico"
#     response= requests.get(URL)
#     open("instagram1.ico", "wb").write(response.content)
#     print("func 1")
#     return "Harr3y"
# async def function3( ):
#     URL = "https://instagram.com/favicon.ico"
#     response= requests.get(URL)
#     open("instagram2.ico", "wb").write(response.content)
#     print("func 1")
#     return "Harry4"
# async def function3( ):
#     URL = "https://instagram.com/favicon.ico"  ##request the website to download the image
#     response= requests.get(URL)
#     open("instagram3.ico", "wb").write(response.content)
#     print("func 1")
#     return "Harry5"

# async def main():
#     L = await asyncio.gather(  ####tasks are running together so that output come soon
#         function1(),
#         function3(),
#         function3()
#         )
#     print(L)

# asyncio.run(main())

# ###############MUTLTITHREADING IN python
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def fun(seconds):
#     print(f'Sleeping For {seconds} seconds')
#     time.sleep(seconds)

# # # normal code
# # fun(3)
# # fun(2)
# # fun(1)
# time1 = time.perf_counter()
# ##Code with threading
# t3 = threading.Thread(target = fun, args =[3])
# t2 = threading.Thread(target = fun, args =[2])
# t1 = threading.Thread(target = fun, args =[1])
# t3.start()
# t2.start()
# t1.start()

# t1.join()
# t2.join()
# t3.join()

# time2 =time.perf_counter()
# print(time2-time1)
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         l = [1,2,3,4,6,7,8]
#         results = executor.map(fun, l)
#         for result in results:
#             print(result)
# poolingDemo()

#######Multiproccessing
import multiprocessing

# def my_func():
#     print('hello')
#     print('Hello from process', multiprocessing.current_process().)

from multiprocessing import Pool
def process_task(task):
    # Do some work here
    print("Task processed:", task)
if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)

def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Counter value:", counter.value)











