# python bool

# A boolean has two values it can return. true and false

# 

print(10 > 22) # In this print function it would return a true or false depending on if it's true or false

# It's actually doing an if statement in the background

def my_statement(): # this is what it is doing in the background
    if 10 > 22:
        return True
    else:
        return False

# booleans can also be other then >, it can be < and ==
# What does these mean? > means the number to the left is higher then the right number
                    #   < is just the reverse of >
                    # and == if checking if it's the same value, or string if the veriable we are checking is a string

print(10 < 22) # This is going to return true, because 10 is a smaller intiger (number) then 22

print(10 == 22) # This is then going to return false, because 10 is not the same as 22

# we can also check something bool value by using the bool() function


x = 1000
y = "Hello World!"

# These both return true because both of them has a value of something being in there. 
# In other words when a string is not empty it's 1, 1 means true. if there was to be nothing in the string, it would return 0, false 
# also the intiger returns true, because there is a value of something in there, if the value of the intiger was 0, then it would return false
print(bool(x))
print(bool(y))

print(bool(False),bool(None),bool(0),bool(""),bool(()),bool([]),bool({})) # All of these also return false or 0 because they are all empty and has no value


class myclass():
  def __len__(self):
    return 0 # We can also make a class and then return 0

myobj = myclass() # Then make the class a object 
print(bool(myobj)) # and then print out the object

# if we change the 'return 0' to a 'return 1', then it's going to return true in our terminal


# we can also do the same for functions

def myFunc():
    return True

print(myFunc()) # but when in a function it's going to return what you put in the return keyword. here you can both put, 1,0,True,False. But you can't put strings like 'return true' The t in true has to be upper case, else you will get an error


# here in this isinstance example we are checking if x is an intiger. it returns true if it is, else false
x = 200
print(isinstance(x, int))
