import os
# file = open(os.path.join(".","day1","sample.txt"))
file = open(os.path.join(".","day2","input.txt"))

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

sum = 0
move_points = {"X": 1, "Y": 2, "Z": 3}
opponent_list = ["A", "B", "C"]
for line in file:
    round = 0
    split_line = line.rstrip().split(" ")
    round += move_points[split_line[1]]
    index = list(move_points).index(split_line[1])
    opponent_index = opponent_list.index(split_line[0])
    if(index == opponent_index):
        round+=3
    elif(index - 1 == opponent_index or (index == 0 and opponent_index == 2)):
        round+=6
    sum += round

print(sum)
