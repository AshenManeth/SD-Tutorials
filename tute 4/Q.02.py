total = 0
count = 0
user_input_score = 0
score_enterd_time = 0

try :


    while True :

        user_input_score = input("enter score (to exit enter -9) : ")
        user_input_score = int(user_input_score)
        count += 1
        total += user_input_score

        if user_input_score == -9 :
            print ("you enterd " + str(count - 1) + " times scores ")
            print("totle of the score = ",total + 9 )

            if count <= 2 :
                print("to calculate vlues you must to enter at least two scores \n")
                break
                
            else:
                avarage = float(total+9)/(count-1)
                print("class avarage is "+ str(avarage) + "\n")
                break

        else :
            print("input next score \n")

except ValueError :
    print('''Please Enter Valied Number.
Don't use letters as your answer \n''')

