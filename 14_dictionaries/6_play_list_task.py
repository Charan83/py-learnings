playlist = {
    'title': 'motivational songs',
    'author': 'Guru',
    'songs': [
        {'title': 'song1', 'artist': 'artist1', 'duration': 2.9},
        {'title': 'song2', 'artist': 'artist2', 'duration': 3.9},
        {'title': 'song3', 'artist': 'artist3', 'duration': 4.9},
        {'title': 'song4', 'artist': 'artist4', 'duration': 5.9}
    ]
}
# total duration of the playlist
total_duration = 0
songslist = playlist['songs']
for song in songslist:
    total_duration += song.get('duration')
print(f"total_duration : {total_duration}")


""" 
playlist_passing = {
    'title': 'motivational songs',
    'author': 'Guru',
    'songs': [
        {'title': 'song1', 'artist': 'artist1', 'duration': 2.9},
        {'title': 'song2', 'artist': 'artist2', 'duration': 3.9},
        {'title': 'song3', 'artist': 'artist3', 'duration': 4.9},
        {'title': 'song4', 'artist': 'artist4', 'duration': 5.9}
    ]
}
# checking copy : shallow
combinedlist = playlist.update(playlist_passing)
print(combinedlist) 

"""
