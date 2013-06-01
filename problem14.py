def simple_collatz(limit):
    (s, l) = (0, 0)
    cache = [0] * int(limit)
    cache[1] = 1
    for i in range(2, int(limit)):
        seq_l = 1
        seq = i
        while (seq != 1 and seq >= i):
            if seq % 2:
                seq = seq*3 + 1
            else:
                seq /= 2
            seq_l += 1
        cache[i] = seq_l + cache[seq]
        if cache[i] > l:
            (s, l) = (i, cache[i])
    return (s, l)

print simple_collatz(1e06)
