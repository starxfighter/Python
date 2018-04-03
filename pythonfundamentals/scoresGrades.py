# Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
# your function should display what the grade is for a particular score.

import random
import math
print("Scores and Grades")
for x in range(0,11):
    random_num = random.random() * 100
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
    grade = math.floor(random_num)
    if grade < 60:
        print("Score: ", grade, "Your grade is F")
    elif grade >= 60 and grade <=69:
        print("Score: ", grade, "Your grade is D")
    elif grade >=70 and grade <=79:
        print("Score: ", grade, "Your grade is C")
    elif grade >=80 and grade <=89:
        print("Score: ", grade, "Your grade is B")
    elif grade >=90 and grade <=100:
        print("Score: ", grade, "Your grade is A")
print("End of Program")
