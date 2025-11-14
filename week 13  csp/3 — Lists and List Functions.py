# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of collections family in python
# Examples:
my_list = [1, 2, 3, 4, 5,]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print(type(my_list)) # [2, 3, 4]
print(my_list[0]) 
print(my_list[1:4])
print(my_list[1:])
print(my_list[:-1])
# reverse the list
print(my_list[::-1]) 
# modifying a list 
my_list.append(6) 
print(my_list)
# add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list)
my_list.extend([9, 10, 11])
print(my_list)
# Remove the last item
my_list.pop()
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list.remove(4)
print(my_list)
my_list.reverse()
print(my_list)
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
superlong_list = list(range(120, 500))
my_list.append(superlong_list)
print(my_list)
del my_list[::3]
print(len(my_list)) 

# list fuinctions 
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of a list
# .pop() - removes and returns an item at a given index
#   (default is the las item)
# .remove() - removes thje f9irst occurence of a specified value 
# .sort() - sorts the list in ascending order 
# .reverse() - reverses the order of the list
###################################################
# why is a list more usedul trhan a variable ?
# A list can hold mutiple values,
# While a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)

print(cakes[0])

print(cakes[-1])

cakes[0] = 'strawberry'
print(cakes)

cakes.append('lemon')
print(cakes)

cakes[1] = 'chocolate'
print(cakes)

cakes.pop()
print(cakes)

cakes.insert(2, 'funfetti')
print(cakes)


my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
food = ['pizza', 'wings', 'empanadas', 'tacos', 'fried chicken']
print(food)
# # Print the second and last item.
print(food[-4])
print(food[-1])
# # Add a new item using .append().
food.append('cheesecake')
print(food)
# # Remove the first item using .pop(0).
food.pop(0)
print(food)
# # Reverse your list using .reverse().
food.reverse()
print(food)

# sets= {1, 2, 3}
# sets aren unordered collections of unique items
# sets do not support indexing or slicing
# sets are mutable, meaning you can add or remove items
# sets arew created using curly braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
print(4 in my_set)
print(3 in my_set)

# tuples arew ordered collections of items 
# tuples are immutable, meaning you cannot modify them after creation
# tuples are created using parentheses ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
# # Create a list of 3 lists (matrix), and access the middle element.