# part 1

# f = open("day_3.txt", "r")
# line_counter = 0
# num_trees = 0
# for line in f.readlines():
#     line_counter += 1
#     print(f"We're on row number {line_counter}")
#     new_line = line.strip() * 100
#     print(new_line)
#     print()
#     if line_counter == 1:
#         print("First line")
#     else:
#         if new_line[3 * (line_counter - 1)] == '#':
#             num_trees += 1
#             print(f"Tree number {num_trees}!")

# part 2

f = open("day_3.txt", "r")
line_counter = 0
num_trees_1 = 0
num_trees_2 = 0
num_trees_3 = 0
num_trees_4 = 0
num_trees_5 = 0
for line in f.readlines():
    line_counter += 1
    print(f"We're on row number {line_counter}")
    new_line = line.strip() * 100
    print(new_line)
    print()
    if line_counter == 1:
        print("First line")
    else:
        if new_line[1 * (line_counter - 1)] == '#':
            num_trees_1 += 1
        if new_line[3 * (line_counter - 1)] == '#':
            num_trees_2 += 1
        if new_line[5 * (line_counter - 1)] == '#':
            num_trees_3 += 1
        if new_line[7 * (line_counter - 1)] == '#':
            num_trees_4 += 1
        if line_counter % 2 == 1:
            if new_line[1 * (line_counter - 2)] == '#':
                num_trees_5 += 1

print(num_trees_1, num_trees_2, num_trees_3, num_trees_4, num_trees_5)
print(num_trees_1 * num_trees_2 * num_trees_3 * num_trees_4 * num_trees_5)
























