#OOP :#--------------------------------------------------------

# class Member :
#     def __init__(ahmed):
#         print("Hi from OOP !")

# Member()    #   Hi from OOP !

#--------------------------------------------------------

# class hi :
#     def __init__(self):
#         self.name="ahmed"   # attribute

# object1=hi()
# object2=hi()
# # print(dir(member1))
# print(object1.name)     #   ahmed 
# print(object2.name)     #   ahmed 

#--------------------------------------------------------

# class hi :
#     def __init__(self,user_name):
#         self.name=user_name   # attribute

# object1=hi("Ahmed")
# object2=hi("Osama")
# print(object1.name)     #   ahmed 
# print(object2.name)     #   Osama 

#--------------------------------------------------------

# class car :
#     def __init__(self,car_name,car_color):
#         self.car_name=car_name
#         self.car_color=car_color
# my_car=car("mercedes","black")
# print(my_car.car_name)
# print(my_car.car_color)

#--------------------------------------------------------

# class car :
#     def __init__ (self,car_type,module,year):
#         self.car_type=car_type
#         self.module=module
#         self.year=year
# my_car=car("Toyota","Camri",2022)
# print(f"The {my_car.year} {my_car.car_type} {my_car.module}\'s is now running !")

#--------------------------------------------------------

#Class Attribute :

# class car :
#     not_allowed_cars=["honda","atos"]   #   Class Attribute
#     def __init__ (self,car_type,module,year):
#         self.car_type=car_type
#         self.module=module
#         self.year=year
#         if car_type in car.not_allowed_cars :
#             print("This car is not allowed")
#             raise ValueError  
#         else:
#             print(f"The {self.year} {self.car_type} {self.module}\'s is now running !")

# my_car=car("Toyota","Camri",2022)

#--------------------------------------------------------

#Class Methods :

# class car :
#     @classmethod
#     def mod (cls,car_type,module,year):
#         print(f"The car_type is : {car_type} \nThe module is : {module}\nThe yaer of production : {year}")
#     def __init__ (self,car_type,module,year):
#         self.car_type=car_type
#         self.module=module
#         self.year=year
#         print(f"The {self.year} {self.car_type} {self.module}\'s is now running !")

# car_one=car("Toyota","Camri",2026)

#--------------------------------------------------------

#Magic Methods :

#-----__calss__----- : it show you what the that the Object is belong to .

# class hi :
#     def __init__(self,name):
#         self.name=name
#         print(f"Hello {self.name}")

# my_name=hi("Ahmed")
# print(my_name.__class__)        #       <class '__main__.hi'>

#--------------------------------------------------------

# class Hi :
#     def __init__(self,name):
#         self.name=name
#         print(f"Hello {self.name}")
#     def __len__(self):
#         return len(self.name)
#     def __str__(self):
#         return f"Hello {self.name} and Welcome from __str__ ! ."
# my_name=Hi("Ahmed")      #       Hello Ahmed
# print(len(my_name.name))    #   5
# print(my_name)      #       Hello Ahmed and Welcome from __str__ ! .

#--------------------------------------------------------

# class book :
#     def __init__(self,book_name,author,pages):
#         self.author=author
#         self.book_name=book_name
#         self.pages=pages
#         print(f"The book {book_name}\nwrited by the author {author}")
#     def get_info(self):
#         print(f"The book {self.book_name} who author is {self.author} is amazing")
#     def __str__(self):
#         return f"{self.book_name} : {self.author}"
#     def __len__(self):
#         return self.pages
# my_book=book("flow","Me",200)
# my_book.get_info()
# print(my_book.book_name)
# print(my_book)
# print(len(my_book))

#--------------------------------------------------------

#app :

# import os 

# class Counter :
#     def __init__(self,path):
#         self.path=path
#         self.attempts=3
#     def user_attempt(self):
#         while self.attempts>=1:
#             try :
#                 file=open(self.path,"r")
#                 return (file.read())
#             except:
#                 self.attempts-=1
#                 if self.attempts==0:
#                      return "Your attempts was fenish "
#                 print(f"There is a error , You have a {self.attempts} attempts ,Try agian")
#                 self.path=input("Enter the file path : ")
#     def __str__(self):
#         try :
#             with open (self.path,"r") as file :
#                 return ">>>     The file opened successfully ."
#         except:
#             return">>>     Sorry , we cant open the file ."
# one=Counter(r"C:\Users\GIGABYTE\OneDrive\Desktop\Learn_Python\fff.txt")
# print(one.user_attempt())
# print(one)

#--------------------------------------------------------

#Inheritance :  النسخ او الوراثة 

# class Food :
#     def __init__(self,name):        #       Initialize Function
#         self.name=name              #       Attribute
#         print(f"{self.name} is craeted form main class (Food class)")
#     def eat(self):             #       Method
#         print(f"Eat the {self.name} from eat function")
# class FF(Food) :
#     def __init__(self,name):
#         super().__init__(name)      #       super().__init__() = self.name=name = Food.__init__(name)
#         print(f"Hello from {self.name}")

# pizza=Food("pizza").eat("pizza")    #     pizza is craeted form main class (Food class)
#                                     #     Food is craeted form main class
#                                     #     Eat the food from eat function

# shawarma=FF("shawarma")             #     shawarma is craeted form main class (Food class)
#                                     #     Hello from shawarma
#                                     #     Eat the shawarma from eat function

#--------------------------------------------------------

#Encapsulation :

# class Member :
#     def __init__(self,name):
#         self._name=name     #   Protected Attribute

# one=Member("Ahmed")
# print(one._name)

# Just an agreement among programmers that this feature is protected from use in other classes

# class Member :
#     def __init__(self,name):
#         self.__name=name     #   Privat Attribute
#     def say_hello(self) :    #   Methods
#         return f"Hello , Your name is : {self.__name}"
  
# one=Member("Ahmed")
# print(one.say_hello())     #   Hello , Your name is : Ahmed
# # print(one.__name)        #   AttributeError: 'Member' object has no attribute '__name'
# print(one._Member__name)   #   Ahmed 
# #   You can access the private attribute only by calling the function

#--------------------------------------------------------

#Getters & Setters :

# class Member :
#     def __init__(self,name):
#         self.__name=name     #   Privat Attribute
#     def get_name(self) :     #   This Methods show you the Privat Attribute
#         return self.__name
#     def set_name(self,new_name):
#         self.__name=new_name
#         return self.__name
# one=Member("Ahmed")
# print(one.get_name())              #   Ahmed
# print(one.set_name("Osama"))       #   Osama

#--------------------------------------------------------

#Property Decorator :

# class Member :
#     def __init__(self,name):
#         self.__name=name     #   Privat Attribute
#     @property   #   It raed the method below as a Attribute (Property)
#     def get_name(self) :     
#         return self.__name
#     def set_name(self,new_name):
#         self.__name=new_name
#         return self.__name
# one=Member("osama")
# print(one.get_name())

#--------------------------------------------------------

#ABCs Abstract Base Class :     

# كلاس مجرد اساسي بهدف استعماله داخل كلاسات اخرى 

# from abc import ABCMeta                     #   we import this module for this class to be a abstract base class 
# from abc import abstractmethod              #   we import this module for this method to be a abstract base method
# class Programming (metaclass=ABCMeta):      #   abstract class
#     @abstractmethod
#     def has__oop(self):                     #   abstract method
#         pass
#     @abstractmethod
#     def name__oop(self):
#         pass


# class Python(Programming):
#     def has__oop(self):
#         return "Yes"
#     def name__oop(self):
#         return "Python"

# class C(Programming):
#     def has__oop(self):
#         return "No"
#     def name__oop(self):
#         return "C"

# one=Python()
# print(one.has__oop())        #      Yes     
# print(one.name__oop())       #      Pyhton

# two=C()
# print(two.has__oop())        #      No
# print(two.name__oop())       #      C
print(type(None))