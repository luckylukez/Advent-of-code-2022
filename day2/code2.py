def calculate_score(opponent_move, my_move):
    score = 0

    match (my_move - opponent_move)%3:
        case 1:
            score += 6
        case 0: 
            score += 3

    score += (my_move+1)
    return score


def main():
    with open('strategy.txt', 'r') as strategy:
        lines = strategy.readlines()

    column_1 = []
    column_2 = []

    for line in lines:
        [a, b] = line.split(' ')
        match a:
            case 'A':
                column_1.append(0)
            case 'B':
                column_1.append(1)
            case 'C':
                column_1.append(2)
        match b.strip():
            case 'X':
                column_2.append(0)
            case 'Y':
                column_2.append(1)
            case 'Z':
                column_2.append(2)

    my_actual_moves = [((column_2[i]-1)+column_1[i])%3 for i in range(len(column_1))]

    sum = 0
    sum2 = 0
    for i in range(len(column_1)):
        sum += calculate_score(column_1[i], column_2[i])
        sum2 += calculate_score(column_1[i], my_actual_moves[i])
    print(sum)
    print(sum2)


    print()

if __name__ == '__main__':
    main()