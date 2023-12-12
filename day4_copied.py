file = open('day4.txt', 'r')
res = 0

count = 0
for row in file.readlines():
    count += 1
    if count > 10:
        break
    else:
        row = row.rstrip("\n")
        card_id, card_nums = row.split(": ")[0], row.split(": ")[1]
        print(card_id, card_nums)
        win_nums, nums = card_nums.split(" | ")[0], card_nums.split(" | ")[1]
        print(win_nums, card_nums)
        win_lst = [int(i) for i in win_nums.split(" ") if i.isnumeric()]
        print(win_lst)
        player_lst = [int(i) for i in nums.split(" ") if i.isnumeric()]
        print(player_lst)
        row_total = 0
        for num in player_lst:
            if num in win_lst:
                if row_total == 0:
                    row_total = 1
                else:
                    row_total *= 2
        res += row_total
print(res)

# Correct Total: 23941
