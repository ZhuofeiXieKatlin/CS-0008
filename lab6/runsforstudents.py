'Runs'


def findruns(L):
    print('\nList is ', L)
    k=1
    for run in range(1,len(L)):
        if L[run]!=L[run-1]:
            k=k+1
    print("Runs found:",k)
    
    max = 0
    count = 1
    x=0
    for j in range(len(L)):
        if L[j] == L[j-1]:
            count = count +1
        else:
            count = 1 
        if count >= max:
            max=count
            x=L[j]
    print ("%s %ds %s %d"%("The longest run of",x,"is of length",max)) 



                 
def main():    
    L = [1, 2, 2, 1, 5, 1, 1, 7, 7, 7, 7, 7, 1, 1, 3, 3, 3]
    findruns(L)

    L = [4, 4, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 7, 7, 1, 1, 3, 3, 6, 3, 3]
    findruns(L)
    
    L = [6]*5 + [2]*9 + [4]*6
    findruns(L)
    
    
    
main()