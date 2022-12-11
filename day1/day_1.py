import os
# file = open(os.path.join(".","day1","sample.txt"))
file = open(os.path.join(".","day1","input.txt"))

most_food = 0
counter = 0
for line in file:
    if(line == '\n'):
        if counter > most_food:
            most_food = counter
        counter = 0
    else:
        counter += int(line.rstrip())

print(most_food)