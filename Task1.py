"""
Assignment

"""

tup = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

# using list comprehension

res = [(tup[i], tup[i+1]) for i in range(len(tup)-1)]
print("""
-------------------------------------------------------------------------------
Consecutive days""")
print(res)



#------------------------------------------------------------------------------------


day_details = {}
for i, day in enumerate(tup, start=1):
    day_details[day] = (i, day[:3], day.lower(), day.upper(), len(day))

print()
print("Day details dictionary:\n", day_details)


#------------------------------------------------------------------------------------

main_dict = {}
for i in tup:
    myDict = {}
    for j in i:
        if j in myDict:
            myDict[j] += 1
        else:
            myDict[j] = 1
    main_dict[i] = myDict

req_tuple = tuple((x,y) for x, y in main_dict.items())
print("""
-------------------------------------------------------------------------------
tuple with occurence of each character in each day""")
print(req_tuple)

#------------------------------------------------------------------------------------
