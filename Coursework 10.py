sequence = [1,2,3,4,5,1,2,3,4]
longest = -1
length = 0
LL = 0


for i in range (len(sequence)): #check if element higher or lower than last
        if (i + 1 == len(sequence)): #check if its at end of array
            if(length > LL):
                LL = length
                longest = i - LL
                break

        elif (sequence[i] < sequence[i + 1]): #check if it is smaller than element nect to it
            length += 1

        elif (length >= LL): #check if length bigger than LL to see if it can change length
            LL = length
            longest = i - length #longest changed to first to see starting point
            length = 0

for i in range(longest, longest + LL +1):
    print(sequence[i])
