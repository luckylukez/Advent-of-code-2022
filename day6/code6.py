import itertools

with open('data.txt', 'r') as data:
    string = data.read()

print(string[:4])

last_three = ['m', 'z', 'r']

def has_no_duplicate(l):
    for a,b in itertools.combinations(l,2):
        if a == b:
            return False
    return True

ind = 0
for i in range(len(string)):
    if has_no_duplicate(string[i:i+4]):
        ind = i+3
        break
    i += 1

print(ind)

ind = 0
for i in range(len(string)):
    if has_no_duplicate(string[i:i+14]):
        ind = i+14
        break
    i += 1

print(ind)
    