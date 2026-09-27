#print(2==5) #bool >>> #boolean
#print({"one":1,"two":2,"three":3}) dict >>> #dictionary
#variabels:
#you can do this :
#--------------------------------------------------------
#a,b,c=1,12,3
#print(a,b,c)
#Run :          1 12 3
#--------------------------------------------------------
#escape sequences characters :
#1-back space : --------------
#\b          >>> remove the last latter before \
#print("hello wo\bld") >>> remove latter o from >>> world
#Run :          hello  wld
#---------------------------------------------------------
#`2-escape back slash + \ : -----------
#print("i need ti add a back slash \\ " )  >>> if you need to put a back slash
# , just add another back slash behaind it .
#3-line feed :
#print("hello\nworld") >>> it put the world in a line and the
# another world in another line and it use only with str
#Run:            hello
#                world
#4-carriage return :
#print("1234567\rahmed") >>> it replace the first five numbers
# or elements by ahmed because ahmes has five elements (a.h.m.e.d)
#Run :            ahmed67
#5-horizontal tab :
#print("hello\tworld") >>> it do a TAP between the elements
#6-drop the sentes down :
#myvariable="""ahmed
#is
# the
#  goat"""
#print(myvariable)
#Run:
#ahmed
#is
#  the
#  goat
#------------------------------------------------------------
#cosatenation : its a method to link  strings together to have a long string
#gega="ahmed is the "
#alpha="GOAT ."
#print(gega + alpha)
#ahmed is the GOAT .
#print(gega + "\n" + alpha)
#Run :           #ahmed is the
#GOAT .
#-------------------------------------------------------------------
#a method to highligh a sentence
#myvriable="ahmed is the 'goat'"
#myvriable001='ahmed is the "goat"'
#myvariable002=""" 'ahmed'
#       "is the  goat" """
#print(myvariable002)
#print(myvriable)
#print(myvriable001)
#Run:
#ahmed is the 'goat'
#ahmed is the "goat"
#myvariable=""" ahmed
#'is' the \
#"goat" """
#print(myvariable)
#Run:
#'is' the  "goat" >>> \ <<< it rise up the word >goat< upper line
#myvariable=""" ahmed
#'is' the \\
# "goat" """
#print(myvariable)
#Run:
#'is' the \
#"goat"
#---------------------------------------------------------------------
#index number :0 1 2 3 4 5 6 7 8 9 10 11  12
#myv="ahmed study eng"
#print(myv[0])
#print(myv[0:5:1])
#print(myv[-1])
#print(myv[-2])
#print(myv[:2])
#print(myv[:])
#print(myv[:15])
#print(myv[0::1])
#print(myv[::1])
#print(myv[1::1])
#print(myv[::])
#print(myv[::2])
#print(myv[::3])
#Run:
#a
#ahmed
#g
#n
#ah
#ahmed study eng
#ahmed study eng
#ahmed study eng
#ahmed study eng
#hmed study eng
#ahmed study eng
#amdsuyeg
#aesde
#--------------------------------------------------------------------
# Strings Methods:
#len : is amethos that copute the number of elements . example :
#m="12345668"
#print(len(m))
#strip: to removethe right and left spaces
#rstrip: to removethe right space
#lstrip: to removethe left space
#example:
#myv="           ahmed is the goat           "
#print(myv.strip())
#print(myv.rstrip())
#print(myv.lstrip())
#Run:
#ahmed is the goat
#          ahmed is the goat
#ahmed is the goat
#----------------------------------------------------------------------
#split() >>> it take you data and transfet it as a >list<
#based on the spaces or the what you chose inter the >()<
#example01:
#myv="1 2 3 4"
#print(myv.split())
#Run:
#['1', '2', '3', '4']
#example02:
#myv="1 2 3 4"
#print(myv.split("."))
#Run:
#['1 2 3 4']
#exmaple003:
#myv="1234"
#print(myv.split()) or print(myv.split("."))
#Run:
#['1234']
#exmaple004:
#myv="ahmed-is-the-goat-of-sure"
#print(myv.split("-"))
#print(myv.split("-",4))
#run :
#['ahmed', 'is', 'the', 'goat', 'of', 'sure']
#['ahmed', 'is', 'the', 'goat', 'of-sure']
#myv="ahmed*is*the*goat*of*sure"
#print(myv.rsplit("*"))
#print(myv.rsplit("*",3))
#run:
#['ahmed', 'is', 'the', 'goat', 'of', 'sure']
#['ahmed*is*the', 'goat', 'of', 'sure']
#---------------------------------------------------
#center: used to do same modification on strings
#myv="ahmed"
#print(myv.center(7,"*"))
#run:
#*ahmed*
#------------------------------------------------------------------------
#count: it count or calculate how many times this word are repeated
#myv="ahmed is the goat because he is study engineering"
#print(myv.count("i"))
#print(myv.count("i",0,31))
#---------------------------------------------------------------------------
#swapcase: swape a capetal latter by small latter and the opposite is ture
#myv001="HI IM AHMED"
#myv002="hi im ahmed"
#myv003="Hi Im AhMeD"
#print(myv001.swapcase())
#print(myv002.swapcase())
#print(myv003.swapcase())
#run:
#hi im ahmed
#HI IM AHMED
#hI iM aHmEd
#------------------------------------------------------------------------------
#starstwith() : it test if it is the fist (starts with it)  or no
#myv="hi im ahmed"
#print(myv.startswith("i"))
#print(myv.startswith("m",4,11))
#------------------------------------------------------------------------------
#endswith() : it test if it is the last (ends with it )  or no
#myv="hi im ahmed"
#print(myv.endswith("d"))
#print(myv.endswith("m",0,5))
#-------------------------------------------------------------------------------
#index("substring",start,end)
#myv="i love programming"
#print(myv.index("e"))
#print(myv.index("i",0,5))
#--------------------------------------------------------------------------------
#find'"substring", start , end )
#print(myv.find("p",0,6)) >>> if he did't find the subsentex he print -1 not eror like idex
#myv1="I Love Python 3B"
#print(myv1.istitle())
#myv2="i iove iython 3b"
#print(myv2.islower())
#myv3=" "
#print(myv3.isspace())
#myv4="I\tLove\tPython\t3B"
#print(myv4.expandtabs(2))
#myv5="I\nLove\nPython\n3B"
#---------------------------------------------------------------------------------------
#print(myv5.splitlines())
#replace(old,new,count)
#myv="I Love Python and I Love C++"
#print(myv.replace("Love", "hete",1))
#---------------------------------------------------------------------------------------
#join >>> make the elements string and separated the elements fron each
#myv=["ahmed" , "ali" , "abdo" ]
#print(" ".join(myv))
#print("#".join(myv))
#--------------------------------------------------------------------------------------
#String Formating the old way :
#First thing you should know is you can only concatenate str not str and int/flout
#name="Ahmed"
#birthdat=2332008
#myage=18
#print("hi my is :" +myage)
#Run :
#TypeError: can only concatenate str (not "int") to str
#We use placeholde
#name="Ahmed"
#birthday=23032008
#myage=18
#print("hi im %s"%name ,"and my birthday is %d"%birthday , "and my age is %d:"%myage)(%s,%d,%d)
#print("hi im: %s and my birthday is: %d and my age is: %d"%(name,birthday,myage))
#Run:
#hi im: Ahmed and my birthday is: 23032008 and my age is: 18
#name="Ahmed"
#birthday=23032008
#my_total_average=16.95
#print("hi im: %s and my birthday is: %d and my total average is: %f"%(name,birthday,my_total_average))
#Run:
#hi im: Ahmed and my birthday is: 23032008 and my total average is: 16.950000
#name="Ahmed"
#birthday=23032008
#my_total_average=16.95
#print("hi im: %s and my birthday is: %d and my total average is: %.2f"%(name,birthday,my_total_average))
#Run: you can control the numbers after the point
#hi im: Ahmed and my birthday is: 23032008 and my total average is: 16.95
#--> truncate string : The placeholder
#print("hellow my name is : %s"%"ahmed")
#myv="Ahmed is the GOAT"
#print("im ahmed and %.5s" %(myv))
#Run :
#im ahmed and Ahmed >>> it mean yiu stop in index number 5(0.1.2.3.4)
#my_name ="ahmed abdo"
#my_age=18.5555454141475869
#my_domain= "EE"
#print("my name is %.5s and my age is %.6f , and my domain is %.1s"%(my_name,my_age,my_domain))
#----------------------------------------------------------------------------------------
#String Formating the new ways :
#print("hi my name is {}" .format("ahmed"))
#my_name="ahmed abd alkader"
#my_family_name="ghamri"
#my_age1=18
#my_age2=18.54415987446
#my_domain="EE"
#print("hi there , my name is {:s} , my age is {:d} , my family name is {:s}".format(my_name,my_age2,my_family_name))
#print("hi there , my name is {:.5s} , my age is {:.4f} , my family name is {:s}".format(my_name,my_age1,my_family_name))
#Run:
#hi there , my name is ahmed abd alkader , my age is 18 , my family name is ghamri
#hi there , my name is ahmed , my age is 18.6560 , my family name is ghamri
#formating edits :
#myv1=2008201820222025
#print("my money in bank is {:d}".format(myv1)) #>>>print : 2008201820222025
#print("my money in bank is {:_d}".format(myv1)) #>>>print : 2_008_201_820_222_025
#print("my money in bank is {:,d}".format(myv1)) #>>>print : 2,008,201,820,222,025
#a,b,c = "One" , "Two" , "Three"
#print("{} {} {} free algeria".format(a,b,c)) #>>> One Two Three free algeria
#print("{2} {1} {0} free algeria".format(a,b,c)) #>>> Three Two One free algeria
#print("{2} {0} {0} free algeria".format(a,b,c)) #>>> Three One One free algeria
#x,y,z=10 , 20 , 30
#print("my index is {0:.2f} {1:.3f} {2:.3f}".format(x,y,z))   #>>> my index is 10.00 20.000 30.000
#print("my index is {0:f} {1:f} {2:f}".format(x,y,z)) #>>> my index is 10.000000 20.000000 30.000000
#formating version 3.6+ :
#myv1="ahmed"
#myv2=18
#print("hi , my name is : {myv1} and my ge is : {myv2}")  #>>>   hi , my name is : {myv1} and my ge is : {myv2}
#print(f"hi , my name is : {myv1} and my ge is : {myv2}")  # >>>     hi , my name is : ahmed and my ge is : 18
#---------------------------------------------------------------------------------------------------
#Complex numbers :
# mycomlexnumber = 5+6j
# print(mycomlexnumber) #>>> (5+6j)
# print(type(mycomlexnumber))  #>>>   <class 'complex'>
#you can convert int to float and coplex :
#print(float(100)) #>>> int to float :  100.0
#print(int(100.67))  #   >>>  float to int :  100
#print(complex(100))  # >>>   int to complex    (100+0j)
#print(complex(100.6767))    # float to complex :    (100.6767+0j)
##you can't convert complex to int and float :
#print(int(100+67j))        #>>> TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(float(100+67j))      #>>> TypeError: float() argument must be a string or a real number, not 'complex'
#--------------------------------------------------------------------------------------------------------
#Lists :

# l=[2008,"ahmed",1,16.95,True]
# d[1]=67
# print(d)
# print(l)            #>>>    l=[2008,"ahmed",1,16.95,True]
# print(type(l[0]))         #>>>    2008
# print(l[1])         #>>>    ahmed
# print(l[-1])        #>>>    True
# print(l[-5])        #>>>    ahmed
# print(l[0:2])       #>>>    [2008, 'ahmed']
# print(l[0:3])       #>>>    [2008, 'ahmed', 1]
# print(l[0:5])       #>>>    [2008, 'ahmed', 1, 16.95, True]
# print(type(l[0]))   #>>>    <class 'int'>

# l=[1,2,3,4,5,6]
# print(*l)

#run :

# 1
# 2
# 3
# 4
# 5
# 6

#>>>append :

# l1=[2008,"ahmed",1,16.95,True]
# l1.append("osama")
# l1.append(18)
# l1.append(67.67)
# print(l1) #     [2008, 'ahmed', 1, 16.95, True, 'osama', 18, 67.67]
# l2=[2006,"mohmed ali",67,17.50]
# l1.append(l2)
# print(l1)       #>>>   [2008, 'ahmed', 1, 16.95, True, 'osama', 18, 67.67, [2006, 'mohmed ali', 67, 17.50]]
# print(l1[8])        #>>>        [2006, 'mohmed ali', 67, 17.5]
# print(l1[8][1])     #>>>         mohmed ali

#>>>extend() :

# l1=[2008,"ahmed",1,16.95,True]
# l2=[2006,"mohamed ali",67,17.50]
# l1.extend(l1)
# print(l1)    #   >>>  [2008, 'ahmed', 1, 16.95, True, 2008, 'ahmed', 1, 16.95, True]

#>>>sort() :

# l1=[1,5654,565187,231286498,231664,611]
# l2=["l","a","m","h","f","g"]
# l3=[2008,67,"ahmed",18]
# l1.sort()
# l1.sort(reverse=False)
# print(l1)       #     >>>    [1, 611, 5654, 231664, 565187, 231286498]
# print(l1)       #     >>>    [1, 611, 5654, 231664, 565187, 231286498]
# l1.sort(reverse=True)
# print(l1)                     #>>>      [231286498, 565187, 231664, 5654, 611, 1]
# l2.sort()
# print(l2)                     #>>>      ['a', 'f', 'g', 'h', 'l', 'm']
# l2=sort(reverse=False)
# print(l2)                     #>>>      ['a', 'f', 'g', 'h', 'l', 'm']
# l2.sort(reverse=True)
# print(l2)                     #>>>      ['m', 'l', 'h', 'g', 'f', 'a']

#>>>reverse() :

# l1=[1,2,3,"ahmed",120.22]
# l1.reverse()
# print(l1)    #>>>    [120.22, 'ahmed', 3, 2, 1]

#>>>clear :

# l=[1,2,3,45.25,67,21]
# l.clear()
# print(l)     #       >>>     []

#>>>count :
#
# d=[1,2,9,6,9,45,45,5,6,5]
# print(d.count(5))             #>>>        2

#>>>index:

# d=[1,2,9,6,9,45,45,5,6,5]
# print(d.index(6))     #  >>>         3

#>>>insert:

# d=[1,2,9,6,9,45,45,5,6,5]
# d.insert(0,12)
# print(d)        #       [12, 1, 2, 9, 6, 9, 45, 45, 5, 6, 5]
# d.insert(3,16)
# print(d)        #       [12, 1, 2, 16, 9, 6, 9, 45, 45, 5, 6, 5]
# d.insert(-1,67)
# print(d)        #       [12, 1, 2, 16, 9, 6, 9, 45, 45, 5, 6, 67, 5]
# d.insert(-2,100)
# print(d)        #       [12, 1, 2, 16, 9, 6, 9, 45, 45, 5, 6, 100, 67, 5]

#>>>pop()

# d=[1,2,9,6,9,45,45,5,6,5]
# d.pop(4)
# print(d)          #       [1, 2, 9, 6, 45, 45, 5, 6, 5]

#set :

#>>>sets is not ordered and indexed :
#>>>sets elements is must be unique :
# set1={"ahmed","osama",67}
# print(set1)         #       {'ahmed', 67, 'osama'}
# print(set1)         #       {'osama', 67, 'ahmed'}
# print(set1)         #       {67, 'osama', 'ahmed'}
# print(set1[0])      #       TypeError: 'set' object is not subscriptable

#>>>union :

# a={"ahmed",67,2008,"EE"}
# b={"abdo",100,1998,"ME"}
# print(a | b)        #>>>        {67, 'ahmed', 100, 1998, 'EE', 'abdo', 2008, 'ME'}
# print(a.union(b))       #>>>       {67, 'ahmed', 100, 1998, 'EE', 'abdo', 2008, 'ME'}

#>>>copy :

# a={"ahmed",67,2008,"EE"}
# f=a.copy()
# print(f)        #       {2008, 67, 'ahmed', 'EE'}
#
# #remove:
#
# a={"ahmed",67,2008,"EE"}
# a.remove(67)
# print(a)        #       {2008, 'ahmed', 'EE'}

#>>>pop() :         show you a random element

# a={"ahmed",67,2008,"EE",100}
# print(a.pop())          #       2008
# print(a.pop())          #       100
# print(a.pop())          #       67

#>>>update :

# a={"ahmed",67,2008,"EE",100}
# b={"GGG","abdo",2006,"c++"}
# a.update(["html","Css"])
# print(a)            #       {67, 100, 'ahmed', 2008, 'Css', 'html', 'EE'}
# a.update(b)
# print(a)            #       {67, 100, 'Css', 'GGG', 'ahmed', 'html', 2006, 'c++', 2008, 'EE', 'abdo'}

#>>>difference:

# a={1,2,3,4}
# b={1,2,"hamada","ME",1990}
# print(a.difference(b))          #>>>        {3, 4}
# print(a-b)                      #>>>        {3, 4}
# print(b.difference(a))          #>>>        {'hamada', 'ME', 1990}
# print(b-a)                      #>>>        {'hamada', 'ME', 1990}

#>>>difference_update :

# a={1,2,3,4}
# b={1,2,"hamada","ME",1990}
# a.difference_update(b)
# print(a)
# b.difference_update(a)
# print(b)

#>>>intersection :

# e={1,2,3,67,"ahmed"}
# f={100,67,500,"oss",2}
# print(e)
# print(e.intersection(f))        #       {2, 67}
# print(e & f)                      #       {2, 67}
# print(e)

#>>>intersection_update :

# e={1,2,3,67,"ahmed"}
# f={100,67,500,"oss",2}
# # print(e)
# e.intersection_update(f)          #       {2, 67}
# print(e)                          #       {2, 67}

#>>>symmetric_difference :

# e={1,2,3,67,"ahmed"}
# f={100,67,500,"oss",2}
# print(e.symmetric_difference(f))            #       {1, 3, 100, 500, 'ahmed', 'oss'}
# print(e ^ f)                                #       {1, 'oss', 3, 100, 500, 'ahmed'}

#>>>symmetric_difference_update :

# e={1,2,3,67,"ahmed"}
# f={100,67,500,"oss",2}
# e.symmetric_difference_update(f)
# print(e)                                      #       {1, 3, 'ahmed', 100, 500, 'oss'}

#>>>issuperset :

# a={1,2,3,"hamed","oss"}
# b={2,3,"hamed"}
# c= {1, 2, 1268, 25, "yoyo"}
# print(a.issuperset(b))                          #       True
# print(a.issuperset(c))                          #       False
