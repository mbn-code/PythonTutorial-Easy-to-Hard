x = 10

def myfunc():
# We can also use the global keyword and then it will use the veriable x outside the function also
  global x
  x = "World!" # So even if we have a veriable at the top which is a intiger, then it will still update the veriable because it's a global one

myfunc()

print("Hello " + x)