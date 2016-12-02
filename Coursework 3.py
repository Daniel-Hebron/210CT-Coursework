s = (int(input('Input Number: ')))
ans = 0

if s >= 0: 
    while ans*ans <= s:
        ans += 1
        
    if ans*ans != s:
        ans=ans -1
        print('The Highest Square Number is', ans)
        
    else: print('The Highest Square Number is', ans)
else: print(s,'is an error') 

