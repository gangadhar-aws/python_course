line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position[0] == 'A':
    map[int(position[1])-1][0] = 'X'
elif position[0] == 'B':
    map[int(position[1])-1][1] = 'X'
else:
    map[int(position[1])-1][2] = 'X'
