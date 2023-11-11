my_list = list(range(0, 100))

new_list = [item * 2 for item in my_list]
new_list = list(map(lambda x: x * 2, my_list))

data_list = [(i, j) for i in range(100) for j in range(100)]
for value in data_list:
    print(value[0], value[1])


from itertools import product
data_list = list(product(range(100), repeat=2))
for value in data_list:
    print(value[0], value[1])
