# Print odd numbers from 1 to 1002
for x in range(1, 1002, 2):
    print(x)
# Print multiples of 5 from 5 to 1,000,000
for x in range(5, 1000000, 5):
    print(x)
# Sum List
sum = 0
a = [1, 2, 5, 10, 255, 3]
for x in range(0,len(a)):
    sum += a[x]
print(sum)
print(sum/len(a))