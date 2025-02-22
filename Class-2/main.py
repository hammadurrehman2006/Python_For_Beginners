#Loops in python
names = ["Hammad", "Ibad", "Saif", "Talha"]

# For loop to print all names
for name in names:
    print(name)
    print("---")
# for loop to print range of numbers
for i in range(10):
    print(i)

# noted something about the above loop it gave 0 to 9 numbers but not 1 to 10
# to print number from 1 to 10 we will use 
for i in range(1, 11):
    print(i)

# While loop

i = 0
while i < 10:
    print(i)
    i += 1