hidden_num=6
user_value=0
count=0

try:

    while True:
        user_value=input("Make Your Guess [between 1 - 20] :")
        user_value = int(user_value)
        count+=1

        if user_value>20 or user_value<1:
            print("Enter a valid number!\n")

        elif user_value!=hidden_num:
            print("Wrong Guess try Again!\n")

        elif user_value== hidden_num:
            print("Congratulation You guessed the correct number! it was 6")
            print("You took"+" "+str(count)+" "+"Guesses.")
            break
except ValueError :
    print("Error : pleace enter correct number *you cant use letters as your answer* ")

except NameError :
    print("Error: pleace enter correct answer")





