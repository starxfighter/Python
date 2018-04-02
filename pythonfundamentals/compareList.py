# Takes in two lists and compares them to see if they are equal to one another
def compareList(listA, listB):
    print("length a", len(listA))
    print("length b", len(listB))
    trigger = 0
    if len(listA) != len(listB):
        print("This lists are not equal")
    else:
        for x in range(0,len(listA)):
            if listA[x] != listB[x]:
                trigger = 1
        if trigger == 1:
                print("The lists components are not equal")
        else:
                print("The lists are identical")

# Lists are the same contents and same length
print("Test Case 1")
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareList(list_one, list_two)
# One list is longer than the other
print("Test Case 2")
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareList(list_one, list_two)
# One list is longer than the other
print("Test Case 3")
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compareList(list_one, list_two)
# String list where they are the same length but one value different
print("Test Case 4")
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareList(list_one, list_two)
# String list where they are the same length but one value different
print("Test Case 5")
list_one = [1,2,7,6,2]
list_two = [1,2,5,6,2]
compareList(list_one, list_two)