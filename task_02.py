new_list = [13, 12, 2, 4, 1, 9, 5, 3, 11]
res_list = [new_list[num] for num in range(1, len(new_list)) if new_list[num] > new_list[num - 1]]
print(res_list)
