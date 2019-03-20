'''
Student: Zhuofei Xie
purpose: Inputing a string of digits and an integer representing yhr number of
         digits in each group. From the consecutive products of each group of 
         three, determine the maximum. 
Date:9/21/2017
sample run: 
number: 491773 and 2
        72890346 and 3
        845801561660797191338754992 and 6
'''
import math
run=int(input("Enter the number of runs: "))
for count in range(run):
        snum=input("Enter an integer:")
        dig=int(input("Number of digits in a product: "))

        val=0                       ###call function that returns product of digits 
        indx=0
        grps=len(snum)-dig+1        ###define groups of digits 
        x=0

        def product(d,x,s):         ###the function of product with three changes(d,x,s)
                last=x+d
                pro=1
        
                while x<last:      ###using while function 
                        pro*=int(snum[x])
                        x+=1
                return pro         ###return pro from a string to integer

        while indx<grps:          ###using while function 
                val2=product(dig,indx,snum)
        
       
                if val2>val:     ###using if function
                        val=val2
                indx+=1

        print("The max product of", dig, "consecutive digits in",snum,"is",val)
               ###printing the final answer
        print("    ")         ###leaving a blank for the next line
        
        
