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
# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.