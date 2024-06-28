n = int(input())
k = []
dist_k = []
for _ in range(n):
    i = int(input())
    k.append(i)
    if i not in dist_k:
        dist_k.append(i)
ans = 0
for i in dist_k:
    temp = k.copy()
    while i in temp:
        temp.remove(i)
    cnt = 0
    prev_v = 0
    for j in range(len(temp)):
        if prev_v == temp[j]:
            cnt += 1
        else:
            prev_v = temp[j]
            cnt = 1
        ans = max(ans, cnt)
print(ans)