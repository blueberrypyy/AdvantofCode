
# 12 red cubes, 13 green cubes, and 14 blue cubes
max_color_dict = {
        'red': 12,
        'green': 13,
        'blue': 14
        }
game_ids = list()

with open('day2.txt', 'r') as puzzle_input:

    for line in puzzle_input:
        possible = True
        line = line.rstrip()
        colon = line.find(':')
        game_id = line[:colon].split()[1]

        revealed = line[colon+1:].split(';')
        cubes_revealed_dict = dict() 

        # loop through revealed cubes
        for cube in revealed:
            for item in cube.split(','):
                amount, color = item.split()
                cubes_revealed_dict[color] = int(amount)

            # Compare current dictionary values with max values and print out results
            for key, value in cubes_revealed_dict.items():
                if max_color_dict[key] < value:
                    possible = False
                    continue

        if possible:
            game_ids.append(int(game_id))


print('Sum of all game ids:', sum(game_ids))                
#sum is 2285


