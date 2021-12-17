# python if else elif

# two veriables with value 1000 and 0
x = 1000
y = 0

# if x is bigger then y execute the code under
if x > y:
    print("x bigger then y")
# if that is not 'true'
else: # do:
    print("y bigger then x")

# we can also use the elif statement in python with means 'else if something: then do'

if x > y:
    print("x bigger then y")
# else if x is smaller then y, execute the following
elif x < y:
    print("y bigger then x")
# else just pass and don't do anything
else:
    pass

# we can also compare x and y with just printing. it's going to return true if the statement is true, else false

print(x>y)