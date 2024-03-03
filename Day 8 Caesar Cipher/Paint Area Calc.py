import math


def paint_area(height, width, coverage):

    cans = (height*width)/coverage
    return round(cans)

h = int(input("Enter Hight of The Wall"))
w = int(input("Enter width of The Wall"))
c = 5
result = paint_area(h,w,c)
print(f"You Need {result} cans of paint")