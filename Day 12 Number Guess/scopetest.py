

apples = 5
orange = 0

print("Before modifiying apples",apples)
def fruits():
    global orange
    global apples
    orange = 6
    print(apples)
    apples = 10

fruits()

print("After Updating variables inside functions apples, ",apples)
print(orange)