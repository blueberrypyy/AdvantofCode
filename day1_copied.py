file = open('day1.txt', 'r')

'''
total = 0

for row in file.readlines():
    nums = []
    for i in list(str(row)):
        if i.isnumeric():
            nums.append(i)    
            res = f"{nums[0]}{nums[-1]}"
    total += int(res)

print(total)
'''
