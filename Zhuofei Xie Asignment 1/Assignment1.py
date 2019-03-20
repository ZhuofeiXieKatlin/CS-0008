'''
Student: Zhuofei Xie
purpose: Comparing the product of two positive integers using the multiplication
         algorithm of the ancient Egyptians. 
Date:9/21/2017
sample run: 
number: 14 and 12
        72890346 and 35619
'''
run=int(input("Enter the number of runs: "))
for count in range(run):
    x=int(input("Enter x: "))               ### input the value of x
    y=int(input("Enter y: "))               ### input the value of y
    product= 0                              ### the original value of "product"
    
    if y<x:                                 ### using if function 
        temp = x                            ### changing the position of x and y
        x = y
        y = temp
        integer_1=x 
        integer_2=y           

    print(55*"-")
    print("%15s %15s  %22s" % ("X", "Y" ,"Product"))
    print(55*"-")
    print("%15d %15d %23d" % (x, y,product)) ###printing all calculations 

    while x>0:                           ###using while function
        if x%2==0:                    ### the situation of x is an even num
            x=1/2*x
            y=2*y
            print("%15d %15d %23d" % (x, y,product)) ###printing all calculations
        
        else:                   ###the situation of x is an odd num
            x-=1
            product += y
            print("%15d %15d %23d" % (x, y,product))  ###printing all calculations

    print(55*"-")
    print(integer_1, '*',  integer_2, '=', product) ###the result of x * t
    print(" ")                    ###leaving a blank for the next line