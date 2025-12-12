INPUT = "input.in"

def search(line, start, cutoff):
    elem = -1
    pos = -1
    for i in range(start, len(line) - cutoff + 1):
        joltage = int(line[i])
        if joltage > elem:
            elem = joltage
            pos = i
    return elem if cutoff <= 1 else elem * 10 ** (cutoff - 1) + search(line, pos + 1, cutoff - 1)

ans = 0
for line in open(INPUT).read().split('\n'):
    if line == "":
        continue
    lineres = search(line, 0, 12)
    ans += lineres
print(f"ans: {ans}")