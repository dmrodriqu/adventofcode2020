
f = open('input.txt', 'r')

texts = f.read()
passports = texts.split('\n\n')
categories = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
invalid = 0
for check in passports:
    data = check.replace('\n', ' ')
    info = dict(item.split(':') for item in data.split())
    diff = categories - set(info.keys())
    if not(bool(diff)):
        invalid+=1

print(invalid)
f.close()
