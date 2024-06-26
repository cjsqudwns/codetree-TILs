n, k = map(int, input().split())
arr = [0] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1] += 1
    if b < n:
        arr[b] -= 1

for i in range(1, n):
    arr[i] += arr[i - 1]

arr = arr[:n]
arr.sort()

print(arr[n // 2])