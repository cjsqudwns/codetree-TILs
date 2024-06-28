def dfs(ar, ac, br, bc, move_cnt, flag):
    if flag:  # A턴
        for i in range(4):
            nr = ar + dr[i]
            nc = ac + dc[i]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4 or m[nr][nc]:
                continue
            m[nr][nc] = True
            dfs(nr, nc, br, bc, move_cnt - 1, not flag)
            m[nr][nc] = False
    else:  # B턴
        for i in range(4):
            nr = br + dr[i]
            nc = bc + dc[i]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if move_cnt == 0:
                if ar == nr and ac == nc:
                    global ans
                    ans += 1
                    return
                else:
                    continue
            if m[nr][nc]:
                continue
            m[nr][nc] = True
            dfs(ar, ac, nr, nc, move_cnt - 1, not flag)
            m[nr][nc] = False


k = int(input())
m = [[False for _ in range(5)] for _ in range(5)]
for i in range(k):
    r, c = map(int, input().split())
    m[r - 1][c - 1] = True
ans = 0
m[0][0] = True
m[4][4] = True
# visited = False
# 아래, 왼, 위, 오 / r, c
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dfs(0, 0, 4, 4, 23 - k, True)
print(ans)