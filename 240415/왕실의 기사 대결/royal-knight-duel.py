def move_knight(knight_num, dir, moved_knights):
    # 체크할 타일 확인
    tiles = check_tiles(dir, knight_info[knight_num - 1])
    contact_knights = []
    if len(tiles) > 0 :
        # 체크된 타일 중에 벽이 포함 되어 있는지 체크
        for tile in tiles:
            if map_info[tile[0]-1][tile[1]-1] == 2:
                contact_knights.append(-1)
                return contact_knights
        for i in range(N): # 진행 방향에 벽은 없고 다른 기사가 있는지 check
            if (knight_info[i][4] != 0 and i+1 not in moved_knights):
                if check_knight_exist(knight_info[i], tiles): # 타일들 위치에 기사가 있을 경우 true
                    contact_knights.append(i+1)
        return contact_knights
    else:
        contact_knights.append(-1)
        return contact_knights
def check_tiles(dir, moving_knight):
    tiles = []
    if dir == 0: # 위
        for i in range(moving_knight[3]): # 가로
            tile = [moving_knight[0]-1, moving_knight[1]+i]
            if(index_check(tile)):
                tiles.append(tile)
    elif dir == 1: # 오른쪽
        for i in range(moving_knight[2]): # 세로
            tile = [moving_knight[0]+i, moving_knight[1]+moving_knight[3]]
            if(index_check(tile)):
                tiles.append(tile)
    elif dir == 2: # 아래
        for i in range(moving_knight[3]):
            tile = [moving_knight[0]+moving_knight[2], moving_knight[1]+i]
            if(index_check(tile)):
                tiles.append(tile)
    elif dir == 3: # 왼쪽
        for i in range(moving_knight[2]):
            tile = [moving_knight[0]+i, moving_knight[1]-1]
            if(index_check(tile)):
                tiles.append(tile)
    return tiles
def index_check(tile): # 1 ~ L
    if tile[0] < 1 or tile[0] > L or tile[1] < 1 or tile[1] > L:
        return False
    else:
        return True
def check_knight_exist(knight, tiles):
    for i in range(knight[0], knight[0] + knight[2]):
        for j in range(knight[1], knight[1] + knight[3]):
            for tile in tiles:
                if tile[0] == i and tile[1] == j:
                    return True
    return False
def check_trap(knight_info, knight_num, moved_knights):
    for i in range(len(knight_info)):
        if (i+1 != knight_num) and (i+1 in moved_knights):
            for j in range(knight_info[i][0], knight_info[i][0] + knight_info[i][2]): # 세로
                for k in range(knight_info[i][1], knight_info[i][1] + knight_info[i][3]): # 가로
                    if map_info[j-1][k-1] == 1:
                        if(knight_info[i][4] > 0):
                            knight_info[i][4] -= 1
                        

L, N, Q = map(int, input().split())
map_info = [[] for _ in range(L)] # 체스판
for i in range(L):
    map_info[i] = list(map(int, input().split()))
d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위 / 오른쪽 / 아래 / 왼쪽
knight_info= [] # 처음 위치 y,x 0,1 / 세로 길이 2 / 가로 길이 3 / 체력 4
knight_hp = []
for i in range(N):
    knight_info.append(list(map(int, input().split())))
    knight_hp.append(knight_info[i][4])
missions = [] # i번 기사 d
for i in range(Q):
    missions.append(list(map(int, input().split())))


for mission in missions:
    knight_num = mission[0]
    if(knight_info[knight_num - 1][4] <= 0): # 죽은 애들에 대한 명령을 스킵
        break
    dir = mission[1]
    next_knights = [mission[0]]
    moved_knights = []
    while(True):
        results = []
        if len(next_knights) != 0:
            temp = next_knights[0]
            if temp in moved_knights:
                next_knights.remove(temp)
                continue
            moved_knights.append(temp)
            results = move_knight(temp, dir, moved_knights)
            next_knights.remove(temp)
        if -1 in results: # 변경 사항 저장 x
            break
        elif (len(results) == 0 and len(next_knights) == 0): # 변경 사항 저장 o
            for i in moved_knights:
                knight_info[i-1][0] += d[dir][0]
                knight_info[i-1][1] += d[dir][1]
            # + trap이 있는지 체크
            check_trap(knight_info, mission[0], moved_knights)
            break
        else:
            for result in results:
                if result not in moved_knights:
                    next_knights.append(result)
total_damage = 0
for i in range(N):
    if knight_info[i][4] != 0:
        total_damage += knight_hp[i] - knight_info[i][4]
print(total_damage)