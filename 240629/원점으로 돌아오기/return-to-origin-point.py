def dps(x, y, cnt, rest_p):
    if len(rest_p) == 0:
        if x == 0 or y == 0:
            global ans
            ans += 1
            return
    for p in rest_p:
        if p[0] == x or p[1] == y:
            next_p = rest_p.copy()
            next_p.remove(p)
            dps(p[0], p[1], cnt - 1, next_p)


n = int(input())
p_arr = []
for i in range(n):
    p_arr.append(tuple(map(int, input().split())))
ans = 0
dps(0, 0, n, p_arr.copy())
print(ans)