"""
I thought the solution below will give me TLE but somehow it didn't. But still it looks ridiculous
"""
def solution():
    n, k = map(int, input().split())
    l, t, r = [], [], []
    for _ in range(n):
        tl, tt, tr = map(int, input().split())
        l.append(tl)
        t.append(tt)
        r.append(tr)
    a = [l[i] - (i + 1) * k for i in range(n)]
    s = [t[i] - (i + 1) * k for i in range(n)]
    b = [r[i] - (i + 1) * k for i in range(n)]
    for x in range(n):
        if a[x] > b[x]:
            print(-1)
            break
    def f(a, b, c):
        if a < b: return b
        if a > c: return c
        return a
    def slice(s, l, r):
        l = sorted(s[l:r + 1])
        return l[(len(l) - 1) // 2]
    cand = []
    flag = False
    for x in range(n):
        ax, bx = a[x], b[x]
        cal = f(s[x], ax, bx)
        table = (x, x, ax, bx, cal)
        cand.append(table)
        length = len(cand)
        while length >= 2 and cand[-1][4] < cand[-2][4]:
            l1, r1, a1, b1, c1 = cand[-1]
            l2, r2, a2, b2, c2 = cand[-2]
            left, right = l2, r1
            ax, bx = max(a1, a2), min(b1, b2)
            if ax > bx:
                flag = True
                print(-1)
                break
            cal2 = slice(s, left, right)
            cal = f(cal2, ax, bx)
            for _ in range(2): cand.pop()
            table = (left, right, ax, bx, cal)
            cand.append(table)
            length = len(cand)
        if flag: break
    q = [0]*n
    for left, right, ax, bx, cal in cand:
        for x in range(left, right + 1):
            q[x] = cal
    res = list()
    cost = 0
    for x in range(n): res.append(q[x] + (x + 1) * k)
    for x in range(n): cost += abs(res[x] - t[x])
    if not flag:
        print(cost)
        print(*res)
solution()

