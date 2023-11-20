list_of_numbers = []
count = 1
sum = 0

try :
    while count <= 5 :
        user_inputs =(input("enter values here : "))
        user_inputs = int(user_inputs)
        list_of_numbers.append(user_inputs)

        count += 1
        continue
    for i in list_of_numbers :
        sum = sum + i
    print("sum of this five numbers ",sum)
except ValueError :
    print("You cant yous letters as your answer")