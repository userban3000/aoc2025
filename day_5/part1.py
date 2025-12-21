INPUT = "input.in"

with open(INPUT) as f:
    content = f.read()
    
ranges_text, numbers_text = content.split('\n\n', 1)

ranges = [tuple(map(int, line.split('-'))) for line in ranges_text.strip().split('\n')]
numbers = [int(line) for line in numbers_text.strip().split('\n')]

sum = 0
for num in numbers:
    for range in ranges:
        if num >= range[0] and num <= range[1]:
            sum += 1
            break

print(sum)