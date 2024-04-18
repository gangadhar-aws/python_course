
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(piano_keys[2:5])  # Getting items ['c', 'd', 'e']
print(piano_keys[2:])   # Get list from 2n index ['c', 'd', 'e', 'f', 'g']
print(piano_keys[::2])  # get every second item ['a', 'c', 'e', 'g']
print(piano_keys[::-1]) # reversing the list: output: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[::3])  # every two items skiped output:  ['a', 'd', 'g']


