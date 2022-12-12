import os
import re

# file = open(os.path.join(".", "day5", "sample.txt"))
file = open(os.path.join(".","day5","input.txt"))

list_of_stacks = [[], [], [], [], [], [], [], [], []]

for line in file:
    counter = 0
    if line == "\n":
        break
    while len(line) > 0:
        if line.startswith(" "):
            line = line[4:]
            counter += 1
        elif line.startswith("["):
            temp = list_of_stacks[counter]
            temp.append(line[1])
            line = line[4:]
            counter += 1

for stack in list_of_stacks:
    stack.reverse()

for line in file:
    temp = re.findall(r"\d+", line)
    values = list(map(int, temp))
    crane = []
    for i in range(values[0]):
        crane.append(list_of_stacks[values[1] - 1].pop())
    for i in range(values[0]):
         list_of_stacks[values[2] - 1].append(crane.pop())

result = ""
for stack in list_of_stacks:
    if(len(stack) != 0):
        result += stack.pop()

print(result)
