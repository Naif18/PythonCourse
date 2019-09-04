Lists=["Saturday" , "Sunday" , "Monday" ]
print(len(Lists))

Lists.append("Tuesday")
print(Lists)
Lists.insert(0,"Friday")
print(Lists)

Lists.remove("Friday")
Lists.append("NoDay")

print(Lists)

Lists.pop()
print(Lists)


Lists.clear()
print(Lists)
#----------------------
#Copying

org=["Jen" , "Feb" , "Mar"]
copy=org
print(copy)

copy=list(org)
print(copy)

Parenthesis= list(("this" , "Is" , "new" , "List"))
print(Parenthesis)
