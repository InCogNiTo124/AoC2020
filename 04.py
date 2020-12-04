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
FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
print(sum(1 for passport in passports if FIELDS <= passport.keys()))
