def week():
    week_days = ('Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in week_days:
        yield day
    """ inital_idx = 0
    while inital_idx < len(week_days):
        yield week_days[inital_idx]
        inital_idx += 1 """


days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
