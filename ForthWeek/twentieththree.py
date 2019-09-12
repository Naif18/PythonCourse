DayList= {
    "saturday" : 1 ,
    "sunday" : 2,
    "monday" : 3,
    "tuesday" : 4,
    "wedneday" : 5,
    "Thersday" : 6,
    "friday":7
}

if "friday" in DayList:
    print("Yes, it's Friday")

#Dictionary Lengh
print(len(DayList)) 

#Delete value
DayList.pop("monday")
print(DayList)

#Delete the last value we added
DayList.popitem()
print(DayList)