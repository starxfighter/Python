# Checks and prints even and odd numbers with a message
def oddEven():
    for x in range(0,2001):
        if (x%2) == 0:
            print("Number is: ", x, " This is an even number")
        else:
            print("Number is: ", x, " This is an odd number")

#given a list and a multiplier multiply each item in the list by the multiplier
def multiply(list, multi):
    for x in range(0, len(list)):
        list[x] = list[x] * multi

    return list

# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied 
# list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list
def layered_multiples(arr):
    # print("input", arr)
    new_array=[]
    val = "i"
    for x in range(0, len(arr)):
        tempArr=[]
        for y in range(0, arr[x]):
            tempArr += val
        # print("temparr", tempArr)
        new_array.append(tempArr)
        # print("new Array", new_array)
    return new_array

# Function calls
oddEven()
a = [2,4,10,16]
b = multiply(a, 5)
print("Multiplied Array", b)
x = layered_multiples(multiply([2,4,5],3))
print("New Array", x)

        