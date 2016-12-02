import random

myList = [5,3,8,6,1,9,2,7] #list I will be shuffling
shuffledList = [] # putting shuffled list into a new empty list

while(myList!=[]):
    n = random.randint(0, len(myList)-1)
    shuffledList.append(myList[n]) #adding random integer from myList and deleting it from myList
    del myList[n]

print(shuffledList)
