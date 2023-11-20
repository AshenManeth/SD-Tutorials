import random
double_count = 0 


num_of_ralls = input("how many times you want rall dis : ")
num_of_ralls = int(num_of_ralls)

for i in range (num_of_ralls):
    die1 = random.randint(1,7)
    die2 = random.randint(1,7)

    if die1 == die2 :
        double_count += 1

print(num_of_ralls," times you double were genareted ",double_count,"times")
