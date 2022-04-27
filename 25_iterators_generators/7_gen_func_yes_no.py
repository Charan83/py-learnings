def yes_or_no():
    is_yes = True
    while True:
        if is_yes:
            yield 'yes'
        else:
            yield 'no'
        is_yes = not is_yes


yes_no_gen = yes_or_no()
print(next(yes_no_gen))
print(next(yes_no_gen))
print(next(yes_no_gen))
print(next(yes_no_gen))
print(next(yes_no_gen))
