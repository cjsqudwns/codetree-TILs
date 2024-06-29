n = int(input())
h_arr = [int(input()) for _ in range(n)]
ans = 0
for i in range(1, max(h_arr)):
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