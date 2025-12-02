INPUT = "input.in"

res = 0

for entry in open(INPUT).read().split(","):
    start, end = (int(x) for x in entry.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        length = len(s)
        if length % 2:
            continue
        if s[length//2:] == s[:length//2]:
            res += i

print(res)
