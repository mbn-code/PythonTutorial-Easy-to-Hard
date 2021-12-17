# python functions

# This is a function

def myFunction(): # You can call a function whatever you want, just that it doens't start with a number or have a hyphen or space just like a veriable
    print("Hello, I am getting executed by a function")

myFunction() # Calling the function



# in funciton we can pretty much do anything just like if it was not in a function

def mySecFunction():
    for x in range(2):
        print("Hello World!")
    
    x = 2

    if x == 2:
        print("The veriable x is given the value 2")
    else:
        pass
mySecFunction()

# we can call the fuction as many times as we want, we can also call a function inside a function

def callFuncInFunc():
    mySecFunction()

callFuncInFunc()

# and then when you call that function, it's going to call the other function again
