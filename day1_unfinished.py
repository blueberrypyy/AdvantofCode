
def part1():
    master_list = list()
    counts = 0

    with open('day1.txt', 'r') as puzzle_input:
        for line in puzzle_input:
            if counts > 100000000:
                break
            else:
                counts += 1
                nums = []

                for char in line:
                    if char.isnumeric():
                        nums.append(char)

                if len(nums) < 2:
                    try: final_num = str(nums[0]) + str(nums[0])
                    except: pass
                else:
                    final_num = str(nums[0]) + str(nums[-1])

                #print('line:', counts, final_num)
                master_list.append(int(final_num))

    #print(master_list)
    print(sum(master_list))
    final_answer = sum(master_list) - master_list[-1]
    #54722

    # Master list duplicated the answer for the last line for some reason
    final_answer = sum(master_list) - master_list[-1]

#____________________________

all_possible_nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
master_list = list()
counts = 0

with open('day1.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        if counts > 10:
            break
        else:
            counts += 1
            nums = []

            for word in all_possible_nums:
                if word in line:
                    nums.append(word)

            line_split = line.split(word)
            print('split:', line_split)

            if len(nums) < 2:
                try: final_num = str(nums[0]) + str(nums[0])
                except: pass
            else:
                final_num = str(nums[0]) + str(nums[-1])

            print('line:', counts, final_num)
            master_list.append((final_num))

#print(master_list)
print(master_list)
#54722

# Master list duplicated the answer for the last line for some reason
#final_answer = sum(master_list) - master_list[-1]


