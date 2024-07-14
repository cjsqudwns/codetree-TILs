n, q = map(int, input().split())
parents = [-1]
authority = [-1]
notification = [True for _ in range(n + 1)]

for _ in range(q):
    q_info = tuple(map(int, input().split()))
    # 사내 메신저 준비
    if q_info[0] == 100:
        for i in range(1, n + 1):
            parents.append(q_info[i])
        for i in range(n + 1, 2 * n + 1):
            authority.append(q_info[i])
    # 알림망 설정 ON / OFF
    elif q_info[0] == 200:
        notification[q_info[1]] = not notification[q_info[1]]
    # 권한 세기 변경
    elif q_info[0] == 300:
        authority[q_info[1]] = q_info[2]
    # 부모 채팅방 교환
    elif q_info[0] == 400:
        parents[q_info[1]], parents[q_info[2]] = parents[q_info[2]], parents[q_info[1]]
    # 알림을 받을 수 있는 채팅방 수 조회
    elif q_info[0] == 500:
        cnt = 0
        for i in range(1, n + 1):
            if q_info[1] != i:
                auth = authority[i]
                cur_node = i
                while True:
                    if cur_node == q_info[1]:
                        cnt += 1
                        break
                    if not notification[cur_node] or auth <= 0:
                        break
                    else:
                        cur_node = parents[cur_node]
                        auth -= 1
        print(cnt)