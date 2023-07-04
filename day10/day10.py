import numpy as np
import copy

with open('data.txt', 'r') as data:
    lines = [line.strip().split(' ') for line in data.readlines()]

display = np.zeros(240, dtype=int)
print(display)

def update_display(t, sprite):
    if t%40 in sprite:
        display[t] = 1

def int_to_string(i):
    if i == 1:
        return '#'
    return '.'

def show(display):
    d = np.reshape(copy.copy(display), (6,40))
    for l in d:
        p="".join([int_to_string(i) for i in l.tolist()])
        print(p)
    print(d)

t = 0
val = 1
sum = 0
vals = []
for line in lines:
    
    sprite = [val-1,val,val+1]
    update_display(t, sprite)

    t += 1
    if t%40 == 20:
        sum += t*val
    
    if line[0] != 'noop':
        sprite = [val-1,val,val+1]
        update_display(t, sprite)

        t += 1
        if t%40 == 20:
            sum += t*val
        val += int(line[1])
        vals.append(val)
    print('---------------------------------------------------')
    show(display)
print(sum)

x = 40
y = 6
print(max(vals))






