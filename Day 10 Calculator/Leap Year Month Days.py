

def leap_year(year):
    """This function return the true or false if year is leap year it returns true
    else it will return false
    :rtype: object"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("Enter Year: "))
month = int(input("Enter Month Number: "))

if leap_year(year):
    if month == 2:
        print(f"Days of The {month}month :",month_days[month-1]+1)
    else:
        print(f"Days of The {month}month :", month_days[month-1])
else:
    print(f"Days of The {month}month :", month_days[month-1])


