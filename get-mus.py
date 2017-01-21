#!/usr/bin/python

from __future__ import unicode_literals

def main():
    import youtube_dl
    import sys
    options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,        # only download single song, not playlist
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([sys.argv[1]])


if __name__ == '__main__':
    main()
