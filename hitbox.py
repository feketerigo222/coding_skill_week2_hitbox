input_num = []
enemy = {}
while True:
    val = input("")
    if val:
        input_num.append(val)
    else:
        break

if input_num:
    i = 0
    for item in input_num:
        if i == 0:
            my_data = item.split(' ')
            my_data = [int(s) for s in my_data]
            i += 1
        elif i == 1:
            enemy_cnt = item.split(' ')
            enemy_cnt = [int(s) for s in enemy_cnt]
            i += 1
        elif i > 1:
            enemy[i-2] = item.split(' ')
            enemy[i-2] = [int(s) for s in enemy[i-2]]
            i += 1

print(my_data)
print(enemy_cnt)
print(enemy)

a = my_data[0] + my_data[1]
print(a)
