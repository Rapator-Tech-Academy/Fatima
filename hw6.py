#Different python set methods
mySetNames = {"Alex", "Chloe", "Jane", "Rick", "Morty"}
mySetNames2 = mySetNames.copy()
print(mySetNames)
print(mySetNames2)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))
print(b.issubset(a))

print(a.issuperset(b))
print(b.issuperset(a))


#built-in functions with set
#all
mySet = {1, 0, "apple"}
x = all(mySet)
print(x)

#any
mySet = {1, 0, "apple"}
x = any(mySet)
print(x)

#len
x = len(mySetNames)
print(x)

#max
x = max(mySetNames)
print(x)

#min
x = min(mySetNames)
print(x)

#sum
sumSet = {1, 8, 99, 7, 4}
x = sum(sumSet)
print(x)

