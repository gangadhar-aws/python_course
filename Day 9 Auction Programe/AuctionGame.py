
print("Welcome to the Auction Program.")

game_on = True

bidders = {}
while game_on:
    name = input("What is your name ? \n :")
    bid = int(input("What' is your Bid ? \n $"))
    guess = input("Are there any other bidders? Type 'y' for Yes 'n' for No ").lower()
    bidders[name] = bid

    if guess == "y":
        game_on = True
    else:
        game_on = False
        max = 0
        name = ''
        for i in bidders:
            if bidders[i] > max:
                max  = bidders[i]
                name = ''
                name +=i
        print(f"The Winner of Bid is Name: {name} and Bid is ${max}")


