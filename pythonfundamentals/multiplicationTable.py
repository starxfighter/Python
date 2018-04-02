x=range(1,13)
y=range(1,13)
line = "X "
for j in y:
    line += str(j)
    line += " "
print(line)
# print("/n")
for i in x:
    line = str(i) + " "
    for j in y:
        line += str(i*j)
        line += " "
        # print(i*j) 
    print(line)
    # print("/n ")