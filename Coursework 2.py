def TZ(n):
    count = 0
    while n>0:
        n = n / 5
        count = count + n
    return int(count)
n = int(input ('Factorial : '))
print (TZ(n))
