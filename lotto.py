import random
lotto=[] #create empty list

for x in range(1,7): #for loop to get 6 numbers to get random numbers between 1 and 50
    rand= random.randint(1, 51)
    # while rand in lotto: which one is better
    if rand in lotto:
        rand = random.randint(1, 51)
    #to avoid duplicate numbers, we set while loop to ensure that a number is generated only that number is not in the list already
    lotto.append(rand)
print("Winning numbers: ", lotto,)
# lotto.sort()
# print(lotto)

# convert lotto to set to check common numbers with our_numbers
our_numbers = {3, 28, 4, 18, 44, 1}
print("Our numbers: ", our_numbers, "\n")
lotto = set(lotto)
print("We have ", len(lotto & our_numbers), "winning numbers ", end ="")
if len(lotto & our_numbers):
    print (lotto & our_numbers)

