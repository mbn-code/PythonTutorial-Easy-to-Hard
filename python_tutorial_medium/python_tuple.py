
# creating a tuple
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

# Tuples allow duplicate values
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

# again we can also get the lenght of a tuple

tuple1 = ("apple", "banana", "cherry")
print(len(tuple1))


thistuple = ("apple",) # tuple because of the ',' at the end 
print(type(thistuple))
 
# NOT a tuple
thistuple = ("apple") # this is just going to be a string
print(type(thistuple))


# String, int and boolean data types can be stored in a tuple

tuple1 = ("apple", "banana", "cherry")
print(tuple1)
tuple1 = (1, 5, 7, 9, 3)
print(tuple1)
tuple1 = (True, False, False)
print(tuple1)
