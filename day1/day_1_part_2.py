import os
# file = open(os.path.join(".","day1","sample.txt"))
file = open(os.path.join(".","day1","input.txt"))

most_food = []
counter = 0
for line in file:
    if(line == '\n'):
        most_food.append(counter)
        counter = 0
    else:
        counter += int(line.rstrip())

if(counter != 0):
    most_food.append(counter)
    counter = 0 

most_food = sorted(most_food, reverse=True)
most_food_total = 0
for food in most_food[0:3]:
    most_food_total += food
print(most_food_total)