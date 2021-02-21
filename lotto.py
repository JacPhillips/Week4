import random
lotto=[] #create empty list

for x in range(1,7): #for loop to get 6 numbers to get random numbers between 1 and 50
    rand= random.randint(1, 51)
    while rand in lotto:
        rand = random.randint(1, 51)
    #to avoid duplicate numbers, we set while loop to ensure that a number is generated only that number is not in the list already
    lotto.append(rand)
print(lotto)

