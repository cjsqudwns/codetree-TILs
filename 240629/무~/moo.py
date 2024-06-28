def calculate_s(before_str):
    result = before_str
    if len(result) >= n:
        print(result[n - 1])
        return
    else:
        result += before_str + "o" + before_str
        calculate_s(result)


n = int(input())
calculate_s("moo")