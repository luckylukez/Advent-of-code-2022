#     [B]             [B] [S]        
#     [M]             [P] [L] [B] [J]
#     [D]     [R]     [V] [D] [Q] [D]
#     [T] [R] [Z]     [H] [H] [G] [C]
#     [P] [W] [J] [B] [J] [F] [J] [S]
# [N] [S] [Z] [V] [M] [N] [Z] [F] [M]
# [W] [Z] [H] [D] [H] [G] [Q] [S] [W]
# [B] [L] [Q] [W] [S] [L] [J] [W] [Z]
#  1   2   3   4   5   6   7   8   9 
crates = {1 : 'BWN',
          2 : 'LZSPTDMB',
          3 : 'QHZWR',
          4 : 'WDVJZR',
          5 : 'SHMB',
          6 : 'LGNJHVPB',
          7 : 'JQZFHDLS',
          8 : 'WSFJGQB',
          9 : 'ZWMSCDJ'}

for key in crates.keys():
    crates[key] = [*crates[key]]

with open('data.txt', 'r') as data:
    lines = data.readlines()

for ind, line in enumerate(lines):
    line = line.strip()
    line = line.split(' ')
    line.pop(4)
    line.pop(2)
    line.pop(0)
    lines[ind] = line

# for line in lines:
#     for i in range(int(line[0])):
#         moving_crate = crates[int(line[1])].pop()
#         crates[int(line[2])].append(moving_crate)

for line in lines:
    nr_moving = int(line[0])
    _from = int(line[1])
    _to = int(line[2])
    moving_crates = []
    for i in range(nr_moving):
        moving_crates.append(crates[_from].pop())
    for i in range(nr_moving):
        crates[_to].append(moving_crates.pop())
    

def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        new += x
 
    # return string
    return new

ans = [crates[i][-1] for i in range(1,10)]
ans = convert(ans)
print(ans)




