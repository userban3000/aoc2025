INPUT = "input.in"

res = 0

for entry in open(INPUT).read().split(","):
    start, end = (int(x) for x in entry.split("-"))
    for num in range(start, end + 1):
        num_str = str(num)
        length = len(num_str)
        for sublen in range(1, length//2+1):
            if length % sublen:
                continue
            sub = num_str[0:sublen]
            if all(num_str[i:i+sublen] == sub for i in range(0, length, sublen)):
                res += num
                break

print(res)
