my_list = open('day_1.txt', 'r').read().split('\n')

output_1 = [f"x = {x}, y = {y}, sum = {int(x) + int(y)}, product = {int(x) * int(y)}"
 for x in my_list for y in my_list if int(x) + int(y) == 2020][0]

output_2 = [f"x = {x}, y = {y}, z = {z}, sum = {int(x) + int(y) + int(z)}, product = {int(x) * int(y) * int(z)}"
 for x in my_list for y in my_list for z in my_list if int(x) + int(y) + int(z) == 2020][0]

print(output_1)
print(output_2)
