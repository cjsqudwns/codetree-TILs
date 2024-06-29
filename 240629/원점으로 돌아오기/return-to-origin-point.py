def dps(x, y, rest_p, prev_dir):
    if len(rest_p) == 0:
        check = False
        if x == 0:
            if y < 0 and prev_dir != 0:  # 상
                check = True
            elif y > 0 and prev_dir != 2:  # 하
                check = True
        elif y == 0:
            if x < 0 and prev_dir != 1:  # 우
                check = True
            elif x > 0 and prev_dir != 3:  # 좌
                check = True
        if check:
            global ans
            ans += 1
        return
    for p in rest_p:
        dir = -1
        if x == p[0]:
            if y < p[1] and prev_dir != 0:  # 상
                dir = 0
            elif y > p[1] and prev_dir != 2:  # 하
                dir = 2
            else:
                continue
        elif y == p[1]:
            if x < p[0] and prev_dir != 1:  # 우
                dir = 1
            elif x > p[0] and prev_dir != 3:  # 좌
                dir = 3
            else:
                continue
        else:
            continue
        next_p = rest_p.copy()
        next_p.remove(p)
        dps(p[0], p[1], next_p, dir)


n = int(input())
p_arr = []
for i in range(n):
    p_arr.append(tuple(map(int, input().split())))
ans = 0
dps(0, 0, p_arr.copy(), -1)
print(ans)