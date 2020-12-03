from collections import Counter

def part1(f):
    valid = 0
    for line in f:
        parse =line.replace(':', '').split()
        rng = parse[0].split('-')
        char = parse[1]
        password = parse[2]
        interval = [int(x) for x in rng]
        count = dict(Counter(password))
        try:
            if interval[0] <= count[char] <= interval[1]:
                valid += 1
        except:
            pass
    print(valid)


def part2(f):
    valid = 0
    for line in f:
        parse =line.replace(':', '').split()
        rng = parse[0].split('-')
        char = parse[1]
        password = parse[2]
        ixl = int(rng[0]) - 1     
        ixr = int(rng[1]) - 1
        if (password[ixl] == char) ^ (password[ixr] == char):
            valid +=1
    print(valid)

f = open('input.txt')
part1(f)
f.seek(0)
part2(f)
f.close()
