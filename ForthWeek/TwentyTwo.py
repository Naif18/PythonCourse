dict={
    "brand": "Ford",
    "model": "Mostang",
    "year" : 1990
}

print(dict)
x= dict["year"]
print(x)

#print the value by get method
z= dict.get("model")
print(z)

#Change value by it's Key
dict["year"] = 2011
print(dict)

#in order to print the value of the key in DIC
for x in dict:
    print(dict[x])


for z in dict.values():
    print(z)

#Loop through both keys and values
for x,z in dict.items():
    print(x,z)