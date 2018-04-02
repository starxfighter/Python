# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
location = words.find("day")
print(location)
temp = words.replace("day", "momth", 1)
print(temp)
# Min and Max
x = x = [2,54,-2,7,12,98]
print(max(x))
print(min(x)) 
# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0])
last = len(x) -1 
print(x[last])
newArr=[]
newArr.append(x[0])
newArr.append(x[last])
print(newArr)
# New List
import math
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print(x)
half = math.floor(len(x)/2)
print(half)
temp = x[:half]
print(temp)
nArr=[]
nArr.append(temp)
start = half
end = len(x)
for i in range(start, end):
    nArr.append(x[i])
print(nArr)