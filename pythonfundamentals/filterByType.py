# print a specific message based on type and criteria
def filter_type(value):
    typechk = type(value).__name__
    if typechk == "int":
        if value <= 100:
            print("That's a small number")
        else:
            print("Thats a big number")
    elif typechk == "str":
        if len(value) <= 50:
            print("That's a short sentence")
        else:
            print("That's a long sentence")
    elif typechk == "list":
        if len(value)>= 10: 
            print("Big List")
        else:
            print("Short List")
    else:
        print("Type error")
        
    # print(typechk)

# Test the function
print("sI")
sI = 45
filter_type(sI)
print("mI")
mI = 100
filter_type(mI)
print("bI")
bI = 455
filter_type(bI)
print("eI")
eI = 0
filter_type(eI)
print("spI")
spI = -23
filter_type(spI)
print("sS")
sS = "Rubber baby buggy bumpers"
filter_type(sS)
print("mS")
mS = "Experience is simply the name we give our mistakes"
filter_type(mS)
print("bS")
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
filter_type(bS)
print("eS")
eS = ""
filter_type(eS)
print("aL")
aL = [1,7,4,21]
filter_type(aL)
print("mL")
mL = [3,5,7,34,3,2,113,65,8,89]
filter_type(mL)
print("lL")
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
filter_type(lL)
print("eL")
eL = []
filter_type(eL)
print("spL")
spL = ['name','address','phone number','social security number']
filter_type(spL)