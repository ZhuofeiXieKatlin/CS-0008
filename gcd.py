def main():
    x=int(2)
    y=int(3)
    print("The GCD of ",x , "and", y, "is", end=" ")
    while y != 0:
        x_prime=y
        y_prime=x % y
        x=x_prime
        y=y_prime
   
    print(x)
main ()
