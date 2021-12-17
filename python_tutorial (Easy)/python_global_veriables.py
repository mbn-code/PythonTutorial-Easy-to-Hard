# making veriable x and assign to world (string)
x = "world"

# as shown here we can create a veriable outside the function and then still use it inside the function (global veriable)
def myFunction():
    print("Hello " + x)

# calling the function
myFunction()


print("\nSecond example: \n")
# making veriable
x = "Hello"

# Then making function with the same veriable name inside, but a differnt string assigned to it
def myfunc():
  x = "fantastic" # In python, it reads like a script (top to buttom)
  print("Python is " + x) # python will know not to use the same veriable outside the function, if we make the same veriable name but different value

myfunc()

# Here we are now using the veriable from the top before the function
print("World " + x) # and python knows not to use the one inside the function