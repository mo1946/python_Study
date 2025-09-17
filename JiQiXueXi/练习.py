def my_sum(*args):
    return sum(args)

l = [i ** 2 for i in range(10)]
print(l)
print(my_sum(*l))