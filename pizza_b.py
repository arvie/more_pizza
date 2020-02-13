import random

m, n = list(map(int, "100 10".split()))
s = """
4 14 15 18 29 32 36 82 95 95
"""
a = list(map(int, s.split()))

def slices(r):
    return sum([a[i] for i in range(n) if r & 2**i])

r = 0
rs = set()

while True:
    if r < m:
        rnd = random.randint(0, n - 1)
        while rnd in rs:
            rnd = random.randint(0, n - 1)
        r = r + a[rnd]
        rs.add(rnd)
    elif r > m:
        rnd = random.randint(0, n)
        while rnd not in rs:
            rnd = random.randint(0, n - 1)
        r = r - a[rnd]
        rs.remove(rnd)
    if abs(r - m) < 1:
        res = [a[i] for i in rs]
        print(len(res))
        print(' '.join(map(str, rs)))
        break

