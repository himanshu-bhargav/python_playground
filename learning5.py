''' This file is for learning purposes only. It is not intended to be used in production. '''

''' A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values. '''
dict1={'course_name': 'Python Programming', 'course_duration': '3 months', 'course_fee': 50000}
# print(dict1)
# print(type(dict1)) 
# print(dict1['course_name'])

# for a in dict1:
#     print(a)   
#     print(dict1[a])

# a=dict1['course_fee']
# print(a)

''' The get() method returns the value of the specified key. If the key does not exist, it returns None.    '''
# a= dict1.get('course_fee')
# print(a)    

# ''' The keys() method returns a view object that displays a list of all the keys in the dictionary. '''
# for a in dict1.keys():
#     print(a)   
#     print(dict1[a])

''' The values() method returns a view object that displays a list of all the values in the dictionary. '''
# for a in dict1.values():
#     print(a)

''' The items() method returns a view object that displays a list of dictionary's key-value tuple pairs. '''
# for a,b in dict1.items():
#     print(a,':', b)
      
''' The pop() method removes the specified key and returns the corresponding value. '''    
# del dict1['course_fee']     
# print(dict1)    

# dict1.update({'course_fee': 40000})
# print(dict1)

# dict1['course_fee']=50000
# print(dict1)    

# dict1.clear()
# print(dict1)   

''' A dictionary can contain another dictionary. This is called a nested dictionary. '''
courses={
    'Python': {'course_name': 'Python Programming', 'course_duration': '3 months', 'course_fee': 50000},
    'Angular': {'course_name': 'Data Science', 'course_duration': '6 months', 'course_fee': 100000},
    'Machine Learning': {'course_name': 'Machine Learning', 'course_duration': '6 months', 'course_fee': 150000},
    'Data Science': {'course_name': 'Data Science', 'course_duration': '6 months', 'course_fee': 100000},
    'Web Development': {'course_name': 'Web Development', 'course_duration': '6 months', 'course_fee': 100000}  
   }

# print(type(courses))
# print(courses)

# print(courses['Python'])
# print(courses['Python']['course_fee'])  
# courses['Python']['course_fee'] = 30000
# print(courses['Python'])  

''' To access the nested dictionary, we can use the keys of the outer dictionary to access the inner dictionary.   '''
# for k,v in courses.items():
#     print(k,':', v) 

''' A tuple is a collection of ordered, immutable, and indexed elements. In Python, tuples are written with round brackets. '''
''' A tuple can contain any number of items, and they can be of different types.   '''
# t1=(10, 20, 30, 40, 50)
# t2=(60, 70, 80, 90, 100)
# print(t1, t2)
# ''' To access the elements of a tuple, we can use indexing. The index starts from 0.   '''
# print(t1[2] + t2[3])


# ''' A tuple can also be created without using parentheses. This is called tuple packing.   '''
# t1=()
# t1=4,
# print(type(t1))
# print(t1)


# t1=(10, 20, 30, 40, 50,20,30,60,70,80,90,100 )
# print(t1.count(20))
# print(t1.index(40))       

# ''' The len() function returns the number of items in a tuple.   '''
# lenght=len(t1)
# print(lenght)   

# ''' To access the elements of a tuple, we can use indexing. The index starts from 0.   '''
# for a in range(lenght):
#     print(a, ':', t1[a])

# ''' The min() function returns the smallest item in a tuple. The max() function returns the largest item in a tuple. The sum() function returns the sum of all items in a tuple.   '''
# print(min(t1))
# print(max(t1))  
# print(sum(t1))  
# print(sum(t1,100))

''' A tuple can also be created without using parentheses. This is called tuple packing.   '''
# data=(1,2,3,4)
# print(type(data))   
# ''' To unpack a tuple, we can use the assignment operator. The number of variables must be equal to the number of items in the tuple.       '''
# a,b,c,d=data
# print(a,b,c,d)      

''' A set is a collection of unordered, mutable, and unindexed elements. In Python, sets are written with curly brackets. A set cannot contain duplicate elements.   '''
s={1,2,3,4,5}
# print(type(s))  
# print(s)
# print(s[0])  # Sets are unindexed, so this will raise an error

''' To add an element to a set, we can use the add() method. To remove an element from a set, we can use the remove() method. To check if an element is in a set, we can use the in keyword.   '''
# for a in s:
#     print(a)     

''' The add() method adds an element to the set. If the element is already present in the set, it will not be added again. The update() method adds multiple elements to the set.   '''
# s.add(6)
# print(s)

# ''' The update() method adds multiple elements to the set. If any of the elements are already present in the set, they will not be added again.   '''
# s.update([6,7,8,9])
# print(s)    

# l1=[10,20,30,40,50]
# s.update(l1)
# print(s)

# print(s.pop())  # The pop() method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
# print(s)    

# #print(s.remove(1000))  # The remove() method removes the specified element from the set. If the element is not present in the set, it raises a KeyError.

# print(s.discard(1000))  # The discard() method removes the specified element from the set. If the element is not present in the set, it does nothing.   

# s1={1,2,3,4,5,[1,2,3]}  # A set cannot contain mutable elements like lists, so this will raise a TypeError   

# print(s1)

# s1={1,2,3,4,5,"hello"}  # A set can contain immutable elements like strings, so this will not raise an error
# print(s1)

# a={10,20,30,40}
# b={30,40,50,60}

# print(a|b)# The union of two sets is a set that contains all the elements of both sets. The union operator is represented by the | symbol.
# print(a&b)# The intersection of two sets is a set that contains only the elements that are present in both sets. The intersection operator is represented by the & symbol.
# print(a-b) # The difference of two sets is a set that contains only the elements that are present in the first set but not in the second set. The difference operator is represented by the - symbol.
# print(a^b) # The symmetric difference of two sets is a set that contains only the elements that are present in either set but not in both sets. The symmetric difference operator is represented by the ^ symbol.

''' A function is a block of code that performs a specific task. In Python, functions are defined using the def keyword. A function can take arguments and return a value.   '''
def show():
    print('Hello World')    
    print('Welcome to Python Programming')  

# # show()  # To call a function, we can use the function name followed by parentheses. If the function takes arguments, we can pass the arguments inside the parentheses.    
# show()

''' A function can take arguments. Arguments are the values that we pass to a function when we call it. We can define a function with parameters, which are the variables that we use to accept the arguments.   '''
# def sum(num1,num2)  :
#     print(num1+num2)

# a=10
# b=20
# sum(a,b)

# sum(100,200)

# def add(a,b):
#     return a+b

# result=add(40,50)
# print(result)


# def sum(num1,num2=40)  :
#     print(num1+num2)

# sum(50)
# sum(50,100)

''' A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. The syntax of a lambda function is: lambda arguments: expression. Lambda functions are often used as a shortcut for defining simple functions.   '''
# add=lambda a,b: a+b
# result=add(10,20)     

# print(result)  

# ''' A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. The syntax of a lambda function is: lambda arguments: expression. Lambda functions are often used as a shortcut for defining simple functions.   '''
# square=lambda x: x*x
# print(square(5))            

# ''' A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. The syntax of a lambda function is: lambda arguments: expression. Lambda functions are often used as a shortcut for defining simple functions.   '''
# show=lambda: print('Hello World')  
# show()  

''' The map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). The syntax of the map() function is: map(function, iterable).   '''
nums=[1,2,3,4]
result=list(map(lambda x:x*2,nums))
print(result)

