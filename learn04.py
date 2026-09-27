# # ------------------------
# # -- Built In Functions --
# # ------------------------
# # all()
# # any()
# # bin()
# # id()
# # ------------------------

# x = [1, 2, 3, 4, []]

# if all(x):

#   print("All Elements Is True")

# else:

#   print("Theres At Least One Element Is False")

# x = [0, 0, []]

# if any(x):

#   print("There's At Least One Element is True")

# else:

#   print("Theres No Any True Elements")

# print(bin(100))

# a = 1
# b = 2

# print(id(a))
# print(id(b))

#sum(iterabnle,start) :

# l=[1,2,3,4]
# print(sum(l))       #       10
# print(sum(l,10))    #       20  >   10+10=20

#round(number,numberofdigits) :

# print(round(159.4))     #       159
# print(round(159.5))     #       160
# print(round(159.7))     #       160

# print(round(159.4444,3))     #       159.444
# print(round(159.4445,3))     #       159.445
# print(round(159.555,2))     #        159.56
# print(round(159.777,2))     #        159.78

# range(start(DV)=0 , end= importent , step(DV)=1) :
    
# print(list(range(10)))      #       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#print() :

#spe:

# print("Hello ahmed how are you")                      # Hello ahmed how are you
# print("Hello","ahmed","how","are","you",sep="@")      # Hello@ahmed@how@are@you

#end :

# print("Hello ahmed how are you",end="   @   ")          # Hello ahmed how are you   @   Hello from VS Code
# print("Hello from VS Code")

#abs(number) : absolute value of a number :

# print(abs(10))      #   10
# print(abs(-10))     #   10

#pow(number,exp,mod) : the power of a number 

# print(pow(2,2))         #       4
# print(pow(2,3,3))         #       2

#min(item,item,item,item,...,or iterator) :

# l=[2,3,4]
# print(min(1,2,3,4))                     #       1
# print(min(l))                           #       2
# print(min("Z","Osama\n"))               #       Osama

# #min(item,item,item,item,...,or iterator) :

# l=[2,3,4]
# print(max(1,2,3,4,5))                   #       5
# print(max(l))                           #       4
# print(max("C","B","D","Osama"))         #       Osama

#slice(start,end)

# l=[1,2,3,4,5]
# print(l[slice(len(l))])     #       [1, 2, 3, 4, 5]
# print(l[:len(l)])           #       [1, 2, 3, 4, 5]
# print(l[slice(4)])          #       [1, 2, 3, 4]
# print(l[:4])                #       [1, 2, 3, 4]

#map(function,iterable) :-------------------------------------------

#   1 :
# def designe (word):
#     return f"#_{word}_#"
# my_words=["ahmed","osama","anas","pop"]
# my_map=map(designe,my_words)
# for name in my_map :
#     print(name)     

#   2 :

# def designe (word):
#     return f"#_{word}_#"
# my_words=["ahmed","osama","anas","pop"]
# for name in map(designe,my_words) :
#     print(name)       

#   3 :

# my_words=["ahmed","osama","anas","pop"]
# for name in map(lambda name : f"#_{name}_#",my_words) :
#     print(name) 

#run :   
      #_ahmed_#
      #_osama_#
      #_anas_#
      #_pop_# 

#app01 :-------------------------------------------

# sum=0
# b=0
# def num (str_numbers):
#     return int(str_numbers)
# str_numbers = ["10", "20", "30", "40"]
# for number in map(num,str_numbers):
#     sum+=number
#     b=b+1
#     print(f"#{b}___{number}")
# print(f"\nThe total is :#{sum}")

#app02 :-------------------------------------------

# def upper (word) :
#     return word.upper()
# words = ["python", "learn", "map", "recursion"]
# for word in map(upper,words) :
#     print(f"{word}")

#app03 :-------------------------------------------

# length_list=[]
# def length (word) :
#     return word
# words = ["ahmed","apple", "banana", "cherry", "kiwi"]
# for word in map(length,words) :
#     length_list.append(len(word))
# print(length_list)

#app03 with lambda :-------------------------------------------

# length_list=[]
# words = ["ahmed","apple", "banana", "cherry", "kiwi"]
# for word in map(lambda word:word , words):
#        length_list.append(len(word))
# print(length_list) 

#app04 :-------------------------------------------
# n=0
# celsius = [0, 20, 37, 100]
# for degree in map(lambda degree : degree*1.8 +32 ,celsius) :
#       print(f"{celsius[n]} C = {degree:.2f} K")
#       n+=1

#app05 :-------------------------------------------

# list3=[]
# def times (number1,number2) :
#       return number1*number2
# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# for number in map(times,list1,list2):
#     list3.append(number)
# print(list3)

#app05 with lambda :-------------------------------------------

# list3=[]
# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# for number in map(lambda number1,number2 :number1*number2 ,list1,list2):
#     list3.append(number)
# print(list3)

#filter : accept a True value only-------------------------------------------

# def checknum(number):
#     if number == 1:
#         return number
# my_numbers =[0,1,0,4,0,6,0]
# for number in filter(checknum,my_numbers) :
#     print(number)

#>>> it dont accept a False value elif you rturn it True 

# def checknum(number):
#     if number == 0:
#         return True
# my_numbers =[0,1,0,4,0,6,0]
# for number in filter(checknum,my_numbers) :
#     print(number)

#reduce :-------------------------------------------

 
# from functools import reduce

# def sumall (num1,num2) :
#     return num1+num2
# my_numbers=[1,2,3,4,5]
# result=reduce(sumall,my_numbers)
# print(result)

#enumerate(iterable,start) :-------------------------------------------

# eng_modules=["analysis","algebra","physics","chemistry"]
# list=reversed(["analysis","algebra","physics","chemistry"])
# for  counter,module in enumerate(list,1):
#     print( f"The module is {counter}: {module}")

#reversed(iterable) :-------------------------------------------

# eng_modules=["analysis","algebra","physics","chemistry"]
# eng_modules_r=reversed(eng_modules)
# for module in eng_modules_r:
#     print( f"The module is : {module}")

# eng_modules=["analysis","algebra","physics","chemistry"]
# for module in reversed(eng_modules):
#     print( f"The module is : {module}")

# eng_modules=["analysis","algebra","physics","chemistry"]
# eng_modules_r=reversed(eng_modules)
# for  counter,module in enumerate(eng_modules_r,1):
#     print( f"The module is {counter}: {module}")

#modules :-------------------------------------------

# import random

# print(f"Random number{random.random()}")
# # print(f"Random number{random : module name .random() : module function}") >>> show a random float number  

#import one or two functions from modules : 

# from random import randint 

# print(f"The random number is : {randint(1,100)}")

# import pyfiglet 
# import  termcolor
# print(termcolor.colored("Ahmed",color="green"))
# print(pyfiglet.figlet_format("Ahmed"))
# print(termcolor.colored(print(pyfiglet.figlet_format("Ahmed")),color="green"))

# import datetime

# print(datetime.datetime.now())               #     2026-09-04 14:04:11.678865
# print(datetime.datetime.now().time())        #     14:04:11.678865
# print(datetime.datetime.now().time().hour)   #     14
# print(datetime.datetime.now().time().minute) #     4
# print(datetime.datetime.now().date())        #     2026-09-04
# print(datetime.datetime.now().year)          #     2026
# print(datetime.datetime.now().month)         #     9
# print(datetime.datetime.now().day)           #     4
# print(datetime.datetime.min)                 #     0001-01-01 00:00:00
# print(datetime.datetime.max)                 #     9999-12-31 23:59:59.999999

#Generator :-------------------------------------------

#>>> Normal Function :

# def get_numbers_list(n):
#     numbers = []
#     for i in range(n):
#         numbers.append(i)
#     return numbers

# print(get_numbers_list(6))

#>>> Generator :-------------------------------------------

# def get_numbers_gen(n):
#     for i in range(n):
#         yield i
# my_gen = get_numbers_gen(4)

# print(next(my_gen))     #     0
# print(next(my_gen))     #     1
# print(next(my_gen))     #     2
# print(next(my_gen))     #     3

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# my_gen=mygenerator()
# print(next(my_gen))     #     1
# print(next(my_gen))     #     2
# print("#"*50)
# for i in my_gen :
#     print(i)            #     3
#                         #     4

#app01 :-------------------------------------------

# def even_numbers(number):
#     for i in range(number):
#         if i%2==0 :
#             yield i
# my_gen=even_numbers(8)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

#app02 :-------------------------------------------

# def countdown(number):
#       while number >1 :
#            yield number
#            number-=1
#       else:
#             number==1
#             yield number
# my_gen=countdown(5)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

#app03 :-------------------------------------------

# def square_gen(*numbers) :
#     for number in numbers :
#         yield number**2
# my_gen=square_gen(5,4,3,2)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# Decorator:-------------------------------------------

#>>>When function whitout parametar :

# def Decorator(func):
#     def add_hash():
#         print("#")
#         func()
#         print("#")
#     return add_hash 
# @Decorator        
# def say_hello():
#     print("Hello from function")

# say_hello()

#>>>When function whit parametar :

# def Decorator(func):
#     def mod(n1,n2):
#         print("The sum is : ")
#         func(n1,n2)
#     return mod

# @Decorator # sum=Decorater(sum)

# def sum(n1,n2):
#     print(n1*n2)

# sum(10,10)

#>>>SpeedTest :-------------------------------------------

# from time import time

# def SpeedTest(func):
#     def modification():
#         start=time()
#         func()
#         end=time()
#         print(f"The time taken of the function is {end - start}")
#     return modification

# @SpeedTest

# def numbers():
#     for number in range(1,1000):
#         print(number)

# numbers()


#pillow :-------------------------------------------

# from PIL import Image 

# my_image=Image.open(r"C:\Users\GIGABYTE\OneDrive\Pictures\alpha.jpg")

# # my_image.show()

# cut=(500,500,1500,1000)
# my_new_image=my_image.crop(cut)
# my_new_image.show()

#Exception :-------------------------------------------

# num=int(input("Enter a number"))
# if num < 0 :
#     raise Exception(f"The number is less then zero")
# else:
#     print(f"{num} is accept")

#try & except :-------------------------------------------

# try : # try the below code and test errors
#       age=int(input("Enter your Age "))
#       if age >=18 :
#                   print(f"age {age} is accept")
#       else:
#             print(f"age {age} is not accept")
# except : # if there is a error it Execute the code below
#       print("enter a valid value")
# finally : # it works whatever happened
#       print("nothing")


#app01 :-------------------------------------------

# tries=3
# while tries>0 :
#       try:
#             file=input("Give the absolute path of the file : ")
#             print(r"Example : C:\Users\GIGABYTE\OneDrive\Documents\python_crash_course.pdf")
#             my_file=open(file,"r")
#             print(my_file.read())
#       except :
#             print("The path is invalid")
#             tries-=1
#             print(f"You have {tries} tries ")
#       else:
#             break
# else:
#       print("try aftre 30 second")