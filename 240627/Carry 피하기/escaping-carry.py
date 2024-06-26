def check_carry(n1, n2):
    while n1 > 0 and n2 > 0:
        c1 = n1 % 10
        c2 = n2 % 10
        if c1 + c2 >= 10:
            return True
        n1 //= 10
        n2 //= 10
    return False


def backtracking(cnt, depth, current_sum):
    global result
    result = max(cnt, result)
    if depth == n:
        memo[(cnt, depth, current_sum)] = result
        return

    for i in range(depth, n):
        if not check_carry(current_sum, num_arr[i]):
            backtracking(cnt + 1, i + 1, current_sum + num_arr[i])

    memo[(cnt, depth, current_sum)] = result


n = int(input())
num_arr = [int(input()) for _ in range(n)]

result = 0
memo = {}
backtracking(0, 0, 0)
print(result)