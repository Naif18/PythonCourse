sets= {"One" , "Tow" , "Three" , "Four"  , "Apple"}
print(len(sets))

sets.remove("Four")
print(sets)

sets.discard("One")
print(sets)

#pop method delete any items in the set becouse it is  unordered 

X = sets.pop()
print(X)

print(sets)

#del sets 

#Using the set constructor to make a set

con_set=set(("Apple" , "Banana" , "Cherry"))
print(con_set)
# Coparing between tow set and remove the existing one 
con_set.difference_update(sets)
print(con_set)