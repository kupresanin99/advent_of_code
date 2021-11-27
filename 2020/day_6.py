# part 1

import re
f = open("day_6.txt", "r")
whole_file = f.read()
f.close()
chunks = re.split('\n\n', whole_file)
chunks = [len(set(re.sub(r'\n', '', x))) for x in chunks]
print(sum(chunks))

# part 2
f = open("day_6.txt", "r")
whole_file = f.read()
f.close()
chunks = re.split('\n\n', whole_file)
chunks = [re.sub(r'\n', ' ', x) for x in chunks]
sum_of_intersection = 0
for chunk in chunks:
    sum_of_intersection += len(set.intersection(*[set(x) for x in chunk.split()]))
print(sum_of_intersection)

