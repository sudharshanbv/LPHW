
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'peers', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print(f"The count is {num}")

for fruit in fruits:
    print(f"A fruit of type : {fruit}")

for i in change:
    print(f"i got {i}")

#we can create an empty list like this
#elements = []

#this is way to add emements to a lists
#for i in range(0, 6):
#    elements.append(i)

elements = range(0, 6)

for i in elements:
    print(f"Element was: {i}")
