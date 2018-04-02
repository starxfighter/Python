# Write a program that takes a list and prints a message for each element in the list,
#  based on that element's data type.
def typeList(inList):
    newString = []
    tsum = 0
    cnt_str = 0
    cnt_num = 0
    for x in range(0, len(inList)):
        typechk = type(inList[x]).__name__
        if typechk == "str":
            newString.append(inList[x])
            cnt_str += 1
        if typechk == "int":
            tsum += inList[x]
            cnt_num += 1
    if cnt_str > 0 and cnt_num > 0:
        print("The list entered is of mixed type")
        print("String: ", newString )
        print("Sum: ", tsum)
    elif cnt_str > 0:
        print("The list you entered is of string type")
        print("String: ", newString )
    elif cnt_num > 0:
        print("The list entered is of integer type")
        print("Sum: ", tsum)
    # print("String: ", newString )
    # print("Sum: ", tsum)

# Mixed list
l = ['magical unicorns',19,'hello',98.98,'world']
typeList(l)   
# Integer List
l = [2,3,1,7,4,12]
typeList(l)
# String List
l = ['magical','unicorns']
typeList(l)
