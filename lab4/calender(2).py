'''
student name: Zhuofei Xie
The purpose: run the programm which can create calender for people
Date:9/26/2017
sample run: 
number: 30 and 4
'''
def main():
    run=int(input("How many runs: "))  
    for count in range(run):       
        n = int(input("Input the number of days in the month (28-31): "))
        while n<28 or n>31:
            n = int(input("Input the number of days in the month (28-31): ")) 
        
        d = int(input("Input the starting day (0=Sun, 1=Mon,...): "))
        while d<0 or d>6:    
            d = int(input("Input the starting day (0=Sun, 1=Mon,...): "))    
       
        m = input("Input the month: ")
        print(m)        
        
        for j in range(d):
            print("   ", end = "")
        i=1
        while i<=n:
            if i <10:
                print("",i,end=" ")
            else: 
                print(i, end=" ")
            if (i+d)%7==0:
                print(" ")
            i+=1
        print("    ")
        print("    ")
        
main()