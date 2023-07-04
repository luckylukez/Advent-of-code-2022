import math

# Each ape has:
# a worry function
# a queue of objects
# a division number and two other monkies to throw to

# Check if eval works and if div_nr works

class Monkey():
    def __init__(self, start_items, worry_func, div_nr, peer_numbers):
        self.items = start_items
        self.worry_func = worry_func
        self.div_nr = div_nr
        self.peer_numbers = peer_numbers
        self.peers = None
        self.inspections = 0

with open('data.txt', 'r') as data:
    lines = [line.strip().split(' ') for line in data.readlines()]

monkeys = []


i = 0
while i < len(lines):
    print(lines[i][0])
    if lines[i][0] == 'Monkey':
        print('here!')
        # object queue:
        i += 1
        start_queue = [int(s.replace(',','')) for s in lines[i][2:]]

        # worry function
        i += 1
        func_chars = lines[i][-3:]
        func_text = ''
        for char in func_chars:
            func_text = func_text + char
        worry_function = lambda old : eval(func_text)

        i += 1
        div_nr = int(lines[i][-1])

        i += 1
        m1 = int(lines[i][-1])
        i += 1
        m2 = int(lines[i][-1])
        peer_numbers = (m1, m2)

        monkeys.append(Monkey(start_queue, worry_function, div_nr, peer_numbers))

    i += 1

print('Monkeys: ')
print(monkeys)

for monkey in monkeys:
    monkey.peers = [monkeys[peer_nr] for peer_nr in monkey.peer_numbers]

for i in range(20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            worry_lvl = monkey.items.pop(0)
            monkey.inspections += 1
            worry_lvl = math.floor(worry_lvl / 3)
            if worry_lvl % monkey.div_nr == 0:
                monkey.peers[0].items.append(worry_lvl)
            else:
                monkey.peers[1].items.append(worry_lvl)


inspectionss = [monkey.inspections for monkey in monkeys]
print('Inspections: ', inspectionss)
import numpy as np
m1 = max(inspectionss)
max_ind = np.argmax(inspectionss)
inspectionss.pop(max_ind)
m2 = max(inspectionss)
print(m1*m2)

#monkey_business = inspectionss[-1] * inspectionss[-2]
#print(monkey_business)













# Calculate moneky business!!
