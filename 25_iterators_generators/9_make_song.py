'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, beverage='soda'):
    current_count = count
    msg = ''
    is_song_over = False
    while not is_song_over:
        if current_count > 1:
            msg = f"{current_count} bottles of {beverage} on the wall"
            current_count -= 1
        elif current_count == 1:
            msg = f"Only 1 bottles of {beverage} left"
            current_count -= 1
        else:
            is_song_over = True
            msg = f"No more {beverage}"
        yield msg


coke_song = make_song(15, 'nimma soda')
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))
print(next(coke_song))


# Other SOllution
def make_song_other(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
