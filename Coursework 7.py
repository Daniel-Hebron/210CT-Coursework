N = int(input('Enter A Number: '))
if N > 1: 
    for i in range(2, N): #between 2 and the number user chose
        if(N % i) == 0: #if N remainder equal to 0 it is prime
            print(N, 'is not a prime number')
            break
    else:
        print(N, 'is a prime number')
else:
    print ('please input a positive number') #if user input negative number

