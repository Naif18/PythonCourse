Ls=[90 , 33 , 20  , 88 , 50]

Ls.append("I'm new")
print(Ls)

#-----

newLs= Ls.copy()
print(newLs)

#-------------

Ls.pop(5)
Ls.sort()
print(Ls)

#-----------

Ls.extend("Lastest")
print(Ls)

#--------------

tuples=("swift" , "Python" , "Java" , "C#")

if "Python" in tuples:
    print("Python is there")
