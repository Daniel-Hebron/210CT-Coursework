def RemoveVowels(word):
    if len(word) == 0:
        return word 
    else:
        x = word[1:len(word) + 1] #1: will work from first letter of word until last
        firstLetter = word[0] #zero operator
        if firstLetter in "aeiouAEIOU":
            return RemoveVowels(x) #will loop & delete each vowel in word until none left
        else:
            return firstLetter + RemoveVowels(x)
word=(str(input('Input Word: ')))

print(RemoveVowels(word))
