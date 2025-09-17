# 案例一 求1-100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"1-100的和为：{sum}")
print("-" * 20)

# 案例二 求1-100中偶数的和
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2
print(f"1-100中的偶数和为：{sum}")