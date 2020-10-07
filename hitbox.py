input_num = []
enemy = {}
while True:
    val = input("")
    if val:
        input_num.append(val)
    else:
        print(len(input_num))
        break

if input_num:
    print("入力した値は以下のとおりです")
    i = 0
    for item in input_num:
        print(item.split(' '))
        if i == 0:
            my_data = item
            i += 1
        elif i == 1:
            enemy_cnt = item
            i += 1
        elif i > 1:
            enemy[i-2] = item
            i += 1

print(my_data)
print(enemy_cnt)
print(enemy)
