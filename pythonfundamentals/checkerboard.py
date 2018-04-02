# Write a program that prints a 'checkerboard' pattern to the console. 8x8
trigger = 1
for x in range(0, 9):
    if trigger == 1:
        print("*&*&*&*&")
        trigger = 0
    else:
        print("&*&*&*&*")
        trigger = 1
