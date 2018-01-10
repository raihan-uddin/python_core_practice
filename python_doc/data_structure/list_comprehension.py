squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares1 = list(map(lambda y: y ** 2, range(10)))
print(squares1)

squares2 = [z ** 2 for z in range(10)]
print(squares2)

a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(a)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
a = [x * 2 for x in vec]  # create a new list with the values doubled
print(a)
a = [x for x in vec if x >= 0]  # filter the list to exclude negative number
print(a)
a = [abs(x) for x in vec]  # apply a function to all the elements
print(a)

# call a method on each element
freshfruit = ['banana', 'loganberry ', 'passion fruit ', 'apple']
print([weapon.strip() for weapon in freshfruit])

# create a list of 1-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

from math import pi

print([str(round(pi, i)) for i in range(1, 6)])
