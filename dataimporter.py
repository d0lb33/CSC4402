import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import false
import itertools


class Song:
    id_iter = itertools.count()
    id: int
    genre: String
    album_id: int
    name: String
    seconds: int


class Artist:
    id_iter = itertools.count()
    id: int
    name: String


class Album:
    id_iter = itertools.count()
    id: int
    name: String
    release_date: String
    artist_id: int


artists: list[Artist] = []
songs: list[Song] = []
albums: list[Album] = []


def get_sec(time_str):
    """Get Seconds from time string MM:SS"""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

# Open CSV file
with open('songs.csv', encoding="utf8") as csvfile:

    # Read CSV file
    song_list = csv.reader(csvfile, delimiter=',', quotechar='|')

    i = 0

    # Loop over CSV.
    for row in song_list:
        if i > 0:  
            # Header Layout:
            #     0       1        2         3         4             5
            # song_name, time, album_name, genre, release_date, album_artist

            # Gather details of each row
            song_name = row[0]
            time = row[1]
            seconds = get_sec(time)
            album_name = row[2]
            genre = row[3]
            release_date = row[4]
            artist_name = row[5]

            # Create artists
            # Check if artist exists:
            exists = false
            artist = Artist()

            for a in artists:
                if a.name == artist_name:
                    artist = a
                    exists = True
            if exists == false:
                artist.name = artist_name
                # Only iterate id if we are creating a new artist.
                artist.id = next(artist.id_iter)
                artists.append(artist)


            # Create albums
            # Check if album exists
            exists = false
            album = Album()

            for a in albums:
                if a.name == album_name:
                    album = a
                    exists = True

            if exists == false:
                album.name = album_name
                # Only iterate id if we are creating a new album.
                album.id = next(album.id_iter)
                # Assign this album to an artist
                album.artist_id = artist.id
                album.release_date = release_date
                albums.append(album)

            # Create songs
            # Check if album exists
            exists = false
            song = Song()

            for s in songs:
                if s.name == song_name:
                    song = s
                    exists = True

            if exists == false:
                song.name = song_name
                # Only iterate id if we are creating a new song.
                song.id = next(song.id_iter)
                # Assign this song to an album
                song.album_id = album.id
                # General song data
                song.seconds = seconds
                song.genre = genre
                songs.append(song)
        i += 1

    engine = create_engine('sqlite:///music_library.db')

    with engine.connect() as con:

        # Clear tables
        con.execute("DELETE FROM artists")
        con.execute("DELETE FROM songs")
        con.execute("DELETE FROM albums")

        # Insert artists
        for artist in artists:
            con.execute(
                f'INSERT INTO artists (id, name) VALUES ({artist.id}, "{artist.name}")')

        # Insert albums
        for album in albums:
            con.execute(
                f'INSERT INTO albums (id, name, release_date, artist_id) VALUES ({album.id}, "{album.name}", "{album.release_date}","{album.artist_id}")')
        
        # Insert songs
        for song in songs:
            con.execute(
                f'INSERT INTO songs (id, name, album_id, genre, seconds) VALUES ({song.id}, "{song.name}", {song.album_id},"{song.genre}",{song.seconds})')
