import math
import sys


def cal(num, num_len, mul, ch_idx, ch_num):
    result = 0
    e = 0
    for _ in range(num_len):
        if e != ch_idx:
            result += math.pow(mul, e) * (num % 10)
        else:
            result += math.pow(mul, e) * ch_num
        num //= 10
        e += 1
    return int(result)


# 입력 받기
a = input()
b = input()
l = []
for i in range(len(a)):  # 가장 낮은 자리 수부터
    if a[len(a) - i - 1] == '0':
        l.append(cal(int(a), len(a), 2, i, 1))
    else:
        l.append(cal(int(a), len(a), 2, i, 0))
for i in range(len(b)):
    for j in range(3):
        if str(j) != b[len(b) - i - 1]:
            ans = cal(int(b), len(b), 3, i, j)
            if ans in l:
                print(ans)
                sys.exit()