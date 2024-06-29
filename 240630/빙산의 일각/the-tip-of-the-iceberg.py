n = int(input())
h_arr = [int(input()) for _ in range(n)]

# 고유한 높이값 추출
unique_heights = sorted(set(h_arr))

max_chunks = 0

# 각 고유 높이에 대해 최대 덩어리 수 계산
for height in unique_heights:
    chunks = 0
    in_chunk = False
    for h in h_arr:
        if h > height:
            if not in_chunk:
                chunks += 1
                in_chunk = True
        else:
            in_chunk = False
    max_chunks = max(max_chunks, chunks)

print(max_chunks)