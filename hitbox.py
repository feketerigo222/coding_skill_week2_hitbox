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
            a = item.split(' ')
            enemy_cnt = int(a[0])
            i += 1
        elif i > 1:
            enemy[i-2] = item.split(' ')
            enemy[i-2] = [int(s) for s in enemy[i-2]]
            i += 1


def checkA(i):
    global hitcheck
    if enemy[i][0] <= my_data[0] <= (enemy[i][0] + enemy[i][2]):
        heightCheck(i)
        return hitcheck
    elif my_data[0] <= enemy[i][0] <= (my_data[0] + my_data[2]):
        heightCheck(i)
        return hitcheck


def checkB(i):
    global hitcheck
    if enemy[i][0] <= my_data[0] and (my_data[0] + my_data[2]) <= (enemy[i][0] + enemy[i][2]):
        heightCheck(i)
        return hitcheck
    elif enemy[i][0] >= my_data[0] and (my_data[0] + my_data[2]) >= (enemy[i][0] + enemy[i][2]):
        heightCheck(i)
        return hitcheck


def heightCheck(i):
    global hitcheck
    if enemy[i][1] <= my_data[1] <= (enemy[i][1] + enemy[i][3]):
        hitcheck = True
        return hitcheck
    elif my_data[1] <= enemy[i][1] <= (my_data[1] + my_data[3]):
        hitcheck = True
        return hitcheck
    elif enemy[i][1] <= my_data[1] and (my_data[1] + my_data[3]) <= (enemy[i][1] + enemy[i][3]):
        hitcheck = True
        return hitcheck
    elif my_data[1] <= enemy[i][1] and (enemy[i][1] + enemy[i][3]) <= (my_data[1] + my_data[3]):
        hitcheck = True
        return hitcheck


i = 0
while i < enemy_cnt:
    hitcheck = False
    if (checkA(i) == True) or (checkB(i) == True):
        print("敵機" + str(i+1) + "が当たり")
    i += 1
