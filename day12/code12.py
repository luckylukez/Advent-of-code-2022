import numpy as np
import copy

def get_char_value(character):
    if character == 'E':
        return 27
    if character == 'S':
        return 0
    if character.isupper():
        return ord(character) - 38
    return ord(character)  - 96

with open('data.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

X = len(lines)
Y = len(lines[0])

height_map = np.zeros((X,Y))

for i in range(X):
    for j in range(Y):
        height_map[i,j] = get_char_value(lines[i][j])

visited = np.zeros((X,Y))

(x_start, y_start) = np.where(height_map==0)
x_start = x_start[0]
y_start = y_start[0]
print(x_start, y_start)

print(get_char_value('E')) # set to 27
print(get_char_value('a'))
print(get_char_value('z'))

class SearchStep():
    def __init__(self, path, ):
        pass

start_path = []
queue = []
iteration = 0
height  = 1

start_pos = np.array((x_start, y_start))
moves = np.array([(1,0),(-1,0),(0,1),(0,-1)])
print(moves)
print(moves[0])

start_path.append(start_pos)
queue.append(start_path)

while len(start_path) > 0:
    pos = copy.copy(start_path)




