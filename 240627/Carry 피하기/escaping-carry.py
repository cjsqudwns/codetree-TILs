def check_carry(n1, n2):
    while n1 > 0 or n2 > 0:
        # print("Before\nn1 : %d\nn2 : %d" % (n1, n2))
        c1 = n1 % 10
        c2 = n2 % 10
        if c1 + c2 >= 10:
            return True
        n1 /= 10
        n2 /= 10
        # print("After\nn1 : %d\nn2 : %d" % (n1, n2))
    return False


def backtracking(cnt, depth, sum):
    global result
    result = max(cnt, result)
    if depth == n:
        return
    for i in range(depth, n):
        if not check_carry(sum, num_arr[i]):
            backtracking(cnt + 1, i + 1, sum + num_arr[i])


n = int(input())
num_arr = []
for _ in range(n):
    num_arr.append(int(input()))
result = 0
for i in range(n):
    backtracking(1, 1, num_arr[i])
print(result)