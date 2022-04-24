#   max
#       - retuns the largest item in an iterable(list, tuple, string....)
#       - maxx from the two or more args

# example 1
print(max(1, 2, 3, 4))

print(max([1, 2, 35, 775, 234]))

# example 2
names = ['Gurucharan', 'Shohil', "Tanuja", "Bhoomika", "Dileep"]
print(min(names))
print(max(names))
print(max(len(name) for name in names))  # 8, but we want the name
name_max_length = max(names, key=lambda n: len(n))
print(f"name_max_length : {name_max_length}")


# example 3
songs = [
    {"title": "happy birthday", "playcount": 10},
    {"title": "Survive", "playcount": 15},
    {"title": "YMCA", "playcount": 6},
    {"title": "Jana Gana Mana", "playcount": 110},
    {"title": "Swedish song", "playcount": 120},
    {"title": "Manam", "playcount": 8},
]
max_song = max(songs, key=lambda song: song["playcount"])
print(f"max_song : {max_song}")
sorted_song_playcount = sorted(
    songs, key=lambda song: song["playcount"], reverse=True)
print(f"sorted_song_playcount : {sorted_song_playcount}")

# example 4


def extremes(iterable):
    return (min(iterable), max(iterable))


print(f"extremes([1,2,3,4,5,6,7]) : {extremes([1,2,3,4,5,6,7])}")
print(f"extremes('gurucharan') : {extremes('gurucharan')}")


#   reversed
#       - original iterator is not changed
#       - a new reversed object is created
str1 = "reversed"
print(list(reversed(str1)))
print(str1)
print(reversed(str1))
