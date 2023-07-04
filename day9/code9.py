import numpy as np
import copy

class Rope():
    def __init__(self):
        self.head = np.array([0,0])
        self.tail = copy.copy(self.head)
        self.visited = np.zeros((1000,1000))
        self.visited[0,0] = 1


    def move_head(self, move):
        # print('head: ' + str(self.head))
        self.head = self.head + move
        # print('head after move: ' + str(self.head))
        self.move_tail()

    def move_tail(self):
        # print('tail: ' + str(self.tail))
        diff = self.head - self.tail
        # print('diff: ', diff)
        signs = np.sign(diff)
        # print('signs: ')
        # print(signs)
        # print('diff: ', diff)
        # print('max of diff: ', np.max(diff))
        # print('abs of max of diff: ', abs(np.max(diff)))
        if np.max(np.abs(diff)) <= 1:
            # print('bajs')
            pass
        else:
            self.tail = self.tail + signs
        self.visited[self.tail[0], self.tail[1]] = 1
        # print('tail after move: ' + str(self.tail))


with open('data.txt', 'r') as data:
    lines = [line.strip().split(' ') for line in data.readlines()]



rope = Rope()

for line in lines:
    match line[0]:
        case 'R':
            move = np.array([1,0])
        case 'L':
            move = np.array([-1,0])
        case 'U':
            move = np.array([0,1])
        case 'D':
            move = np.array([0,-1])
    # print('move: ')
    # print(move)

    for i in range(int(line[1])):
        # print('i: ' + str(i))
        rope.move_head(move)

print(np.sum(rope.visited))


class LongRope():
    def __init__(self):
        self.body = np.zeros((10,2))
        self.visited = np.zeros((1000,1000))
        self.visited[0,0] = 1


    def move_head(self, move):
        self.body[0] = self.body[0] + move
        for i in range(1,len(self.body)):
            self.move_tail(i)

    def move_tail(self, i):
        diff = self.body[i-1] - self.body[i]
        signs = np.sign(diff)
        if np.max(np.abs(diff)) <= 1:
            pass
        else:
            self.body[i] = self.body[i] + signs
        if i == 9:
            self.visited[int(self.body[i,0]), int(self.body[i,1])] = 1

long_rope = LongRope()

for line in lines:
    match line[0]:
        case 'R':
            move = np.array([1,0])
        case 'L':
            move = np.array([-1,0])
        case 'U':
            move = np.array([0,1])
        case 'D':
            move = np.array([0,-1])

    for i in range(int(line[1])):
        long_rope.move_head(move)

print(np.sum(long_rope.visited))


            

        