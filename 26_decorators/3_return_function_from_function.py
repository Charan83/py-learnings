from random import choice

#   example 1


def make_laugh_func():
    def get_laugh():
        l = choice(('hahaha', 'lol', 'thehehe'))
        return l
    return get_laugh


laugh = make_laugh_func()
print(laugh())
print(laugh())

#    example 2 : Inner function can access outer function scope


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'LOL', 'THEHEHEHEHE'))
        return f"{laugh} {person}"

    return get_laugh


laugh_at = make_laugh_at_func('Guru')
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
