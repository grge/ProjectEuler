def palindrome_products(a,b):
    for i in range(a,b):
        for j in range(a,b):
            p = str(i * j)
            if p == p[::-1]:
                yield i*j

print max([i for i in palindrome_products(100,999)])


