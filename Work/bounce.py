# bounce.py
#
# Exercise 1.5

day = 0
height = 100
factor = 3/5
while day < 10:
    day = day + 1
    height *= factor
    print(day, round(height, 4))
