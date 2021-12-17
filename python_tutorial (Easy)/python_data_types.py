# python data types

# we can assign the x verialbe to all these data types, and print it out right after
# And then assign the x veriable again to another one. This is because python can update the veriable and assign it another data type, or even another string


x = "Hello World"	#str	
print(x)
x = 20	#int	
print(x)
x = 20.5	#float	
print(x)
x = 1j	#complex	
print(x)
x = ["apple", "banana", "cherry"]	#list	
print(x)
x = ("apple", "banana", "cherry")	#tuple	
print(x)
x = range(6)	#range	
print(x)
x = {"name" : "John", "age" : 36}	#dict	
print(x)
x = {"apple", "banana", "cherry"}	#set	
print(x)
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(x)
x = True	#bool	
print(x)
x = b"Hello"    #bytes	
print(x)
x = bytearray(5)	#bytearray	
print(x)
x = memoryview(bytes(5))	#memoryview
print(x)



#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview