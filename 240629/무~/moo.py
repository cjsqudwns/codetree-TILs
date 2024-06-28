def calculate_s(before_m, before_mid_len):
    m_locate = before_m
    str_length = m_locate[-1] + 3
    if str_length >= n:
        if n - 1 in m_locate:
            print("m")
        else:
            print("o")
        return
    else:
        m_locate.append(str_length)
        for i in range(len(m_locate) - 1):
            m_locate.append(m_locate[i] + str_length + before_mid_len + 1)
        calculate_s(m_locate, before_mid_len + 1)


n = int(input())
calculate_s([0], 3)