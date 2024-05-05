n = int(input())
n_arr = [0]
for i in range(n):
    n_arr.append(int(input()))
m = int(input())
m_arr = []
for i in range(m):
    m_arr.append(int(input()))
m_arr.sort()
ans = []
for i in range(1, n - m + 2):
    temp_arr = n_arr[i:i + m]
    temp_arr.sort()
    # 순서만 바꾼 것 + 주어준 수열 그대로
    if m_arr == temp_arr:
        ans.append(i)
    # 동일한 숫자를 더하거나 빼고 순서를 바꿔 나오는 수열 check
    dif_arr = list(map(lambda x, y: x - y, temp_arr, m_arr))
    check = True
    v = dif_arr[0]
    for j in range(1, m):
        if dif_arr[j] != v:
            check = False
    if check:
        ans.append(i)
print(len(ans))
for v in ans:
    print(v)