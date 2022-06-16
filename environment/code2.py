myMixedTypeList = [45, 290578, 1.02, True, "This is a string", "007"]
print(myMixedTypeList)

for items in myMixedTypeList:
    print("{} is of the data type {}".format(items,type(items)))