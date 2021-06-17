# python lists

# This is what a list looks like. A list has items.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

x = ["a","b","c"]

print(x)

# python list allow duplicates of items in the list

# You can get the lenght of a list

x = ["a", "b", "c"]
print(len(x)) # it will output 3 becuase there are 3 items in the list


# We can store different data types in a list

x = ["apple", "banana", "cherry"]
y = [1, 5, 7, 9, 3]
z = [True, False, False]

print(x)
print(y)
print(z) # and it's going to output them all as if they were strings 

list1 = ["abc", 34, True, 40, "male"]

print(list1) # We can also store multiple different data types in one list, and it's going to convert them all to strings


# We can use the build in function type() and get the type (and it's going to output list, because it's a list)

x = ["apple", "banana", "cherry"]
print(type(x))

# We can also call the function list(()) (using double brackets) and then it's going to act as a list
x = list(("apple", "banana", "cherry")) # note the double round-brackets
print(x)
print(type(x))