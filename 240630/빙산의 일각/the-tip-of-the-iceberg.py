n = int(input())
h_arr = [int(input()) for _ in range(n)]

# 고유한 높이값 추출
unique_heights = sorted(set(h_arr))

ans = 0

# 각 고유 높이에 대해 최대 연속 건물 수 계산
for height in unique_heights:
    cnt = 0
    max_cnt = 0
    for h in h_arr:
        if h > height:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    ans = max(ans, max_cnt)

print(ans)