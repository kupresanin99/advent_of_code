# part 1

import re
f = open("day_7.txt", "r")
whole_file = f.read()
f.close()
chunks = re.split('\n', whole_file)
new_chunks1 = [re.split(' bags contain ', x) for x in chunks]
new_chunks2 = [[x[0], re.split(', ', x[1])] for x in new_chunks1]

my_dict = {}
for x in new_chunks2:
    value_list = []
    for y in x[1]:
        z = ''.join([i for i in y if not i.isdigit()]).split()

        value_list.append(' '.join(z[:-1]))
    my_dict.update({x[0]:value_list})

print(my_dict)