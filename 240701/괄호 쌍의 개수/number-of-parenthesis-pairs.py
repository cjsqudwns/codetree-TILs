from collections import deque


def check(str):
    d = deque()
    for i in range(len(str)):
        temp = str[i]
        if temp == "(":
            d.append(temp)
        elif temp == ")":
            if len(d) == 0:
                return False
            else:
                d.pop()
    return len(d) == 0


a = list(input())
ans = 0
for i in range(len(a)):
    if a[i] == "(":
        a[i] = ")"
        if check(a):
            ans += 1
        a[i] = "("
    elif a[i] == ")":
        a[i] = "("
        if check(a):
            ans += 1
        a[i] = ")"
print(ans)