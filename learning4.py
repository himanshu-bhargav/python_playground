''' This file is for learning purposes only. It is not intended to be used in production. '''

''' The find() method returns the lowest index of the substring if it is found in the given string. If it is not found then it returns -1. The index() method is similar to find() but raises a ValueError if the substring is not found.   '''
# string1= "Python is a great programming language."

# print(string1.find('o')) # find the first occurrence of 'o'
# print(string1.find('o',5)) # find the first occurrence of 'o' starting from index 5
# print(string1.find('great')) # find the first occurrence of 'great'

# print(string1.index('o',2)) # find the first occurrence of 'o' starting from index 2

# string1= "Python123"
# print(string1.isalpha()) # check if all characters in the string are alphabetic
# print(string1.isdigit()) # check if all characters in the string are digits     
# print(string1.isnumeric()) # check if all characters in the string are numeric
# print(string1.isalnum()) # check if all characters in the string are alphanumeric   

''' String formatting is the process of formatting a string by replacing placeholders with values. There are several ways to format a string in Python, including using the format() method, f-strings, and the % operator.   '''
# name="Himanshu Bhargav"
# age=40
# print(name)
# print('My name is ' + name  + ' and I stay in India.')
# print('My name is {} and I stay in {}.'.format(name,'India')) # using format() method to format the string
# print(f'My name is {name} and I stay in India.') # using f-string to format the string      
# print('My name is %s and I stay in %s.' % (name,'India')) # using % operator to format the string   
# print("My name is {0} and I stay in {1}.".format(name,'India')) # using format() method with positional arguments to format the string
# print("My name is {name} and I stay in {country}.".format(name=name, country='India')) # using format() method with keyword arguments to format the string      
# print("My name is {name:20} and I stay in {country}.".format(name=name, country='India')) # using format() method with keyword arguments to format the string      
# print("My name is {name:>20} and I stay in {country}.".format(name=name, country='India')) # using format() method with keyword arguments to format the string      
# print("My name is {name:<20} and I stay in {country}.".format(name=name, country='India')) # using format() method with keyword arguments to format the string      

''' Lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [] and can contain elements of different data types.   ''' 
# list1 = [1, 2, 3, 4, 5,'a','b','c','d','e',[6, 7, 8, 9, 10]]
# print(list1) 
# print(type(list1))
# print(list1[0],list1[10]) # access the first element of the list

# print(list1[0:5]) # access the first 5 elements of the list
# print(list1[5:10]) # access the last 5 elements of the list     
# print(list1[0::2]) # access every second element of the list
# print(list1[1::2]) # access every second element of the list starting from index 1
# print(list1[-1]) # access the last element of the list
# print(list1[-1::-1]) # access the list in reverse order

# list2=[1,20,30,40,50]
# print(list2)    
# lenth=len(list2) # get the length of the list
# print(lenth)

# ''' The for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The syntax of a for loop is as follows:'''
# for i in range(lenth):
#     print(list2[i]) # access each element of the list using a for loop

# ''' The for loop can also be used to iterate over a list directly without using the range() function. The syntax of a for loop to iterate over a list is as follows:'''
# for i in list2:
#     print(i) # access each element of the list using a for loop 

# ''' The for loop can also be used to iterate over a list in reverse order using the range() function. The syntax of a for loop to iterate over a list in reverse order is as follows:'''    
# for i in range(lenth-1,-1,-1):
#     print(list2[i]) 

# list1=[]
# for i in range(1,11):
#     list1.append(i) # add elements to the list using the append() method
# print(list1)    

# list2=[x for x in range(1,11)] # create a list using list comprehension
# print(list2)    

# list3=[x for x in range(1,11) if x%2==0] # create a list of even numbers using list comprehension
# print(list3)    

# string1="Python is a great programming language 1 2 3."
# list4=[i for i in string1 if i.isalpha()] # create a list of alphabetic characters from the string using list comprehension
# print(list4)
# list5=[i for i in string1 if i.isdigit()] # create a list of digits from the string using list comprehension
# print(list5)    

# list1=[1, 2, 3, 4, 5]
# print(list1)  
# del list1[0] # delete the first element of the list using the del statement
# print(list1)    

# print(list1.pop(1)) # delete the first element of the list using the pop() method and return it
# print(list1)
# print(list1.remove(2)) # delete the first occurrence of the element 2 from the list using the remove() method
# print(list1)    

# list1[1]=25 #upadte
# print(list1)  
# list1.clear()
# list1.insert(3,35)
# list1.append(65)
# print(list1)  
# print(list1[1])

# list1=[1, 2, 3, 4, 5]
# list2=[70,80,90]
# list1.append(list2)
# print(list1)

# ''' The extend() method is used to add the elements of a list (or any iterable) to the end of the current list. The syntax of the extend() method is as follows:    '''
# list1.extend(list2)
# print(list1)

# list1=[10,20,30,40]
# list2=[11,22,33,44,55,66]

# for a,b in zip(list1,list2):
#     print(a,b)

''' A stack is a data structure that follows the Last In First Out (LIFO) principle. It can be implemented using a list in Python. The basic operations of a stack are push, pop, peek, and display.   '''
# stack = []
# while True:
#     i=int(input("1 for push, 2 for pop, 3 for peek, 4 for display, 5 for exit: "))
#     if i==1:
#         element=int(input("Enter the element to push: "))
#         stack.append(element)
#         print(stack)
#     elif i==2:
#         if len(stack)==0:
#             print("Stack is empty.")
#         else:
#             print("Popped element: ",stack.pop())
#             print
#     elif i==3:
#         if len(stack)==0:
#             print("Stack is empty.")
#         else:
#             print("Top element: ",stack[-1])            
#     elif i==4:
#         print("Stack: ",stack)
#     elif i==5:
#         break
#     else:
#         print("Invalid input. Please try again.")


queue = []
while True:     
    i=int(input("1 for enqueue, 2 for dequeue, 3 for peek, 4 for display, 5 for exit: "))
    if i==1:
        element=int(input("Enter the element to enqueue: "))
        queue.append(element)
        print(queue)
    elif i==2:
        if len(queue)==0:
            print("Queue is empty.")
        else:
            print("Dequeued element: ",queue.pop(0))
            print(queue)
    elif i==3:
        if len(queue)==0:
            print("Queue is empty.")
        else:
            print("Front element: ",queue[0])            
    elif i==4:
        print("Queue: ",queue)
    elif i==5:
        break
    else:
        print("Invalid input. Please try again.")