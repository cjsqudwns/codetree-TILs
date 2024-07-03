n = int(input())
str_list = [[i, list(input())] for i in range(n)]
ans = [[0 for _ in range(n)] for _ in range(2)]
# 오름차순
str_list_asc = []
for i in range(n):
    str_asc = sorted(str_list[i][1])
    str_list_asc.append((i, str_asc))
str_list_asc = sorted(str_list_asc, key=lambda x: x[1])
rank = 1
for idx, _ in str_list_asc:
    ans[0][idx] = rank
    rank += 1
# 내림차순
str_list_desc = []
for i in range(n):
    str_desc = sorted(str_list[i][1], reverse=True)
    str_list_desc.append((i, str_desc))
str_list_desc = sorted(str_list_desc, key=lambda x: x[1])
rank = 1
for idx, _ in str_list_desc:
    ans[1][idx] = rank
    rank += 1
for i in range(n):
    fast_order = ans[0][i]
    slow_order = ans[1][i]
    if fast_order < slow_order:
        print(f"{fast_order} {slow_order}")
    else:
        print(f"{slow_order} {fast_order}")

# print(str_list)
# print(sorted(str_list[3][1], key=lambda x: x, reverse=True))
# print(sorted(str_list, key=lambda x: x[1]))