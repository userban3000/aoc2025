INPUT = "input.in"
DEBUG = False

# sum of neighbors, but we know
# center is 1, so substract that
def neighbor_sum(m, i, j):
    sum = 0
    for ii in range(i-1, i+2):
        for ij in range(j-1, j+2):
            sum += m[ii][ij]
    return sum - 1

ans = 0
with open(INPUT, 'r') as f:
    # construct matrix
    dim = (len(f.readline()) + 2, 1 + sum(1 for _ in f) + 2)
    f.seek(0) # back to start of file
    m = [[0 for _ in range(dim[0])] for _ in range(dim[1])]
    for i, line in enumerate(f):
        for j, char in enumerate(line):
            m[i+1][j+1] = 1 if char == "@" else 0


removal = 0
while True:
    for i in range(1, dim[0] - 1):
        for j in range(1, dim[1] - 1):
            if m[i][j] == 1 and neighbor_sum(m, i, j) < 4:
                if DEBUG:
                    print(i, j, neighbor_sum(m, i, j))
                removal += 1
                ans += 1
                m[i][j] = 0
    if removal > 0:
        removal = 0
    else:
        break

print(ans)