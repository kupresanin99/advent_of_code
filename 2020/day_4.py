# part 1

import re
f = open("day_4.txt", "r")
whole_file = f.read()
f.close()
#print(whole_file)
chunks = re.split('\n\n', whole_file)
chunks = [re.sub(r'\n', ' ', x) for x in chunks]
good_ones = [int("byr:" in x) * int("iyr:" in x) * int("eyr:" in x) * int("hgt:" in x) * int("hcl:" in x) * int("ecl:" in x) * int("pid:" in x) for x in chunks]
print(f"part 1 we have {sum(good_ones)} candidate passports")

# part 2
merged = list(zip(chunks, good_ones))
merged = [x[0] for x in merged if x[1] == 1]
list_of_dicts = []
for str in merged:
    try:
        list_of_dicts.append(dict(x.split(":") for x in str.split(" ")))
    except:
        None

for byr in list_of_dicts:
    if int(byr['byr']) not in range(1920, 2003):
        list_of_dicts.remove(byr)

for iyr in list_of_dicts:
    if int(iyr['iyr']) not in range(2010, 2021):
        list_of_dicts.remove(iyr)

for eyr in list_of_dicts:
    if int(eyr['eyr']) not in range(2020, 2031):
        list_of_dicts.remove(eyr)

for ecl in list_of_dicts:
    if (ecl['ecl']) not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        list_of_dicts.remove(ecl)

for hcl in list_of_dicts:
    if not re.match("#[0-9a-f]{6}", hcl['hcl']):
        list_of_dicts.remove(hcl)

for pid in list_of_dicts:
    if not re.match("[0-9]{9}", pid['pid']):
        list_of_dicts.remove(pid)

for hgt in list_of_dicts:
    if 'cm' in hgt['hgt']:
        if int(hgt['hgt'][:-2]) not in range(150, 194):
            list_of_dicts.remove(hgt)

for hgt in list_of_dicts:
    if 'in' in hgt['hgt']:
        if int(hgt['hgt'][:-2]) not in range(59, 77):
            list_of_dicts.remove(hgt)

for hgt in list_of_dicts:
    if 'cm' not in hgt['hgt']:
        if 'in' not in hgt['hgt']:
            list_of_dicts.remove(hgt)
print(f"part 2 we have {len(list_of_dicts)} candidate passports")
