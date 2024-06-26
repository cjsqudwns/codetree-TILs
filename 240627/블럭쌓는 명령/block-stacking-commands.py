n, k = map(int, input().split())
arr = [0 for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        arr[j - 1] += 1
arr.sort()
print(arr[int(n / 2)])