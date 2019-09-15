DayList= {
    "saturday" : 1 ,
    "sunday" : 2,
    "monday" : 3,
    "tuesday" : 4,
    "wedneday" : 5,
    "Thersday" : 6,
    "friday":7
}

#Copy a dictionary 
copydic= DayList.copy()
copydic2=dict(DayList)

print(copydic)
print(copydic2)

#Nested Dictionary

my_family = {
    "Child" : {
        "Name" : "email",
        "year" : 2005
    },
    "Child 2" : {
         "Name" : "email",
        "year" : 2008
    },
    "Child 3" :{ 
        "Name" : "email",
        "year" : 2010
    }
}

print(my_family)

#Create three dictionaries, then create one dictionary that will contain the other three
 

Child  = {
        "Name" : "email",
        "year" : 2015
    } 

Child2 = {
        "Name" : "email",
        "year" : 2017
    }

Child3 = {
        "Name" : "email",
        "year" : 2018
    }

family_Dic={
    "chilDIC" : Child,
    "ChildDIC" : Child2,
    "childDIC" : Child3
}

print(family_Dic)