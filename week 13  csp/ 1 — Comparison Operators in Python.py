# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a == b) #output false

print(a == b)   # check for equality# False
print(a != b)   # checks if not equal# True
print(a > b)    # check for greater than# False
print(a < b)    # checks for less than# True
print(a >= b)   # checks for greater than or equal to# False
print(a <= b)   # checks for less than or equalt to# True


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #output true
8 != 8 #output false
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.
print(8 == 8) #output true
print(3 > 1) #output true
print(10 < 15) #output true
print(8 == 4) #output false
print(13>11) #output false
print(9 >= 10) #output false
 # Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
# if the score is between 90-100 .. you got an A
# if the score is between 80-89 -- you got a B
# if the score is between 70-79 -- you got a C
# if the score is between 61-69... you got a D
# else you failed
score = int(input("what is your score?"))
if score >=90 and score <=100:
    print("you got an A")
elif score >=80 and score <=89:
    print("you got a B")
elif score >=70 and score <=79:
    print("you got a C")
elif score >=60 and score <=69:
    print("you got a D")
else: 
    print("you failed come to ACLAB")

password = input("What is your password?")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("password is valid")
else:
    print("password is invalid. " \
    "it must be at least 8 characters long and contain at least one digit.")