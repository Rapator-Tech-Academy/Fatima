#Set & Dictionary
#set doesn't accept duplicate value, all elements unique
#sets mutable, mySet = {}


my_list = [1,1,4,5,5]
my_list = set(my_list) #list(set(mt_list)) turns back to list
print(my_list)

my_set = {1, "hi", (22,9)}
print(my_set)


mySet= {1, 8, "yellow", "blue", (23,90), "python"}

mySet.add("hello")
mySet.update([1, 2, 3], (6, 7, 8))

mySet.remove(1)
mySet.discard("blue")

mySet.pop()
mySet.clear() 

print(mySet)

#Union, intersection, difference and symmetric difference
A = {1, 2, "rapator", 3, 4, 5, "tech"}
B = {1, 6, 8, 7, 2, 4, "academy"}

#Union
print(A.union(B)) # same as print(A | B)
print(B.union(A))

#Intersection
print (A.intersection(B))

#Difference
print(A.difference(B))
print(B.difference(A))

#Symetric Difference
print(A.symmetric_difference(B)) #same as print(A ^ B)


#set membership test in, not in
1 in A
print(1 in A)

3 not in A
print (3 not in A)


#iteratating through a set
strToSet = set("techacademy")
print(strToSet)

