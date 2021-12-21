my_list = open('day_1.txt', 'r').read().split('\n')
a = 0
b = 0
c = 0
my_results = []
my_counter = 0
for reading in my_list:  # This loop collects sums of 3 elements into a list
  my_counter += 1
  a = b
  b = c
  c = int(reading)
  if my_counter >= 3:
    my_results.append(a + b + c)

a = 100000  # arbitrary dummy large number
b = 100000  # arbitrary dummy large number
my_counter = 0
for num in my_results:  # And this loop checks for increasing, element by element
  a = b
  b = int(num)
  if b > a:
    my_counter += 1
print(my_counter)




