

n = int(input("Enter The Number: "))

sum = 0
for i in range(2,n+1,1):
    if i % 2 == 0:
        sum += i
print("The Sum of Even Numbers is :",sum)
