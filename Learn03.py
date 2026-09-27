#app05 :

# gess=5
# password="ahmed@ghamri"
# while True :
#     password1=input(f"Enter your password , You have {gess} attempts  :  ")
#     if password1==password:
#         print("Password match")
#         break
#     elif password1!=password :
#         print("Password not match")
#         gess -= 1
#         if gess == 0 :
#             print("\nYour attempts are finished, Try again after One minute ")
#             break

#for loop :

#app01 :

# l2=[]
# l=[1,2,3,4,5,6,7,8,9,10]
# for number in l:
#     number+=1
#     l2.append(number)
#     print(number)
#     if number % 2 == 0 :
#         print(f"The number : {number} is Even")
#     elif number % 2 != 0 :
#         print(f"The number : {number} is Odd")
# print(f"\nThe lis is :       {l2}")

#app02 :

# text="python programming is awesome"
# n=0
# l=[]
# for cher in text :
#     if cher == "a" in text or cher == "e" in text or cher == "i" in text or cher == "o" in text or cher == "u" in text:
#         n += 1
#         if cher not in l :
#             l.append(cher)
# print(n)
# print(l)

# >>>another solution :

# text = "python programming is awesome"
# n = 0
# l = []
#
# for cher in text:
#     # 1. تبسيط الشرط باستعمال in
#     if cher in "aeiou":
#         n += 1  # يحسب العدد الإجمالي للحروف
#
#         # 2. إضافة الحرف فقط إذا لم يكن موجوداً من قبل
#         if cher not in l:
#             l.append(cher)
#
# print(f"العدد الإجمالي للحروف المتحركة: {n}")
# print(f"الحروف بدون تكرار: {l}")

#app02 :

# grades = [14.5, 8.0, 9.5, 17.0, 5.5, 10.0, 18.5, 19.0]
# s=[]
# l=[]
# for note in grades :
#     if note >= 10 :
#         note = note + 1.5
#         g=note-20
#         if note >=10 and note <= 20:
#             s.append(note)
#         elif note>20  :
#             note = note - g
#             s.append(note)
#     elif note < 10  :
#         l.append(note)
# total1=0
# for note in s :
#     total1+=note
#     average_s=total1/len(s)
# print(f"Grades of students who passed the exam :    {s}     The Pass average is :    {average_s}{"/"}{len(grades)}")
# total2=0
# for note in l :
#     total2+=note
#     average_l=total2/len(l)
# print(f"Grades of students who failed the exam :    {l}     The Failure average is :    {average_l}{"/"}{len(l)}")

#app03 :

# my_dict={
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
# }
# for keys in my_dict:
#     print(f"my later is : {keys} and my number is : {my_dict[keys]}")

#app04 :

# names=["Ahmed","Ali","Omar","Sami"]
# skills=["Html","JS","CSS","Python"]
# for name in names :             #Outer loop : اللوب الرىيسي
#         print(f"Hi im : {name} and my skills is :")
#         for skill in skills:    #Inner loop : اللوب الفرعي ينطبق على كل عنصر على حدا في اللوب الاصلي
#             print(skill)

#app05 :

# people = {
#     "ahmed": {
#         "html":(f"{90} %")
#     },
#     "kamal": {
#         "css": (f"{80} %")
#
#     },
#     "imad": {
#         "c++":(f"{70} %")
#     },
#     "pop": {
#         "python": (f"{60} %")
#     },
# }
# for name in people:
#     for lang in people[name] :
#         print(f"Name : {name} The language {lang} and score {people[name][lang]}")

#>>>Different ways to print list or tuple elements :

# l=[1,2,3,4,5,6,7,8,9,10]
# for number in l :
#     print(number)
# for index in range (len(l)):
#     print(l[index])

#continue :

# l=[1,2,3,4,5,6,7,8,9,10]
# for number in l :
#     if number==6:
#         continue              #               تجاهل الامر 
#     print(number)
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9
# 10

# l=[1,2,3,4,5,6,7,8,9,10]
# for number in l :
#     print(number)
#     if number==6:
#         break

# """ l=[1,2,3,4,5,6,7,8,9,10]
# for number in l :
#     if number==6:
#         pass                  #               كناك تقله عادي
#     print(number) """
# #advanced dictionary loop :
# """ my_skills={

#         "html":90,
#         "css":80,
#         "python":70,
#         "c++":60,
# }
# for skill,score in my_skills.items() :
#     print(f"My skill is : {skill} and my score is : {score}")

# for skill in my_skills :
#     print(f"My skill is : {skill} and my score is : {my_skills[skill]}") """

# my_skills={

#         "skill01":{
#             "html": (f'90{"%"}')
#         },
#         "skill02":{
#             "css": (f'80{"%"}')
#         },
#         "skill03":{
#             "JS": (f'70{"%"}')
#         },
#         "skill04":{
#             "C++": (f'60{"%"}')
#         },
# }
# for skill in my_skills :
#     for language,score in my_skills[skill].items() :
#         print(f"My {skill} is : {language} and my score is : {score}")
# print("_"*100)
# """ for skill in my_skills :
#     for language in my_skills[skill] :
#         print(f"My {skill} is {language} and my score is {my_skills[skill][language]}")  """

# for skill,detail in my_skills.items():
#     for language,score in my_skills[skill].items():
#         print(f"My {skill} is : {language} and my score is : {score}")


#Functions :


# def ahmed() :
#     print("Hi !")
#     return(55)
# print(ahmed()+1)


# def hello_name(name) :
#     print(f"Hello {name}")
# print(hello_name("ahmed"))
# print(hello_name("osama"))


# l=["ahmed","ali","omar","sami"]
# def Hello_name() :
#     for name in l :
#         print(f"Hello {name}")
# Hello_name()


# def name (family_name,fierst_name,last_name) :
#     print(f"Hello {family_name.capitalize():.2} {fierst_name.capitalize()} {last_name.capitalize()}")
# name("ghamri","ahmed","abdalkader")



# def addition(n1,n2):  
#         if type(n1)==float or type(n1)==int and type(n2)==float or type(n2)==int :
#             print(n1+n2)
#         elif type(n1)!=float or type(n1)!=int and type(n2)!=float or type(n2)!=int:
#             print("Can sum only int to int")
#         else :
#             print("Error , Sorry try again")

# addition(10.56545,20)

# def Hello_people(*peoples_name):
#     for name in peoples_name :
#         print(f"Hello {name}")
# Hello_people("ahemd",2,"qacem",3.25,3+5j)


# def details(name,*skills):
#     print(f"Hello {name} your skill is : ")
#     for skill in skills :
#         print(skill)
# details("omar","html","python")

# #run :

# # Hello omar your skill is : 
# # html
# # python


# def details(name,*skills):
#     print(f"Hello {name} your skills is : {skills}")
#     print(f"{type(skills)}")
# details("omar","html","python")

# #run :

# # Hello omar your skills is : ('html', 'python')


# def data(name,age="unknown",country="unknown")         #       if you dont write the argument then he write unknown , it's defined as a defualt parameter .
#     print(f"Hello my name is {name} and my age is {age} and my {country}")

# data("ahmed",18,"algeria")      #       Hello my name is ahmed and my age is 18 and my algeria
# data("ahmed")                   #       Hello my name is ahmed and my age is unknown and my unknown

# def data(country,age="unknown",name):       #       the defualt parameter it's must be the last parameter .      
#     print(f"Hello my name is {name} and my age is {age} and my {country}")


# def eng(**module):
#     print(type(module))       #      <class 'dict'>
#     for module_name,coffesion in module.items() :         #       for key,value in parameter.items()
#         if isinstance(coffesion,int) :
#             print(f"The module is {module_name} and the coffesion is :  {coffesion}")
#         else :
#             print("Sorry , wrong data input")
#     print(type(module_name))
#     print(type(coffesion))
# eng(analysis=3,algabra=2,chimestry=4)


# my_dict={

#         "html":(f"{90}%"),
#         "css":(f"{80}%"),
#         "python":(f"{70}%"),
#         "c++":(f"{60}%"),
# }

# def my_skills(**my_dict):
#     for language,score in my_dict.items() :
#         print(f"The language i know is : {language} and my score is : {score} .")
# my_skills(**my_dict)


#recursion function :


# def mines(n):
#     if n == 1 :
#         return(1)
#     return(n + mines(n-1))
# print(mines(5))


# def count_down(n):
#     # إذا وصلنا إلى 1، يتوقف السؤال ونرجع 1 فوراً (مثل الشخص الأول في الصف)
#     if n == 1:
#         return 1

#     # وإلا: احسب رقمك الحالي + ناتج الدالة للرقم الذي قبلك
#     return n + count_down(n - 1)
    
# print(count_down(5))  # الناتج: 6


# def factorial(n) :
#     if n==1 :
#         return(1)
#     return (n*factorial(n-1))
# print(factorial(3))


# def clear_word(word):       #         vvoodd   >>>     vod

#     if word==word[0] :
        
#         print(word)

#         return word
        
#     elif word[0]==word[1] :

#         print(word)

#         return (clear_word(word[1:]))

#     elif word[0]!=word[1] :

#         print(word)

#         return (word[0]+clear_word(word[1:]))  

# print(clear_word("ahmed"))


# def power_of(number,power):
#     return number**power
# print(power_of(2,7))


# def power_of(n,p):
#     if p==0 :
#         return (1)
#     return (n*power_of(n,p-1))
# print(power_of(2,3))


# def sum_list(l=[]) :
#     if len(l)==1 :
#         return(l[0])
#     return l[0]+sum_list(l[1:])
# print(sum_list(l=[1,2,3,4]))


# def reverse(word) :         #       ahmed      >>>     demha
#     if len(word)==1 :
#         return word
#     return word[-1]+reverse(word[:len(word)-1])         #       d
# print(reverse("ahmed"))


# def repeating_counting(w,c):
#     n=0
#     if c != w and len(c)==len(w):
#         return 0
#     elif c==w :
#         return 1
#     elif c == w[0] :
#         n+=1
#         return n+repeating_counting(w[1:],c)
#     elif c != w[0] :
#         return repeating_counting(w[1:],c)
# print(f"The reaprting number is :   {repeating_counting("hhhjjjkkjjmmm","j")}")



#>>> My code :


# def special_word(word):             #           radar 
#     if len(word)==1 or len(word)==0 :
#         return True 
#     elif word[0]==word[len(word)-1] :
#         return True==True+special_word(word[1:len(word)-1])
#     elif word[0]!=word[len(word)-1] :
#         return False
# print(special_word("hhchh"))


#>>> The correct code :


# def special_word(word):
#     if len(word) == 1 or len(word) == 0:
#         return True 
#     elif word[0] == word[-1]:
#         return special_word(word[1:-1])    
#     else:
#         return False
# print(special_word("radar"))  # True
# print(special_word("htmh"))   # False


#lambda function :


# hello= lambda name : f"Hello {name}"
# print(hello("ahmed"))


#file handiling :

# import os
# print("="*50)
# print(os.getcwd())      #       C:\Users\GIGABYTE\OneDrive\Desktop\Learn_Python
# # print("="*50)
# # file=open("ahmed.txt","r")
# print("="*50)
# print(os.path.abspath(__file__))        #       c:\Users\GIGABYTE\OneDrive\Desktop\Learn_Python\Learn.py
# print("="*50)
# print(os.path.dirname(os.path.abspath(__file__)))
# print("="*50)
# os.chdir(r"C:\Users\GIGABYTE\OneDrive\Documents\hamada")
# print(os.getcwd())      #       C:\Users\GIGABYTE\OneDrive\Documents\hamada


#>>>Read Files :


# myfile=open(r"C:\Users\GIGABYTE\OneDrive\Desktop\Learn_Python\kader.txt","r")
# print(myfile)       #         give the data about the file    <_io.TextIOWrapper name='C:\\Users\\GIGABYTE\\OneDrive\\Desktop\\Learn_Python\\kader.txt' mode='r' encoding='cp1256'>
# print(myfile.name)      #       he give the abspath :   C:\Users\GIGABYTE\OneDrive\Desktop\Learn_Python\kader.txt
# print(myfile.mode)      #       r
# print(myfile.encoding)      #       cp1256

# print(myfile.read())        #       Hi ! my name is :
                              #       Ahmed Abd Alkader
# print(myfile.readline())


import os
# file=open("dodi.txt","r")
# file=print(file.read())
# file=open("dodi.txt","w")
# file.write(";;;")
# file=open("dodi.txt","r")
# file=print(file.read())


# file=open("dodi.txt","a")
# file=print(file.write("yes\n")) 
# file=open("dodi.txt","a")
# file=print(file.write("ma bro\n"))


# file=open("dodi.txt","a")
# file.truncate(5)        #        it svae the first five characters and remove the else
# file=open("dodi.txt","r")
# file.seek(7)
# print(file.read())
# os.remove("dodi.txt")
