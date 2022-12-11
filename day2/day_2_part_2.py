# file = open(".\day2\sample.txt")
file = open(".\day2\input.txt")

# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 

# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

sum = 0
move_points = {"X": 0, "Y": 3, "Z": 6}
opponent_list = ["A", "B", "C"]
for line in file:
    round = 0
    split_line = line.rstrip().split(" ")
    round += move_points[split_line[1]]
    index = list(move_points).index(split_line[1])
    opponent_index = opponent_list.index(split_line[0])
    if(index == 0):
        if(opponent_index == 0):
            opponent_index = 3
        round += opponent_index
    elif(index == 1):
        round += opponent_index + 1
    else:
        if(opponent_index == 2):
            opponent_index = -1
        round += opponent_index + 2
    sum += round

print(sum)
