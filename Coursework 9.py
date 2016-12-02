L = (input('Interval: ')).split()
array = [2,3,5,7,9,13]


def BSA(low, high, currentlist, n=len(array)):
    LowBoundary = 1
    HighBoundary = n
    
    while LowBoundary < HighBoundary:
        middle = int((LowBoundary+HighBoundary)/2)  #index of element to see if it exists between low and high
        if currentlist(mid) >= low and currentlist(mid) <= high:
            return True
        elif currentlist(mid) > high:
            HighBoundary -=1  #if greater than it will go down one element in the list
        elif currentlist(mid) < low:
            LowBoundary +=1  #if less than it will move up one element in the list
    return False

print(BSA(int(L[0]), int(L[1]), array))
