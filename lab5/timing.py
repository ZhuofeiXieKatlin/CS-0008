import time

print("-"*27)
n="N"
Time=("Time (sec)")
print("sumofcubes (N) with u**3 ")
print("-"*27)
print("%2s  %22s" % (n,Time))

def sumofcubes():
    sum=0
    N=5000000
    for i in range(1,6):
        start=time.time()
        n=N*i
        for j in range(n):
            sum+=j**3        
        stop=time.time()
        print("%1d %9.2f seconds" % (n, (stop-start)))    
        print("-"*27)
print("-"*27)
sumofcubes()

print("      ")
print("      ")
print("      ")

print("-"*27)
n="N"
Time=("Time (sec)")
print("sumofcubes (N) with u*u*u ")
print("-"*27)
print("%2s  %22s" % (n,Time))

def sumofcubes2():
    sum=0
    N=5000000
    for i in range(1,6):
        start=time.time()
        n=N*i
        for j in range(n):
            sum+=j*j*j  
        stop=time.time()
        print("%1d %9.2f seconds" % (n, (stop-start)))    
        print("-"*27)
print("-"*27)
sumofcubes2()


