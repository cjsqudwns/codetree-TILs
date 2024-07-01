def check(str, idx):
    if prev_cnt[idx - 1] < 0:
        return False
    cnt = prev_cnt[idx - 1]
    for i in range(idx, len(str)):
        temp = str[i]
        if temp == "(":
            cnt += 1
        elif temp == ")":
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return cnt == 0


a = list(input())
prev_cnt = [0 for _ in range(len(a) + 1)]
ans = 0
for i in range(len(a)):
    if a[i] == "(":
        prev_cnt[i] = prev_cnt[i - 1] + 1
        a[i] = ")"
        if check(a, i):
            ans += 1
        a[i] = "("
    elif a[i] == ")":
        prev_cnt[i] = prev_cnt[i - 1] - 1
        a[i] = "("
        if check(a, i):
            ans += 1
        a[i] = ")"
print(ans)