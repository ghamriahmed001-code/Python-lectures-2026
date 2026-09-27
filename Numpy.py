import numpy as np 

# list=[1,2,3,4,5]
# array=np.array(list)

# print(list)     #   [1, 2, 3, 4, 5]
# print(array)    #   [1 2 3 4 5]

# print(type(array))      #   <class 'numpy.ndarray'>

#Array of many Dimensions :

#2D Array :

c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

# print(c)                #[[1 2 3]
#                         #[4 5 6]
#                         #[7 8 9]]

#print(c[0][0])  #   1

#3D Array :

# d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(d)                #  [[[1 2]
                        #  [3 4]]

                        #  [[5 6]
                        #  [7 8]]]

# print(d[1][1][1])    #   8

# print(d[1][1][-1])   #   8


#Number of Dimensions :

# print(c.ndim)   #   2
# print(d.ndim)   #   3

#Custom Dimensions :

# my_array=np.array([1,2,3] , ndmin=3)
# print(my_array)     #           [[[1 2 3]]]
# print(my_array[0])  #           [[[1 2 3]]]
# print(my_array[0][0])   #       [[1 2 3]]
# print(my_array[0][0][0])   #     1

#>>>The array accept one type of Data :

# a=np.array([[3.5,"A",1],["B",5,6.5]])

# print(a)        #       [['1' 'A' '3.5']
#                 #       ['B' '5' '6.5']]
# print(type(a[0][0]))    #   <class 'numpy.str_'>

# b=np.array([[3.5,1],[5,6.5]])

# print(b)        #       [3.5 1.1]
#                 #       [5.1 6.5]]

#Speed Test :
# import time 
# import sys

# #list Speed Test :

# number1=range(15000000)
# number2=range(15000000)
# start_list=time.time()
# list1=[n1+n2 for n1,n2 in zip(number1,number2)]
# # print(list1)
# one=time.time() - start_list
# print(f"list's time is {one}")
# print(sys.getsizeof(list1[55]))

# #Array Speed Test :

# array1=np.arange(15000000)
# array2=np.arange(15000000)
# start_array=time.time()
# array3=array1+array2
# # print(array3)
# two=time.time() - start_array
# print(f"array's time is {two}")
# print(array3.itemsize)

#Arithmatics Operations :

# array1=np.array([[1,2,3],[4,5,6]])
# array2=np.array([1,2,3])
# print(array1 + array2)                                    #[[[ 2  4  6]
#                                                           #  [ 5  7  9]]

#                                                           # [[ 8 10 12]
#                                                           #  [11 13 15]]]

# array1=np.array([[1,2,3],[4,5,6]])
# array2=np.array([[1,2,3],[4,5,6]])
# print(array1 + array2)                                     #[[ 2  4  6]
#                                                            # [ 8 10 12]]

# array1=np.array([[1,2,3],[4,5,6]])
# array2=np.array([[1,2,3]])
# print(array1 + array2)                                      #[[2 4 6]
                                                            # [5 7 9]]


#Data Types and Control Array :

#Shoow Data Types :

# my_array1=np.array([1,2,3])
# my_array2=np.array([1.5,2.3,3.6])
# my_array3=np.array(["A","B","c"])

# print(my_array1.dtype)      #       int64
# print(my_array2.dtype)      #       float64
# print(my_array3.dtype)      #       <U1  :  U : unicode string  , 1 : The max number of characters 
# print(my_array2)

# print("#"*50)

#Change Data Type :

# my_array4=np.array([1,2,3],dtype=float)
# my_array5=np.array([1.5,2.3,3.6],dtype=int)
# my_array6=np.array(["A","B","c"])

# print(my_array4.dtype)
# print(my_array5.dtype)
# print(my_array6.dtype)
# print(my_array1)

# print("#"*50)

# my_array7=np.array([0,2,3])
# my_array8=np.array([1.5,2.3,3.6])
# my_array9=np.array(["A","B","c"])

# my_array7=my_array7.astype(bool)
# my_array8=my_array8.astype(str)
# print(my_array8)        #       ['1.5' '2.3' '3.6']
# print(my_array7)        #       [False  True  True]

# #Capacity :
# my_array10=np.array([1.5,2.3,3.6])

# print(my_array7[2].itemsize)        #       1   Byte
# print(my_array8[2].itemsize)        #       12  Byte
# print(my_array10[2].itemsize)       #       8   Byte

#Array Shape :

# my_array7=np.array([0,2,3,4,5])

# print(my_array7.ndim)   #   1
# print(my_array7.shape)  #   (5,)

# array1=np.array([[1,2,3],[4,5,5]])
# print(array1.ndim)      #   2
# print(array1.shape)     #   (2, 3)

# d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(d.ndim)      #   3
# print(d.shape)     #   (2,2,2)

#Array Rechape :

# array1=np.array([[1,2,3,4],[4,5,6,7]])
# print(array1.shape)
# array1=array1.reshape(4,2)
# print(array1)           #   [[1 2]
#                         #    [3 4]
#                         #    [4 5]
#                         #    [6 7]]

# print(array1.shape)     #   (4, 2)

# array2=np.array([[1,2,3,4],[5,6,7,8]])
# array2=array2.reshape(-1)
# print(array2)           #   [1 2 3 4 5 6 7 8]

# array2=array2.reshape(4,2)
# print(array2)   #   [[1 2]
#                 #    [3 4]
#                 #    [5 6]
#                 #    [7 8]]

# array3=np.array([1,2,3,4,5,6,7,8])
# array3=array3.reshape(2,2,2)  #  [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(array3)
