magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    #print(magician)
    print(f"{magician.title()}, that was a great trick")


## Number list
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(1,10, 2))
print(even_numbers)

## Statistics
print(max(even_numbers))
print(min(even_numbers))
print(sum(even_numbers))

## List comprehension
squares = [value**2 for value in range(1,6)]
print(squares)

## Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[:4])
print(players[1:])
print(players[-3:])

## Copy list, generate new list
copy_players = players[:]
print(copy_players)
players.append('Will')
copy_players.append('William')
print(players)
print(copy_players)

## Create new reference to the same list
ref_players = players
players.append('Ivy')
print(ref_players)

#########################################################################
## Immutable list --> tuples
dimensions = (200, 50)
print(dimensions[0])

## Can re-assign the whole elements to the tuples
dimensions = (400, 10)
print(dimensions[0])