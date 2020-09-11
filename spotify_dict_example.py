playlist = {
    'title': 'dog days',
    'author': 'brandon g',
    'songs': [
        {'title': 'song1', 'artist': ['borkman'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['borkman', 'djbark'], 'duration': 5.5},
        {'title': 'borkbork', 'artist': ['borky'], 'duration': 5},
    ]
}

# how long is this playlist:
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)