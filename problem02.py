def fibs_up_to(n):
    (a, b) = (1, 2)
    while a < n:
        yield a
        (a, b) = (b, a + b)
print sum([i for i in fibs_up_to(4e6) if not i % 2])

