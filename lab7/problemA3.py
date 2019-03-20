### problem A3
'''
def problemA3():
    a = int(input("a3: "))
    b = int(input("b3: "))
    
    sumsq=0
    temp = 0
    if a >=b:
        for k in range(b,a+1):
            temp = temp + k**2 
    else:
        for k in range(a,b+1):
            temp = temp + k**2
    sumsq = sumsq + temp
    print(sumsq)
'''    
a = int(input("a: "))
b = int(input("b: "))
sumsq = 0
for k in range(a,b+1):
    temp = 0
    for u in range(1,k+1):
        temp = temp + 1
    sumsq = sumsq + temp*temp
print(sumsq)
