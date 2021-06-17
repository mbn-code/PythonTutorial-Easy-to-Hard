# python for loop

# this is a list
fruits = ["apple", "banana", "cherry"]
# for x in frutes means. print the fruits line by line
for x in fruits:
    print(x)

# list
fruits = ["apple", "banana", "cherry"]


for x in fruits:
    print(x)
    # This means 'when banana in x (the fruits list) break and don't print the rest'
    if x == "banana":
        break

# we can also combine for loop with the range function, and tell it how many times to print or execute a function etc...

for x in range(10):
    print("I got executed 10 times")