''' This file is for learning purposes only. It is not intended to be used in production. '''
''' The match statement is a new feature in Python 3.10 that allows you to match a value against a pattern. It is similar to the switch statement in other programming languages. The syntax of the match statement is as follows:'''
from unittest import case


# day=51
# match day:
#     case 1:     
#         print("Monday")
#     case 2:     
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")       
#     case 5:
#         print("Friday")     
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")    
          
# num=int(input("Enter a number between 1-5:"))
# match num:
#     case 1|2|3:
#         print("You entered number out of 1,2 or 3")
#     case 4|5:
#         print("You entered number out of 4 o5 5")
#     case _:
#         print("Invalid number")

''' import math module to use the sqrt() function to find the square root of a number. The sqrt() function takes a number as an argument and returns the square root of that number.   '''
import math
x=16
# print(math.sqrt(x)) # The sqrt() function takes a number as an argument and returns the square root of that number. In this case, it returns the square root of 16, which is 4.0.
# print(math.sqrt(8)) # The sqrt() function takes a number as an argument and returns the square root of that number. In this case, it returns the square root of 8, which is 2.8284271247461903.
# print(math.pow(2,3)) # The pow() function takes two arguments, the base and the exponent, and returns the result of the base raised to the power of the exponent. In this case, it returns 2 raised to the power of 3, which is 8.
# print(math.ceil(12.9)) # The ceil() function takes a number as an argument and returns the smallest integer greater than or equal to that number. In this case, it returns 13, which is the smallest integer greater than or equal to 12.9.
# print(math.floor(12.9)) # The floor() function takes a number as an argument and returns the largest integer less than or equal to that number. In this case, it returns 12, which is the largest integer less than or equal to 12.9.
# print(math.factorial(5)) # The factorial() function takes a number as an argument and returns the factorial of that number. In this case, it returns 120, which is the factorial of 5 (5! = 5 x 4 x 3 x 2 x 1 = 120).
# print(math.log(100))# The log() function takes a number as an argument and returns the natural logarithm of that number. In this case, it returns 4.605170185988092, which is the natural logarithm of 100.
# print(math.log(100,10)) # The log() function can also take a second argument, which is the base of the logarithm. In this case, it returns 2.0, which is the logarithm of 100 to the base 10 (log10(100) = 2).  
# print(math.sin(0)) # The sin() function takes an angle in radians as an argument and returns the sine of that angle. In this case, it returns 0.0, which is the sine of 0 radians.
# print(math.cos(0)) # The cos() function takes an angle in radians as an argument    and returns the cosine of that angle. In this case, it returns 1.0, which is the cosine of 0 radians.
#print(math.tan(0)) # The tan() function takes an angle in radians as an argument and returns the tangent of that angle. In this case, it returns 0.0, which is the tangent of 0 radians.    

# import random

# print(random.random()) # The random() function returns a random float number between 0.0 and 1.0. In this case, it returns a random float number between 0.0 and 1.0, such as 0.123456789.
# print(random.randint(10,40))  # The randint() function takes two arguments, the start and the end, and returns a random integer between the start and the end (inclusive). In this case, it returns a random integer between 10 and 40, such as 25.
# print(random.randrange(1,3)) # The randrange() function takes two arguments, the start and the end, and returns a random integer between the start and the end (exclusive). In this case, it returns a random integer between 1 and 3, such as 2.
# print(random.randint(1,3)) # The randint() function takes two arguments, the start and the end, and returns a random integer between the start and the end (inclusive). In this case, it returns a random integer between 1 and 3, such as 2.
# list1=[10,20,30,40,50,60]
# print(random.choice(list1))
# random.shuffle(list1) # The shuffle() function takes a list as an argument and shuffles the elements of the list in place. In this case, it shuffles the elements of list1, which is [10, 20, 30, 40, 50, 60], and the order of the elements in list1 will be changed randomly. For example, after shuffling, list1 might become [30, 10, 50, 20, 60, 40].
# print(list1)
# print(random.uniform(1,10)) # The uniform() function takes two arguments, the start and the end, and returns a random float number between the start and the end. In this case, it returns a random float number between 1 and 10, such as 5.678901234.

# import random

# sysnumber=random.randrange(1,101)
# usernumber=int(input("Enter Your number between 1 to 100 :-"))

# if sysnumber>usernumber:
#     print("sys number : ",sysnumber)
#     print("Your number is low")
# elif sysnumber< usernumber:
#       print("sys number : ",sysnumber)
#       print("Your number is high") 
# else:
#      print("Great !! you are Winner, number is equal")    

