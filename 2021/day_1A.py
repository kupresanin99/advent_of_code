my_list = open('day_1.txt', 'r').read().split('\n')
a = 100000  # arbitrary dummy large number
b = 100000  # arbitrary dummy large number
my_counter = 0
for reading in my_list:
  a = b
  b = int(reading)
  if b > a:
    my_counter += 1
print(my_counter)