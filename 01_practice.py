# conversion of list into the array
# l=[]
# for i in range(1,6):
#     a=input("Enter the value")
#     l.append(a) 
# print(l) 

# Q.2 
# import numpy as np
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr) 

# Q.3 

# import numpy as np

# # Create a 2D array
# a = np.array([[1, 2], [3, 4]])

# # Multiply every element by 2
# b = a * 2

# print(b)

# Q.4 

# import numpy as np

# my_list = [10, 20, 30]           # square brackets → list
# my_tuple = (1, 2)                # round brackets → tuple
# my_dict = {"x": 100, "y": 200}   # curly braces → dictionary
# my_array = np.array(my_list)    # use () to call function, pass list []

# print(my_array[1])              # Access element with [] 

# Q.5 

# for i in range(1, 1001, 100):
#     l = list(range(i))
#     t = tuple(range(i))
#     print(f"{i} items → List: {sys.getsizeof(l)} bytes | Tuple: {sys.getsizeof(t)} bytes") 

# Q.6 

# a = [1, 2]
# a.append([3, 4])   # Adds the whole list as one item
# # a becomes [1, 2, [3, 4]]

# b = [1, 2]
# b.extend([3, 4])   # Adds items individually
# # b becomes [1, 2, 3, 4]

# Q.7 
# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr.dtype) 

# Q.8 

# # Identical to the above
# arr=np.array([1+2j,3-4j],dtype='c8')
# arr.dtype 

# Q.9 

# import numpy as np
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr) 
# print(arr[arr>5])
# print(arr[arr%2==0])
#print(arr[(arr>2) & (arr<8) & (arr%2==0)])

Q.10 

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.concatenate((arr1,arr2),dtype="float32")
arr3
