"""
Think it also can be solved by greedy algorithm, but I just used some segment trees to make the lo,gic itself simple.
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
negative = -(10**20+1)
bin_size = 1
while bin_size < n: bin_size <<= 1
li = [negative] * (2*bin_size)
for x, v in enumerate(a): li[bin_size + x] = v
for x in range(bin_size - 1, 0, -1):
    y = x*2
    if li[y] >= li[y+1]: li[x] = li[y]
    else: li[x] = li[y+1]
def get_max_val(left, right):
    global bin_size
    if left > right: return negative
    left += bin_size
    right += bin_size
    ret = negative
    while left <= right:
        l, r = left&1, right&1
        if l:
            ret = li[left] if li[left] > ret else ret
            left += 1
        if not r:
            ret = li[right] if li[right] > ret else ret
            right -= 1
        left >>= 1
        right >>= 1
    return ret
res = -(10**20+1)
for x in range(n):
    sub = x
    max_right = negative
    max_left = negative
    cases = [k-sub, k-sub+1]
    if cases[0] >= 0:
        val = max(x+1, n-cases[0]-1)
        if val <= (n-1): max_right = get_max_val(val, n-1)
    if cases[1] >= 0:
        l_val = max(0, n-cases[1]-1)
        r_val = x-1
        if l_val <= r_val: max_left = get_max_val(l_val, r_val)
    M = max(max_right, max_left)
    if M > negative: res = max(res, M-a[x])
print(res)




