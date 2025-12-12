INPUT = "input.in"

ans = 0
for line in open(INPUT).read().split('\n'):
    # broken input fix lol
    if line == "":
        continue

    # logic
    first_elem = -1
    first_pos = -1
    for i in range(len(line) - 1):
        joltage = int(line[i])
        if joltage > first_elem:
            first_elem = joltage
            first_pos = i
    second_elem = -1
    for i in range(first_pos + 1, len(line)):
        joltage = int(line[i])
        if joltage > second_elem:
            second_elem = joltage
    ans += first_elem * 10 + second_elem
    print(line)
    print(first_elem * 10 + second_elem)

print(ans)