

year = int(input("Enter Year to Check Leap or not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Lear Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")