n = int(input())
arr = [int(input()) for _ in range(n)]

unique_heights = sorted(set(arr))
index_map = {height: idx for idx, height in enumerate(unique_heights)}

index_arr = [[] for _ in range(len(unique_heights))]
for i, height in enumerate(arr):
    index_arr[index_map[height]].append(i + 1)

visited = [False] * (n + 2)
result = 0
answer = 0

for indices in reversed(index_arr):
    for cur_idx in indices:
        if not visited[cur_idx - 1] and not visited[cur_idx + 1]:
            result += 1
        elif visited[cur_idx - 1] and visited[cur_idx + 1]:
            result -= 1
        visited[cur_idx] = True

    answer = max(answer, result)

print(answer)