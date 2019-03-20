def countOff(L,m):
    '''
    Counts off m people in list L, removing the m-th person then returns the 
    remaining list to the caller.
    '''
    y =  m % (len(L))
    L.pop(y-1)
    for x in range(y-1):
        L.append(L.pop(0))
    return L
        
        
def main():
    n = int(input('Enter the number of people:> '))
    m = int(input('Enter the count:> '))
    L = list(range(1,n+1))
    
    print(L)
    while len(L) > 1:
        L = countOff(L,m)
        print(L)  
    print('survives')  
main()    
