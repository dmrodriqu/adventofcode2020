


def part1(f):
    right = 0
    trees = 0
    for line in f:
        line = line[:-1]
        maxindex = len(line)-1
        if right > maxindex:
            right = right % maxindex  - 1
        if line[right] == '#':
            trees += 1
        right += 3

    print(trees)

def part2(f, r, d):
    right = 0
    trees = 0
    for line in f:
        if d == 2:
            f.readline()
        line = line[:-1]
        maxindex = len(line)-1
        if right > maxindex:
            right = right % maxindex  - 1
        if line[right] == '#':
            trees += 1
        right += r
    return trees



f = open('input.txt', 'r')
print('part 1:')
part1(f)
print()
f.seek(0)
t = 1
for i in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
    r = i[0]
    d = i[1]
    t*=part2(f, r, d)
    f.seek(0)
print('part 2:')
print (t)
