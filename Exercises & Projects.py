# list comprehension :

#ex1 :

# squares = [n ** 2 for n in range(1, 21)]
# print(squares)

#ex2 : 

# numbers = [3, 7, 2, 14, 9, 8, 11, 6, 5, 10]
# even=[num for num in numbers  if num%2==0 ]
# print(even)

#ex3

# words = ["python", "list", "comprehension", "is", "powerful"]
# len=[ len(word) for  word in words ]

#ex4

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# upper=[word.upper() for word in fruits ]
# print(upper)


#Generators :

#ex1:

# def square(num):
#     for i in range(1,num+1):
#         yield i**2
# my_gen=square(5)
# for square in square(5) :
#     print(square)

#-------------------------------------------------------------------------------------------------------

# from random import randint
# class Dice :
#     def __init__(self,gees):
#         self.gees=gees
#     def roll(self):
#         tries=3
#         sum=randint(1,6) + randint(1,6)
#         print(sum)
#         while tries >=1 :
#             if sum == self.gees :
#                 return "Gongrats ! , the sum is correct ."
#             elif sum != self.gees :
#                 tries-=1
#                 if tries >=1 :
#                     self.gees=int(input(f"Wrong ! , You have {tries} tries , Try agian : "))
#         else:
#             return f"Sorry , All your chances are over , and the sum is {sum} "
# one=Dice(3)
# print(one.roll())


#-------------------------------------------------------------------------------------------------------

