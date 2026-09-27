#>>>issubset :

# a={1,2,3,"hamed","oss"}
# b={2,3,"hamed"}
# print(a.issubset(b))                          #         False

#>>>isdisjoint :

# a={1,2,3,"hamed","oss"}
# b={2,3,"hamed"}
# c={0,100, 1268, 25, "yoyo"}
# print(a.isdisjoint(b))                            #       False
# print(a.isdisjoint(c))                            #       True

#Dictionary :

# my_dic={
#     "my_bac_note" : 13.57 ,
#     "my_age" : 18 ,
#     "country" : "Algeria" ,
#
#     }
# print(my_dic)
# print(my_dic["my_bac_note"])            #       13.57
# print(my_dic.get("my_bac_note"))        #       13.57
# print(my_dic.keys())                    #       dict_keys(['my_bac_note', 'my_age', 'country'])
# print(my_dic.values())                  #       dict_values([13.57, 18, 'Algeria'])
#

# my_dic = {
#     "my_bac_note": 13.57,
#     "my_age": 18,
#     ["country"]: "Algeria",
#
# }
# print(my_dic)           #           TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

# my_dic = {
#     "my_bac_note": 13.57,
#     "my_age": 18,
#     {"country"}: "Algeria",           #           TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
#
# }

#>>>Two-Dimensional-Dictionary :

# mydic={
#     "one":{
#         "subject 01" : "analysis"
#     },
#     "two" : {
#         "subject 02" : "python"
#     },
#     "three" : {
#          "subject 03" : "css"
#     },
# }

#>>>clear :

# my_dic={
#     "name":"ahmed",
#     "age": 18,
#     "country":"algeria"
# }
# print(my_dic)           #       {'name': 'ahmed', 'age': 18, 'country': 'algeria'}
# my_dic.clear()
# print(my_dic)           #       {}

#>>>update:

#>>>1st method :

# my_dic={
#     "name":"ahmed",
#     "age": 18,
#     "country":"algeria"
# }
# my_dic["birthday"]=2008
# print(my_dic)           #       {'name': 'ahmed', 'age': 18, 'country': 'algeria', 'birthday': 2008}

#2end method :

# my_dic={
#      "name":"ahmed",
#      "age":18,
#      "country":"algeria"
# }
# my_dic.update({
#     "birthday": "2008",
#     "hobits" : ["programming","mathematics","linux","electronics"],
#
# })
# print(my_dic)           #        {'name': 'ahmed', 'age': 18, 'country': 'algeria', 'birthday': '2008', 'hobits': ['programming', 'mathematics', 'linux', 'electronics']}

#>>>copy :

# my_dic={
#      "name":"ahmed",
#      "age":18,
#      "country":"algeria"
# }
# my_dic02=my_dic.copy()
# print(my_dic02)         #       {'name': 'ahmed', 'age': 18, 'country': 'algeria'}

#>>>setdefault

# my_dic={
#      "name":"ahmed",
#      "age":18,
#      "country":"algeria",
# }
# print(my_dic.setdefault("age",100))               #         18
# print(my_dic.setdefault("hobits","fighting"))          #         fighting
# print(my_dic)            #         {'name': 'ahmed', 'age': 18, 'country': 'algeria', 'hobits': 'fighting'}

#>>>popitem :

# my_dic={
#       "name":"ahmed",
#       "age":18,
#       "country":"algeria",
# }
# my_dic.update({"hobits":"mma"})
# print(my_dic.popitem())            #         ('hobits', 'mma')

#>>>items :

# my_dic={
#        "name":"ahmed",
#        "age":18,
#        "country":"algeria",
#        "hobits":"mma"
# }
# my_total_dic=my_dic.items()
# my_dic["hobits"]="chess"
# print(my_total_dic)           #         dict_items([('name', 'ahmed'), ('age', 18), ('country', 'algeria'), ('hobits', 'chess')])
#
# #>>>fromkeys :
#
# a=("jjo","hfj","shk")              #         keys
# b=("gng","jjgj","jjjjg")           #         values
#print(dict.fromkeys(a,b))          #              {'jjo': ('gng', 'jjgj', 'jjjjg'), 'hfj': ('gng', 'jjgj', 'jjjjg'), 'shk': ('gng', 'jjgj', 'jjjjg')}

#>>>del :

# my_dic={
#         "name":"ahmed",
#         "age":18,
#         "country":"algeria",
#         "hobits":"mma"
# }
# del my_dic["name"]
# print(my_dic)           #       {'age': 18, 'country': 'algeria', 'hobits': 'mma'}

#Boolean :          >>>         logical answer just use True or False to answer

#>>>True values :

# print(bool("ahmed"))
# print(bool(1000))
# print(bool(1000.556))
# print(bool(100+50j))
# print(bool(True))
# print(bool([1,2,3,4,5,6]))
# print(bool({1,2,3,4,5,6}))
# print(bool((1,2,3,4,5,6)))
#
# #>>>False value :
#
# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool(None))
# print(bool(False))
# print(bool([]))
# print(bool({}))
# print(bool(()))

#Type Conversion :

#>>>str()

#---------->itn and float to str() :

# age=18
# print(type(age))            #       <class 'int'>
# print(type(str(age)))       #       <class 'str'>
# age1=18.67
# print(type(age1))           #       <class 'float'>
# print(type(str(age1)))          #       <class 'str'>

#** Attention **:

# a="ahmed"
# b="18"
# c="18.67"
# print(float(a))     #       ValueError: could not convert string to float: 'ahmed'
# print(float(b))     #       18.0
# print(int(c))       #       ValueError: invalid literal for int() with base 10: '18.67'

#tuple() :

#---------->string,list,set,dictionary to tuple:

# s0="i love python so much"
# l=["a","b","c"]
# s={1,2,3,"oss","ahmed"}
# d={"age":18 , "country": "algeria"}
# print(tuple(s0))        #       ('i', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 's', 'o', ' ', 'm', 'u', 'c', 'h')
# print(tuple(l))         #       ('a', 'b', 'c')
# print(tuple(s))         #       ('ahmed', 1, 2, 3, 'oss')
# print(tuple(d))         #       ('age', 'country')

#list() :

#---------->string,tuple,set,dictionary to list:

# s0="i love python so much"
# t=("a","b","c")
# s={1,2,3,"oss","ahmed"}
# d={"age":18 , "country": "algeria"}
# print(list(s0))         #       ['i', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 's', 'o', ' ', 'm', 'u', 'c', 'h']
# print(list(t))          #       ['a', 'b', 'c']
# print(list(s))          #       [1, 2, 3, 'ahmed', 'oss']
# print(list(d))          #       ['age', 'country']

#set() :

#---------->string,tuple,set,dictionary to list:

# s0="i love python so much"
# t=("a","b","c")
# l=[1,2,3,"oss","ahmed"]
# d={"age":18 , "country": "algeria"}
# print(set(s0))          #       {'u', 'm', 'i', 'o', 'v', 'e', 'c', 'h', 'n', 'y', 'l', 't', 's', 'p', ' '}
# print(set(t))           #       {'a', 'c', 'b'}
# print(set(l))           #       {1, 2, 3, 'oss', 'ahmed'}
# print(set(d))           #       {'country', 'age'}

#dict() :

#---------->tuple,set,list to dictionary:

# t=("a","b","c")
# l=[1,2,3,"oss","ahmed"]
# s={1,2,3,"oss","ahmed"}
#
# # print(dict(t))          #       ValueError: dictionary update sequence element #0 has length 1; 2 is required
# t=(("a",20),("b","ahmed"),("c",60))
# print(dict(t))          #       {'a': 20, 'b': 'ahmed', 'c': 60}
#
# # l=[1,2,3,"oss","ahmed"]
# # print(dict(l))          #       TypeError: object is not iterable
# # Cannot convert dictionary update sequence element #0 to a sequence
# l=[["a",1],["b",2],["c",3]]
# print(dict(l))          #       {'a': 1, 'b': 2, 'c': 3}
#
# s={1,2,3,"oss","ahmed"}
# print(dict(l))          #           TypeError: cannot use 'set' as a set element (unhashable type: 'set')
# s={{1,2}, {2,20}}
# print(dict(l))          #       TypeError: cannot use 'set' as a set element (unhashable type: 'set')

#practicals :

#---------->User input :

# family_name=input("what is your family name?")
# first_name=input("what is your first name?")
# last_name=input("what is your last name?")

# print("hello {} {} {}".format(family_name,first_name,last_name))
# print(f"hello {family_name} {first_name} {last_name}")
# print("hello %s %s %s"%(family_name,first_name,last_name))

#---------->Slices Email :

# email="ghamriahmed@gmail.com"
# print(email.index("@"))         #       @
# print(email[0:11])          #       ghamriahmed
# print(email[:11])           #       ghamriahmed
# print(email[:email.index("@")])         #       ghamriahmed

# name=input("what is your name").strip().capitalize()
# email=input("what is your email").strip()
# address=input("what is your address").strip().capitalize()
# print("hello my name is {} and my email {} and my address is {}".format(name,email,address))
# print("hello %s\nyour email is %s\nand you address is %s"%(name,email,address))

#---------->Practical your age full details :

# age=float(input("enter your age"))
# months=age*12
# weeks=months*4
# days=weeks*7
# hours=days*24
# minutes=hours*60
# seconds=minutes*60
# print("you lived for :")
# print("%s months" %(months))
# print(f"{weeks} weeks")
# print("{} days ".format(days))
# print("my age is 18.5 and : {} months and {} weeks and {} days ".format(months,weeks,days))
# print(f"my age is 18.5 and : {months} months and {weeks} weeks and {days} days ")
# print("my age is 18.5 and : %s months and %s weeks and %s days "%(months,weeks,days))

#if condition applications :

# name=(input("Enter your Name")).capitalize()
# country=input("Enter your Country").capitalize()
# q=input("you are a student").capitalize()
# course_name="Full Python Course from Scratch"
# course_prise=5000
# if country == "Algeria" and q == "Yes" :
#     print(f"Hello {name} ,because you are from {country} , The \"{course_name}\" Prise is {course_prise} DA , but because you are a student the prise is {course_prise-3500}")
# else :
#     print(f"Hello {name} ,because you are from {country} , The \"{course_name}\" and the Prise is {course_prise-1500} DA")

# age=float(input("Give your age"))
# months=age*12
# weeks=months*4
# days=months*30
# unit=input("chose your unit").lower()
# if unit=="months" :
#     print(f"you lived :     {months} months")
# elif unit=="weeks" :
#     print(f"you lived :     {weeks} weeks")
# elif unit=="days" :
#     print(f"you lived :     {days} days")

#Practical Membership Control :

# admins=["Ahmed","Mohammed","Pop","Amir","Fouad","Hocine"]
# user_name=input("What's your name?").strip().capitalize()
# if user_name in admins :
#     print(f"Welcome {user_name} , you are in the admins's list")
#     print(admins)
#     edit=input("Would you like to edit your user_name").strip().capitalize()
#     if edit == "Yes" or edit == "Y" :
#         update=input("Would you like to update your user_name?").strip().capitalize()
#         if update == "Yes" or update == "Y" :
#             new_user_name=input("enter your new user_name").strip().capitalize()
#             admins[admins.index(user_name)]=new_user_name
#             print(admins)
#             print("Update was successful")
#         elif update == "No" or update == "N" :
#             Delete = input("Would you like to delete your user_name?").strip().capitalize()
#             if Delete== "D" or  Delete == "Delete" or Delete=="Yes" or Delete == "Y":
#                 admins.remove(user_name)
#                 print(admins)
#                 print("Delete was successful")
#             elif Delete == "No" or Delete == "No":
#                 exit()
#     else:
#         exit()
# else:
#     print(f"Sorry {user_name}, you are not in the admins's list")
#     join=input("Would you like to join in the admin's list?").strip().capitalize()
#     if join == "Yes" or join == "Y":
#         admins.append(user_name)
#         print(admins)
#         print("Join was successful")
#     else:
#         exit()

#Loop while and else :

# a=1
# while a<10 :
#     print(a)
#     a+=1        # a=a+1
# else: #     when while condition become false
#     print("loop is done")


# myl=["gh","ah","abd","al","ho","mo","ad","is"]
# myn=1
# a=0
# while a<len(myl) and myn<=8 :
#     print(f"{myn} : {myl[a]}")
#     a+=1
#     myn+=1
#
#
# myl=["gh","ah","abd","al","ho","mo","ad","is"]
# a=0
# while a<len(myl) :
#     print(f"#{str(a+1).zfill(2)} : {myl[a]}")
#     a+=1

#Run:

#01 : gh
#02 : ah
#03 : abd
#04 : al
#05 : ho
#06 : mo
#07 : ad
#08 : is

#app01

# a=input("Give me a number or enter "exit" to quit:  ")
# while True :
#     if a.lower()=="exit":
#         print("Thank you , Have a nice day.")
#         break
#     else:
#         a=float(a)
#         if a%2==0:
#             print(f"The number {a} is even.")
#         elif a%2!=0:
#             print(f"The number {a} is odd.")
#     a = input("Give me a number:  ")

#app02

# sn=10
# counter=0
# while True :
#     a=float(input("enter a number:  "))
#     if a<sn :
#             print("Sorry , you are too small ")
#     else :
#         if a>sn :
#             print("Sorry , you are too big ")
#         elif a== sn :
#             print("Congratulation! , you gess right ")
#             counter += 1
#             break
# print(f"You try {counter} to gess it right")

#app03 :

# l=[]
# pn=4
# while True :
#     if pn>0:
#         a=input("Enter your Web Site Name Without https//   ").strip().lower()
#         l.append(f"https//{a}")
#         pn-=1
#         print(f"The add was successful  {l} and you have   {pn} places in your list")
#     elif pn==0 and len(l)>0:
#         print("The places in the list was done , you have no places")
#         l.sort()
#         print(l)
#         break

#app04 :

# balance=5000
#
# while True :
#     services=input("1-Show the balance \n2-Deposit \n3-Withdraw \n4-exit\n")
#     if services == "1" :
#         print(f"Your Balance is :    {balance} DA")
#     elif services == "2" :
#         Deposit=float(input("Please enter the amount you want to deposit"))
#         if Deposit <= balance:
#             print("The deposit process was successful")
#         elif Deposit > balance or Deposit == 0 or Deposit <= 0:
#             print("The deposit process failed , Please try again")
#     elif services == "3" :
#         Withdraw=float(input("Please enter the amount you want to withdraw"))
#         if Withdraw <= balance:
#             print("The withdrawal process was successful")
#         elif Withdraw > balance or Withdraw == 0 or Withdraw <= 0:
#             print("The withdrawal process failed , Please try again")
#     else :
#         print("You went out")
#         exit()

#app05 :
# total=0
# while True :
#             price = float(input("Please enter the product price "))
#             total+=price
#             if total < 0 :
#                 print("Please enter a valid price , The price never be negative !")
#             elif price == 0:
#                 print("Prices for the items have been entered   ")
#                 promocode = input("Please enter the promocode if you have   ").lower().strip()
#                 if promocode == "save10" :
#                     per10=10/100
#                     total10 = total*per10
#                     print(f"The discount was applied to the total price, and it became  {total10}   DA")
#                     print(f"The original price is:  {total}\n   DA \nThe promocode is:  10%\nThe total price is:    {total10}   DA")
#                     if total10 >= 10000:
#                         total100 = total10 - 100
#                         print(f"A further discount of 100 was applied to the final price, and it became     {total100}  DA")
#                 elif promocode == "save20" :
#                     per20=20/100
#                     total20 = total*per20
#                     print(f"The discount was applied to the total price, and it became {total20}    DA")
#                     print(f"the original price is:  {total}   DA\nThe promocode is:  20%\nThe total price is:    {total20}   DA")
#                     if total20 >= 10000:
#                         total100 = total20 - 100
#                         print(f"A further discount of 100 was applied to the final price, and it became {total100}  DA")
#                 else :
#                     print("We're sorry, the discount code is incorrect, please try again.")
#                 break
