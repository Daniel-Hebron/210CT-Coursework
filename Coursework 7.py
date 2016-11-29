N = int(input('Enter A Number: '))
if N > 1:
    for i in range(2, N):
        if(N % i) == 0:
            print(N, 'is not a prime number')
            break
    else:
        print(N, 'is not a prime number')
else:
    print (N, 'is not a prime number')
