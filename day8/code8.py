import numpy as np

with open('data.txt', 'r') as data:
    lines = [[*line.strip()] for line in data.readlines()]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        lines[i][j] = int(lines[i][j])



I = len(lines)
J = len(lines[0])

booleans = np.zeros((I,J))

for i in range(I):
    j = 0
    h = -1
    while h < 9 and j < J:
        if lines[i][j] > h:
            booleans[i,j] = 1
            h = lines[i][j]
        j += 1

    j = J-1
    h = -1
    while h < 9 and j >= 0:
        if lines[i][j] > h:
            booleans[i,j] = 1
            h = lines[i][j]
        j -= 1

for j in range(J):
    i = 0
    h = -1
    while h < 9 and i < I:
        if lines[i][j] > h:
            booleans[i,j] = 1
            h = lines[i][j]
        i += 1

    i = I-1
    h = -1
    while h < 9 and i >= 0:
        if lines[i][j] > h:
            booleans[i,j] = 1
            h = lines[i][j]
        i -= 1

print(booleans)

print(np.sum(booleans))

I = len(lines)
J = len(lines[0])
scores = np.zeros((I,J))
for i in range(1,I-1):
    for j in range(1,J-1):

        jj = j-1
        s1 = 1
        while jj > 0 and lines[i][jj] < lines[i][j]:
            s1 += 1
            jj -= 1

        jj = j+1
        s2 = 1
        while jj < J-1 and lines[i][jj] < lines[i][j]:
            if i == 1 and j == 2:
                print('jj:')
                print(s2)
                print(jj)
            s2 += 1
            jj += 1

        ii = i-1
        s3 = 1
        while ii > 0 and lines[ii][j] < lines[i][j]:
            s3 += 1
            ii -= 1
            if i == 1 and j == 2:
                print('only s3:')
                print(i)
                print(s3)

        ii = i+1
        s4 = 1
        while ii < I-1 and lines[ii][j] < lines[i][j]:
            s4 += 1
            ii += 1
        if i == 1 and j == 2:
                print('all of the s:')
                print(s1)
                print(s2)
                print(s3)
                print(s4)
        scores[i,j] = s1*s2*s3*s4

for line in lines:
    print(line)
for score in scores:
    print(score)


amax = np.unravel_index(scores.argmax(), scores.shape)
print(scores[amax])
print(np.max(scores))
        
    

