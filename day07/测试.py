
n = int(input())
is_p = [True for i in range(n + 1)]
p = []
is_p[0] = False
is_p[1] = False

for i in range(2, n + 1):
    if is_p[i]:
        p.append(i)
    for j in range(len(p)):
        if i * p[j] > n:
            break
        is_p[p[j] * i] = False
        if i % p[j] == 0:
            break
print(p)
























