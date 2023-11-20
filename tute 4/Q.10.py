import random

hidden_number = random.randint(0,20)
count = 1
user_guess_times = 0
print(hidden_number)



try:
    while count <= 6:

        user_given_number =   input("enter your guess here (you have only"+ str(5 - user_guess_times)+" attempts) : " )
        user_guess_times += 1
        user_given_number = int(user_given_number)

        print("count is ", count)
        

        if user_given_number > 20 :
            print("enter value between 0 and 20...")
            count = count + 1
            
        elif user_given_number <= 20 :
            if user_given_number == hidden_number :
                print("congratulations! you guess correct number...")
                print("you get ",user_guess_times," times to guess number \n ")
                break

            elif user_given_number < hidden_number:
                print("you guess is lower than hidden number. please try again....")
                print("you have only ",5-user_guess_times," attempts...\n")

            elif user_given_number > hidden_number :
                print("you guess is higher than hidden number. please try again....")
                print("you have only ",5-user_guess_times," attempts...\n")


            count += 1

            if count == 6 :
                print("oops.. you dont have enough attempts ! ")
                print("correct random number is ",hidden_number)
                break

    
            
            
    

    
except ValueError :
    print("enter valid value ! lettors are not allocated !")
