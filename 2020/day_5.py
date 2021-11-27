# part 1
f = open("day_5.txt", "r")
my_counter = 0
max_id = 0
my_seat_list = []
for line in f.readlines():
    binary1 = line.strip()[:7].replace('F', '0').replace('B', '1')
    binary2 = line.strip()[7:].replace('L', '0').replace('R', '1')
    my_row = 0
    my_seat = 0
    exponent1 = 6
    exponent2 = 2
    for bit in binary1:
        my_row += 2 ** exponent1 * int(bit)
        exponent1 -= 1
    for bit in binary2:
        my_seat += 2 ** exponent2 * int(bit)
        exponent2 -= 1
    my_seat_list.append((f"""{binary1} is row {my_row} and {binary2} is seat {my_seat} with id {8 * my_row + my_seat}""", 8 * my_row + my_seat))
    if 8 * my_row + my_seat > max_id:
        max_id = 8 * my_row + my_seat
print(f"The max id is {max_id}")
def takeSecond(elem):
    return elem[1]
my_seat_list.sort(key=takeSecond)
my_num = 37
for seat in my_seat_list:
    print(seat[0], seat[1], seat[1] - my_num)
    my_num += 1