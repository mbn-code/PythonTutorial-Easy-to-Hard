# python strings

a = "Hello"

print(a)


# by making eather 3 double or single quotes on each side will make it so you can wrtite more lines insted of doing \n to go to next line.  
a = """
line 1
line 2
line 3
"""
print(a)

# We can also select a specific character from a string by using []

a = "Hello World!"

print(a[3]) # When we do [] it will act as a list. So the H in Hello will be position 0. A list, string, tuple, dictionary etc etc... Will always start with position 0

print("\n")


for x in "banana": # We can also print the individual characters line by line, by using for x in "banna" (x can be almost anything)
  print(x)

print("\n")


# We can also get the lenght of a string by using the build in function len()

a = "Hello World!"

print(len(a))

print("\n")

# asking if something is in the string

a = "The best things in life are free!"
print("free" in a) # This prints true, because free is in the string 
print("banana" in a)# And this false because it's not in the string

print("banana" not in a) # if it's not in the string, then return true, else false

print("\n")

# We can also do if statements with strings 

a = "The best things in life are free!"
if "free" in a:
    print("If free is in type string a, then execute this code")

print("\n")