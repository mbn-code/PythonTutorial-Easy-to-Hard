# assigning multiple values

# in python we can assign multiple values by putting veriables right after each other
x,y,z = "a","b","c"

# You can also print out multiple veriables in one line

print(x,y,z) # This will make then print right after each other, but same line

# but we can also make multiple veriables for one value

x = y = z = "Hello world!"

print(x)
print(y)
print(z)

# This means that we can refer to the same string by different veriables 

print(x,y,z) # We can also print these right after each other like normal veriables

# unpacking a list

fruits = ["apple", "banana", "cherry"] # making a list

x, y, z = fruits # assigning veriables to the items in the list
print(x)
print(y)
print(z)

print(x,y,z) # And again we can print this out after each other