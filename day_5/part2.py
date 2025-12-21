INPUT = "input.in"

with open(INPUT) as f:
    content = f.read()

def in_range(n, range):
    return n >= range[0] and n <= range[1]

def range_sum(ranges: list, r: tuple):
    sum = r[1] - r[0] + 1
    new_ranges = ranges.copy()
    new_range = list(r)
    for range in ranges:
        if in_range(range[0], r) and in_range(range[1], r):
            sum -= range[1] - range[0] + 1
            new_ranges.remove(range)
            continue
        if in_range(range[1], r):
            sum -= range[1] - r[0] + 1
            new_range[0] = max(range[1]+1, new_range[0])
            continue
        if in_range(range[0], r):
            sum -= r[1] - range[0] + 1
            new_range[1] = min(range[0]-1, new_range[1])
            continue
        if range[0] < r[0] and range[1] > r[1]:
            return 0, ranges
    if new_range[1] >= new_range[0]:
        new_ranges.append(tuple(new_range))
    return max(sum, 0), new_ranges

ranges_text, _ = content.split('\n\n', 1)
ranges = [tuple(map(int, line.split('-'))) for line in ranges_text.strip().split('\n')]
committed_ranges = list()

sum = 0
for r in ranges:
    res, committed_ranges = range_sum(committed_ranges, r)
    sum += res

print(sum)