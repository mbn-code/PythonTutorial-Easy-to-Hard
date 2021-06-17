# python while loops

x = 0
# While x is smaller then 11
while x < 11:
    # print x
    print(x)
    # add one to x 
    x += 1

print("\n")

x = 1
while x < 6:
    print(x)
#   This will stop at 3 because we are using (if x is 3 then break)
    if x == 3:
        break
    x += 1
print("\n")

# 
x = 1
while x < 6:
  print(x)
  x += 1
  # if x is more then 6 then print 'x is no longer less then 6'
else:
  print("x is no longer less than 6")