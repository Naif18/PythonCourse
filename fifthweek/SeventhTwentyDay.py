a = 90 
b = 839

if a > b:
    print ("A is grater than B")
else:
    print("B is the biggest")

if a < b: print("It's bigger")

#short hand if .. else
d = 20
x = 30
print("A") if  d > x else print ("B")

#Nested if
z = 40
if z > 10:
    print("Above Ten ,")
    if z > 20:
        print("And laso above twenty")
    else:
        print("but not above 40")