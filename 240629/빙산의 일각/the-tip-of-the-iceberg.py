n = int(input())
dist_h_arr = []
h_arr = []
for _ in range(n):
    h = int(input())
    h_arr.append(h)
    if h not in dist_h_arr:
        dist_h_arr.append(h)
ans = 0
dist_h_arr.sort()
for i in dist_h_arr:
    cnt = 0
    isHigh = False
    for h in h_arr:
        if h > i:
            if not isHigh:
                cnt += 1
                isHigh = True
        else:
            isHigh = False
    ans = max(ans, cnt)
print(ans)