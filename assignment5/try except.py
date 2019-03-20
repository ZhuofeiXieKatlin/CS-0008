while True:
    try:
        num=int(input("Enter an integer: "))
        print("good data")
        break
        ### if you enter a good data, it will not in the loop anymore
    
    except ValueError:
        ### except the data that not in the try statement
        print("you enter bad data")

print("programm complete")
    
