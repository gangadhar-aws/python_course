

def prime_check(num):
    prime = True
    if num <= 1:
        print("Not Prime Number")
    else:
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
    return prime

num = int(input("Enter Number to Check Prime Or Not ? "))

if prime_check(num):
    print(f"{num} is Prime Number")
else:
    print(f"{num} it is Not Prime Number")