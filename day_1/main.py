FILE = "input.in"

i = 50
pw = 0

with open(FILE, 'r') as f:
    for op in f:
        op = op.strip()
        sign = op[0]
        num = int(op[1:])

        old_i = i
        i += num if sign == "R" else -num
        pw += abs(i // 100)
        i %= 100

        if sign == "L":
            pw += (i == 0) - (old_i == 0)

print(pw)
