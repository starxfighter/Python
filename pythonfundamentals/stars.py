def draw_stars(sList):
    line = " "
    for x in range(0, len(sList)):
        for y in range(0, sList[x]):
            line += "*"
        print(line)

def draw_stars2(sList):
    line = " "
    for x in range(0, len(sList)):
        typechk = type(sList[x]).__name__
        if typechk == "str":
            end = len(sList[x])
            val = sList[x][0]
        else:
            end = sList[x]
            val = "*"
        for y in range(0, end):
            line += val
        print(line)
        line = " "


x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
print("Version 2")
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
