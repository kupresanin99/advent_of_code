f = open("day_2.txt", "r")
good_passwords = 0
bad_passwords = 0
for line in f.readlines():
    part1 = line.split(' ')
    part2 = part1[0].split('-')
    my_min = int(part2[0])
    my_max = int(part2[1])
    my_char = part1[1][0]
    my_pass = part1[2].strip()
    if my_pass.count(my_char) in range(my_min, my_max + 1):
        good_passwords += 1
    else:
        bad_passwords += 1
print(f"We have {good_passwords} good passwords and {bad_passwords} bad passwords")

f = open("day_2.txt", "r")
good_passwords = 0
bad_passwords = 0

for line in f.readlines():
    part1 = line.split(' ')
    part2 = part1[0].split('-')
    my_min = int(part2[0])
    my_max = int(part2[1])
    my_char = part1[1][0]
    my_pass = part1[2].strip()
    target = 0
    if my_pass[my_min - 1] == my_char:
        target += 1
    if my_pass[my_max - 1] == my_char:
        target += 1
    if target == 1:
        good_passwords += 1
    else:
        bad_passwords += 1
print(f"We have {good_passwords} good passwords and {bad_passwords} bad passwords")
