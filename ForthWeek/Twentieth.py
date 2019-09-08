Sets = {"One" , "Tow" , "Three" , "Four" }
print(Sets)
#--------
#Not allow to repeat or duplicate
sets2= {"One" , "Tow" , "Three" , "Four"  , "Four"}

print(sets2)

for x in sets2:
    print(x)

#Check if "One" in the list

print("One" in Sets)
#Return True ^

Sets.add("Five")

Sets.update([1 , 24 , 88 ])

print(Sets)
