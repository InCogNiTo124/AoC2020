passports = []
while True:
    try:
        passport = dict()
        while True:
            line = input().strip()
            if line == '':
                passports.append(passport.copy())
                passport = dict()
            else:
                for token in line.split(' '):
                    field, value = token.split(':')
                    passport.update({field: value})
    except Exception as ex:
        break

def height(h):
    if 'in' in h:
        return 59 <= int(h[:-2]) <= 76
    elif 'cm' in h:
        return 150 <= int(h[:-2]) <= 193
    else:
        return False


def hcl(h):
    if len(h) != 7 or h[0] != '#':
        return False
    for char in h:
        if char not in "#0123456789ABCDEFabcdef":
            return False
    return True

def pid(x):
    if len(x) != 9:
        return False
    for char in x:
        if char not in "0123456789":
            return False
    return True

def validate(x): 
    return (1920 <= int(x['byr']) <= 2002 and
            2010 <= int(x['iyr']) <= 2020 and
            2020 <= int(x['eyr']) <= 2030 and
            height(x['hgt']) and 
            hcl(x['hcl']) and
            x['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl','oth'] and
            pid(x['pid']))
            

FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
print(sum(1 for passport in passports if FIELDS <= passport.keys() and validate(passport)))
