import random
def guess_the_number():
    num = random.randint(0,100)
    while True:
        user = int(input("Enter your guess:"))
        if user > num:
            print("Too high guess")
        elif user < num:
            print("Too low guess")
        else:
            print("Your guess is correct! You Won")
            break
guess_the_number()