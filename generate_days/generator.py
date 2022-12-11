import os


f = open("day/day_x.py", "r")
template_text = f.read()
print(template_text)

for i in range(1, 32):
    file_text = template_text.replace('dayx', 'day'+str(i))
    path = '../day'+str(i)
    
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(path + '/day_'+str(i)+'.py'):
        output = open(path + '/day_'+str(i)+'.py', "w")
        output.write(file_text)
        output.close()

    if not os.path.exists(path + '/day_'+str(i)+'_part_2.py'):
        output = open(path + '/day_'+str(i)+'_part_2.py', "w")
        output.write(file_text)
        output.close()

    if not os.path.exists(path + '/input.txt'):
        open(path + '/input.txt', 'a').close()

    if not os.path.exists(path + '/sample.txt'):
        open(path + '/sample.txt', 'a').close()

    pass