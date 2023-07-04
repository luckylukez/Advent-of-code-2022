import numpy as np

def get_char_value(character):
    if character.isupper():
        return ord(character) - 38
    return ord(character)  - 96

def find_duplicate(line):
    i_end = int(len(line)/2)
    j_start = int(len(line)/2)
    print(i_end)
    print(j_start)
    for c1 in line[:i_end]:
        for c2 in line[j_start:]:
            if c1 == c2:  
                #print(f'Returning line {(i,j)}.')
                return c1
            
with open('day3/input.txt', 'r') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    line.strip()
    print(len(line))
    duplicate = find_duplicate(line)
    sum += get_char_value(duplicate)

# print(sum)
# print(get_char_value('a'))
# print(get_char_value('A'))

characters = [chr(i) for i in range(97,122)]
Characters = [chr(i) for i in range(65,90)]
characters.extend(Characters)

sum = 0

# i = 0
# while i < len(lines):
#     characters = [chr(i) for i in range(97,123)]
#     Characters = [chr(i) for i in range(65,91)]
#     characters.extend(Characters)
    
#     for j in range(3):
#         print(characters)
#         print(lines[i+j])
#         for char in characters:
#             for elv_char in lines[i+j]
#                 if char not:
#                     characters.remove(char)
#         print(characters)
            
#     i += 3
#     print(i)
#     print(len(characters))
#     assert(len(characters) == 1)

#     sum += get_char_value(characters[0])

sum = 0
i = 0
while i < len(lines):

    def calc(i):
        for c1 in lines[i]:
            for c2 in lines[i+1]:
                for c3 in lines[i+2]:
                    if c1 == c2 and c1 == c3:
                        return c1
    
    char = calc(i)
    sum += get_char_value(char)
    i += 3
print(sum)

        



        



         

