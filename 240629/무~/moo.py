def calculate_s(depth, before_str):
    result = before_str
    if len(result) >= n:
        print(result[n - 1])
        return
    else:
        temp = "moo" + "o" * depth
        result += temp + before_str
        calculate_s(depth + 1, result)


n = int(input())
calculate_s(1, "moo")