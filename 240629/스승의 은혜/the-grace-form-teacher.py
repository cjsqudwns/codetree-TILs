def find_max_gift():
    def apply_coupon(index):
        new_arr = []
        for i in range(n):
            if i == index:
                new_arr.append(arr[i][0] // 2 + arr[i][1])
            else:
                new_arr.append(sum(arr[i]))
        return new_arr

    ans = 0
    for i in range(n):
        costs = apply_coupon(i)
        costs.sort()
        total_cost = 0
        cnt = 0
        for cost in costs:
            total_cost += cost
            cnt += 1
            if total_cost < b:
                ans = max(ans, cnt)
            else:
                continue
    return ans


n, b = map(int, input().split())
arr = []
for _ in range(n):
    p, s = map(int, input().split())
    arr.append([p, s])
print(find_max_gift())