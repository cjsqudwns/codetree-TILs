def find_nth_character(n):
    # 각 단계의 moo 문자열의 길이를 저장하는 리스트
    length = [3]  # 초기 "moo"의 길이
    while length[-1] < n:
        # 새로운 moo 문자열의 길이 = 2 * 이전 단계 길이 + 현재 단계 중간 부분 길이
        length.append(2 * length[-1] + len(length) + 3)
    
    def get_char(n, k):
        if k == 0:
            # 가장 기본 단계에서 직접 결과 반환
            return "moo"[n - 1]
        prev_length = length[k - 1]
        middle_length = k + 3
        if n <= prev_length:
            # n이 왼쪽 S(k-1)에 속하는 경우
            return get_char(n, k - 1)
        elif n <= prev_length + middle_length:
            # n이 중간 부분에 속하는 경우
            if n - prev_length == 1:
                return "m"
            else:
                return "o"
        else:
            # n이 오른쪽 S(k-1)에 속하는 경우
            return get_char(n - prev_length - middle_length, k - 1)
    
    return get_char(n, len(length) - 1)

n = int(input())
print(find_nth_character(n))