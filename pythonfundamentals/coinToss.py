import random
import math
print("Starting the program")
headcnt = 0
tailcnt = 0
for x in range(0,5001):
    random_num = random.random()
    toss = round(random_num)
    if toss == 0:
        headcnt += 1
        print("Attempt #", x,  "Throwing a coin... It's a head! ... Got ", headcnt, "head(s) so far and ", tailcnt, " tail(s) so far")
    else:
        tailcnt += 1
        print("Attempt #", x,  "Throwing a coin... It's a tail! ... Got ", headcnt, "head(s) so far and ", tailcnt, " tail(s) so far")
