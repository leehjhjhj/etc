n = int(input())
result = []
for _ in range(n):
    arr = [input() for _ in range(8)]
    check_x = [0] * 8
    check_y = [0] * 8
    cnt = 0
    rst = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                cnt += 1
                if check_x[j] == 1 or check_y[i] == 1 or cnt > 8:
                    result.append(0)
                    rst = 1
                    break
                else:
                    check_x[j] = 1
                    check_y[i] = 1
        if rst == 1:
            break

    if rst != 1 and cnt < 8:
        result.append(0)
    elif rst != 1 and cnt == 8:
        result.append(1)

result_cnt = 0
for target in result:
    result_cnt += 1
    if target == 0:
        print(f"#{result_cnt} no")
    else:
        print(f"#{result_cnt} yes")