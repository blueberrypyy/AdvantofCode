line_count = 0

with open('day3.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        line_count += 1

        if line_count > 30: 
            break
        else:

            for char in line:
                if char.isnumeric():
                    print(char, line.index(char))
                elif char != '.':
                    print('symbol', char, line.index(char))







sample = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
