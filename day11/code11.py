import math
import numpy as np

# Each ape has:
# a worry function
# a queue of objects
# a division number and two other monkies to throw to

# Check if eval works and if div_nr works

# 

class Monkey():
    def __init__(self, monkey_nr, start_items, div_nr, peer_numbers, func_text):#, function_strings):
        self.monkey_nr = monkey_nr
        self.items = start_items
        #self.function_strings = function_strings
        self.worry_func = lambda old : eval(function_strings[self.monkey_nr])
        self.div_nr = div_nr
        self.peer_numbers = peer_numbers
        self.peers = None
        self.inspections = 0
        self.func_text = func_text

with open('data.txt', 'r') as data:
    lines = [line.strip().split(' ') for line in data.readlines()]

# lines = lines[:3*7-1]

# for line in lines:
#     print(line)

monkeys = []
function_strings = {}


i = 0
while i < len(lines):
    if lines[i][0] == 'Monkey':
        # print('##########################################################')
        # print(f'monkey {len(monkeys)}:')
        # object queue:
        monkey_nr = int(lines[i][-1][:-1])

        i += 1
        start_queue = [int(s.replace(',','')) for s in lines[i][2:]]
        # print('start items:', start_queue)

        # worry function
        i += 1
        func_chars = lines[i][-3:]
        func_text = ''
        for char in func_chars:
            func_text = func_text + char + ' '
        # print('functions: ', func_text)

        i += 1
        div_nr = int(lines[i][-1])
        # print('div nr: ', div_nr)
        i += 1
        m1 = int(lines[i][-1])
        i += 1
        m2 = int(lines[i][-1])
        peer_numbers = (m1, m2)
        # print('peer numbers: ', peer_numbers)

        monkeys.append(Monkey(monkey_nr, start_queue, div_nr, peer_numbers, func_text))
        function_strings[monkey_nr] = func_text

    i += 1

func_text = 'old + 1'
# print('Function_text: ', func_text)

# print('Monkeys: ')
# print(monkeys)

for i, monkey in enumerate(monkeys):
    monkey.peers = [monkeys[peer_nr] for peer_nr in monkey.peer_numbers]

prime_factors = [2,3,5,7,11,13,17,19]
factor_product = np.prod(prime_factors)
print('factor product: ', factor_product)
bigger_prime_factors = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in range(10000):
    if i%100 == 0:
        print('iteration', i)
        for monkey in monkeys:
            print(monkey.items)
    for monkey in monkeys:
        # print('####################################################################')
        # print(f'Monkey {monkeys.index(monkey)}')
        while len(monkey.items) > 0:
            worry_lvl = monkey.items.pop(0)
            #print(f'Monkey inspects an item with a worry level of {worry_lvl}')
            worry_lvl = monkey.worry_func(worry_lvl)
            if worry_lvl >= factor_product:
                worry_lvl -= factor_product
            # for factor in bigger_prime_factors:
            #     if worry_lvl % factor == 0:
            #         worry_lvl = worry_lvl / factor
            # print(f'worry lvl is changed by {monkey.func_text} to {worry_lvl}')
            monkey.inspections += 1
            # worry_lvl = math.floor(worry_lvl / 3)
            # print(f'Monkey gets bored with item. Worry level is divided by 3 to {worry_lvl}.')
            if worry_lvl % monkey.div_nr == 0:
                # print(f'Current worry level IS not divisible by {monkey.div_nr}.')
                monkey.peers[0].items.append(worry_lvl)
            else:
                monkey.peers[1].items.append(worry_lvl)
                # print(f'Current worry level IS NOT not divisible by {monkey.div_nr}.')


inspectionss = [monkey.inspections for monkey in monkeys]
inspectionss.sort()
print(inspectionss)
# print('Inspections: ', inspectionss)
# import numpy as np
# m1 = max(inspectionss)
# max_ind = np.argmax(inspectionss)
# inspectionss.pop(max_ind)
# m2 = max(inspectionss)
# print(m1*m2)

monkey_business = inspectionss[-1] * inspectionss[-2]
print(monkey_business)













# Calculate moneky business!!
