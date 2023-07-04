with open('./calories.txt', 'r') as calories:
    lines = calories.readlines()
    
sums = []
_sum = 0
for line in lines:
    if line == '\n':
        sums.append(_sum)
        _sum = 0
    else:
        _sum += int(line)
print(max(sums))
sums.sort()
print(sum(sums[-3:]))

