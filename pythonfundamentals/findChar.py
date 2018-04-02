# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.
def findChar(sList, sChar):
    trigger = 0
    newArr = []
    for x in range(0, len(sList)):
        for y in range(0,len(sList[x])):
            if sList[x][y] == sChar:
                trigger = 1
        if trigger == 1:
            newArr.append(sList[x])
            trigger = 0
    print(newArr)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChar(word_list, char)