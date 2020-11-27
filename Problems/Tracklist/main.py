def tracklist(**artists):
    for artist, tracks in artists.items():
        print(artist)
        for album, track in tracks.items():
            print(f'ALBUM: {album} TRACK: {track}')
