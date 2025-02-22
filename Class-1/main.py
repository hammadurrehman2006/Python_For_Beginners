print("Hello world!");
name = "Muhammad Hammad ur Rehman"
age = 18
isAlive = True

print(f"Hello, my name is {name}. I am {age} years old.")

#data types in python
name = "Muhammad Hammad ur Rehman"
age = 18
isStudent = True
pyVersion = 3.11
#list
numbers = [1, 2, 3, 4, 5]
#tuple
coordinates = (1, 2, 3)
#set
set = {1, 2, 3, 4}
#Operators
#Main Types of operators
# 1. Arithmetic operators (+, -, *, /, %, //, **)
# 2. Assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
# 3. Comparison operators (==, !=, >, <, >=, <=)
# 4. Logical operators (and, or, not)
# 5. Identity operators (is, is not)
# 6. Membership operators (in, not in)

# Arithmetic operators
a = 5
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) 
print("Exponentiation:", a ** b)  
print("Floor Division:", a // b) 
print("Modulus:", a % b)

# COmparision operators
a = 5
b = 3

print("Equal to:", a == b)  
print("Not equal to:", a != b)
print("Greater than:", a > b)  
print("Less than:", a < b)  
print("Greater than or equal to:", a >= b)  
print("Less than or equal to:", a <= b)  

# Logical operators
a = True
b = False

print("Logical and:", a and b) 
print("Logical or:", a or b)
print("Logical not:", not a) 

# assignment operators
a = 5

a += 3  # addition assignment
print(a)  

a -= 2  # subtraction assignment
print(a)  

a *= 4  # multiplication assignment
print(a)  

a /= 2  # division assignment
print(a)  

a **= 2  # exponentiation assignment
print(a)  

a //= 2  # floor division assignment
print(a)  

a %= 5  # modulus assignment
print(a) 

# Membership operators
my_list = [1, 2, 3, 4, 5]

print("Membership:", 3 in my_list)  
print("Non-membership:", 6 not in my_list) 

# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Identity:", a is b)  
print("Identity:", a is c) 
print("Non-identity:", a is not b) 
print("Non-identity:", a is not c)  