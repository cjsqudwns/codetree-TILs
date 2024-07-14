n = int(input())
move_arr = [0]
visited = [False for _ in range(n + 1)]
for _ in range(n):
    t = int(input())
    move_arr.append(t)
ans = 0
for i in range(1, n + 1):
    visited_copy = visited.copy()
    next_idx = i
    while True:
        if visited_copy[next_idx]:
            break
        else:
            visited_copy[next_idx] = True
            if move_arr[next_idx] != 0:
                next_idx = move_arr[next_idx]
            else:
                ans += 1
print(ans)