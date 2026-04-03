''' This file is for learning purposes only. It is not intended to be used in production. '''

# x=678
# print("The value of x is:", x)
# print("The type of x is:", type(x))

# x=0b1010
# print("The value of x is:", x)
# print("The type of x is:", type(x)) 
# print("The binary representation of x is:", bin(x))

# x=345
# print("The binary representation of x is:", bin(x))
# print("The octal representation of x is:", oct(x))
# print("The hexadecimal representation of x is:", hex(x))

# a=10
# b=5
# print("The sum of a and b is:", a+b)
# print("The difference of a and b is:", a-b)
# print("The product of a and b is:", a*b)
# print("The quotient of a and b is:", a/b)

# print("The result of 10/3 is:", 10/3)
# print("The remainder of 10%3 is:", 10%3)
# print("The exponentiation of 5**2 is:", 5**2)
# print("The exponentiation of 5**3 is:", 5**3)
# print("The division of 5/2 is:", 5/2)
# print("The floor division of 5//2 is:", 5//2)


# '''In Python, we can use the assignment operator (=) to assign a value to a variable.'''
# x=5
# print("The value of x is:", x)
# '''We can also use the augmented assignment operator (+=) to add a value to a variable and assign the result back to the variable.'''
# x=x+5
# print("The value of x is:", x)
# x+=5
# print("The value of x is:", x)

'''We can also use the augmented assignment operator (-=) to subtract a value from a variable and assign the result back to the variable.'''
# x=5
# x-=5
# print(x)
# x*=5
# print(x)
# x/=5
# print(x)


# x=5
# '''The augmented assignment operator (%=) is used to perform modulus operation and assign the result back to the variable.'''
# x%=3
# print("The value of x is:", x)
# x=5
# '''The augmented assignment operator (//=) is used to perform floor division and assign the result back to the variable.'''
# x//=2
# print("The value of x is:", x)

'''The augmented assignment operator (**=) is used to perform exponentiation and assign the result back to the variable.'''
# x=5
# x**=2
# print("The value of x is:", x)

'''In Python, we can use the comparison operators to compare two values. The result of a comparison is a boolean value (True or False).'''
# x=10
# y=10
# print("The comparison of x and y is:", x==y)
# print("The comparison of x and y is:", x!=y)
# print("The comparison of x and y is:", x>y)
# print("The comparison of x and y is:", x<y)
# print("The comparison of x and y is:", x>=y)
# print("The comparison of x and y is:", x<=y)

'''In Python, we can use the logical operators to combine multiple comparisons. The result of a logical operation is a boolean value (True or False).'''
# x=10
# y="10"
# print("The comparison of x and y is:", x==y)
# x=10
# y=20
# print("The comparison of x and y is:", x<y or x!=10 or x==y)
# print("The negation of x!=10 is:", not x!=10)

'''In Python, we can use the membership operators to check if a value is present in a sequence (such as a string, list, or tuple). The result of a membership operation is a boolean value (True or False).'''
# str="hello Saho"
# print('s' not in str)
# list1=[10,20,30,40,50,60]
# print(80 in list1)

'''In Python, we can use the identity operators to check if two variables refer to the same object in memory. The result of an identity operation is a boolean value (True or False).'''
# x=20
# y=20
# print("The memory address of x is:", id(x))
# print("The memory address of y is:", id(y))
# print("The comparison of x and y is:", x==y)
# print("The identity check of x and y is:", x is y)
# x=[1,2,3]
# y=[1,2,3]
# print("The memory address of x is:", id(x))
# print("The memory address of y is:", id(y))
# print("The comparison of x and y is:", x==y)
# print("The identity check of x and y is:", x is y)

'''In Python, we can use the bitwise operators to perform bitwise operations on integers. The result of a bitwise operation is an integer.'''
x=8
y=10
print("The binary representation of x is:", bin(x))
print("The binary representation of y is:", bin(y))
print("The binary representation of x&y is:", bin(x&y), "and the decimal value is:", x&y)
print("The binary representation of x|y is:", bin(x|y), "and the decimal value is:", x|y)
print("The binary representation of x^y is:", bin(x^y), "and the decimal value is:", x^y)
print("The decimal value of x&y is:", x&y)