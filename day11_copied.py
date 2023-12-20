file = open('day11.txt', 'r')


empty_cols = [26, 42, 55, 62, 71, 78, 80, 102, 106, 118]

gal_dict = {}
current = 1
row_num = 1
for row in file.readlines():
    row = row.rstrip("\n")
    
    for i, char in enumerate(list(row)):
        if char == '#':
            gal_dict[str(current)] = (row_num, i+1)
            current += 1
    if '#' not in row:
        row_num += 1000000
    else:
        row_num += 1

print(gal_dict)
        

for i in empty_cols[::-1]:
    for key, val in gal_dict.items():
        if val[1] > i:
            gal_dict[key] = (val[0], val[1]+1000000)

# print(gal_dict)

dist_dict = {}

for key, val in gal_dict.items():

    for other_key, other_val in gal_dict.items():
        temp = sorted([int(key), int(other_key)])
        temp = [str(i) for i in temp]
        label = " ".join(temp)
        if key == other_key:
            pass
        elif label in dist_dict.keys():
            pass
        else:
            x_vals = sorted([val[1], other_val[1]])
            y_vals = sorted([val[0], other_val[0]])
            distance = (x_vals[1]-x_vals[0]) + (y_vals[1]-y_vals[0])
            dist_dict[label] = distance

# print(dist_dict)

print(sum(dist_dict.values()))
