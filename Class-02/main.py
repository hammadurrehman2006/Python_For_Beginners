#simple funtion 
def Greet():
    print("Hello, user!")
Greet()

#function with parameters

def GreetUser(name):
    print(f"Hello, {name}!")

GreetUser("John Doe")
#prints hello user name.
#in more dynamic way
user = input("Enter your name:")

GreetUser(user)

#default parameters

def GreetUserWithAge(name, age=20):
    print(f"Hello, {name}! You are {age} years old.")

GreetUserWithAge("John Doe")
GreetUserWithAge("Jane Doe", 25)

#returning values from function

def addNumbers(a, b):
    return a + b

result = addNumbers(5, 10)
print(result)