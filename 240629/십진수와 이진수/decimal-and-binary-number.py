n = int(input())

t = 0
result = 0
while n > 0:
    result += (n % 10) * (2 ** t)
    n //= 10
    t += 1
result *= 17
ans = 0
b = 0
while result > 0:
    l = result % 2
    ans += l * (10 ** b)
    result //= 2
    b += 1
print(ans)