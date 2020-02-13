import random

m, n = list(map(int, "4500 50".split()))
s = """
7 12 12 13 14 28 29 29 30 32 32 34 41 45 46 56 61 61 62 63 65 68 76 77 77 92 93 94 97 103 113 114 114 120 135 145 145 149 156 157 160 169 172 179 184 185 189 194 195 195
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
