import random

guess_number = random.randrange(1,21)
user_input_number = 0
count = 0

print("random number is ",guess_number)

try :
    while True :
        user_input_number = input("Make your guess (between 1 and 20) : ")
        user_input_number = int(user_input_number)
        count += 1

        if user_input_number > 20 or user_input_number < 1 :
            print("pleace enter valied number between 1 and 20 \n")

        elif user_input_number != guess_number :
            print("oops your guess is wrong \n ")

        elif user_input_number == guess_number :
            print("congratulation you make correct guess")
            print("you took " + str(count) + " chances to get correct guess\n")
            break
except ValueError :
    print("you cant use letters as your guess")
