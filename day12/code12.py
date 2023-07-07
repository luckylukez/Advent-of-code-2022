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
print('X: ', X)
print('Y: ', Y)

height_map = np.zeros((X,Y))
starting_positions = []

for i in range(X):
    for j in range(Y):
        height_map[i,j] = get_char_value(lines[i][j])
        if height_map[i,j] == 1 or height_map[i,j] == 0:
            starting_positions.append(np.array((i,j)))
print('Number of starting positions: ', len(starting_positions))
#print(height_map)

visited = np.zeros((X,Y))
moves = np.array([(1,0),(-1,0),(0,1),(0,-1)])

(x_start, y_start) = np.where(height_map == 0)
x_start = x_start[0]
y_start = y_start[0]

print('First start position: ', x_start, y_start)

start_pos = np.array((x_start, y_start))
start_path = [start_pos]
queue = [start_path]

final_path = []
visited_nr = 0

while len(queue) > 0:
    path = queue.pop(0)
    pos = path[-1]
    if visited[pos[0], pos[1]] == 1:
        continue 
    else:
        visited[pos[0], pos[1]] = 1
        visited_nr += 1
        if visited_nr % 1000 == 0:
            print('Nodes visited: ', visited_nr)

        is_start_pos = height_map[pos[0], pos[1]] == 1 or height_map[pos[0], pos[1]] == 0
        if is_start_pos: # If we traverse through a starting position, set it to new start position.
            path = [pos] # If we traverse through


    if height_map[pos[0], pos[1]] == 27:
        final_path = path
        break

    for move in moves:
        next_pos = pos + move
        (x_next, y_next) = next_pos

        in_bounds = x_next  >= 0 and x_next < X and y_next >= 0 and y_next < Y
        if not in_bounds:
            continue

        next_pos_visited = visited[next_pos[0], next_pos[1]] == 1
        legal_move = height_map[next_pos[0], next_pos[1]] <= height_map[pos[0], pos[1]] + 1

        if  not next_pos_visited and legal_move:
            new_path = copy.copy(path)
            new_path.append(next_pos)
            queue.append(new_path)

#print(final_path)
print('Total nodes visited: ', visited_nr)
print('Shortest amount of steps to goal from a start position: ', len(final_path) - 1) # The number of steps is the length of the path - 1




