n = int(input ('Factorial : '))
factorial = 1
trailingZeros = 0

for i in range(1, n+1):  #starts at 1 and will end at users number + 1 
    factorial = factorial * i

while(True):
    if int(factorial % 10) == 0: #'%' means it will show you the remainder from division
        trailingZeros += 1 #if n is equal to 0, trailing zero = 1
        factorial = factorial / 10
    else:
        break

print(trailingZeros)
