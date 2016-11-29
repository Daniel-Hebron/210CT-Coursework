def RV(word):
    if len(word) == 0:
        return word 
    else:
        x = word[1:len(word) + 1]
        firstLetter = word[0]
        if firstLetter in "aeiouAEIOU":

            return RV(x)
        else:
            return firstLetter + RV(x)

word=(str(input('Input Word: ')))

print(RV(word))
