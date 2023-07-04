import os

def has_contained_partner(line):
    [r1,r2] = line.split(',')
    r1 = r1.strip().split('-')
    r2 = r2.strip().split('-')
    r1 = [int(chr) for chr in r1]
    r2 = [int(chr) for chr in r2]
    return contains(r1, r2) or contains(r2, r1)

def has_overlap(line):
    [r1,r2] = line.split(',')
    r1 = r1.strip().split('-')
    r2 = r2.strip().split('-')
    r1 = [int(chr) for chr in r1]
    r2 = [int(chr) for chr in r2]
    return overlap(r1,r2)

def contains(r1,r2):
    return  r1[0] <= r2[0] and r1[1] >= r2[1]

def overlap(r1,r2):
    print(r1)
    print(r2)
    print( not (r1[1] < r2[0] or r2[1] < r1[0]))
    print('#######################')
    return not (r1[1] < r2[0] or r2[1] < r1[0])
    
print(os.getcwd())

with open('data.txt', 'r') as data:
    lines = data.readlines()

nr = 0
nr2 = 0
for line in lines:
    line.strip()
    if has_contained_partner(line):
        nr += 1
    if has_overlap(line):
        nr2 += 1

print(nr)
print(nr2)




