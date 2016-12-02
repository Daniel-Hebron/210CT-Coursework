s = input(str('Enter Sentence: ')) #user inputs sentence
print(" ".join(s.split()[::-1])) #split function splits a single string into array, ::-1 is used to reverse the list
