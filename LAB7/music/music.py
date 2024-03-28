#Create music player with keyboard controller. You have to be able to press keyboard: play, stop,
# next and previous as some keys. Player has to react to the given command appropriately.
import pygame as pg
import time

pg.init()
heydaddy=pg.mixer.music.load("hey daddy.mp3")
intersteller=pg.mixer.music.queue('intersteller.mp3')
dooropen=pg.mixer.music.queue("dooropen.mp3")
clock = pg.time.Clock()
pg.mixer.music.play(-1) 
screen=pg.display.set_mode((1200,800))

songlist=["BillieJean.mp3", "intersteller.mp3","dooropen.mp3"]
curr_song=None

run=True
play=False
i=0
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                play=not play
                if play:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key==pg.K_RIGHT:
                i+=1
                if i>=len(songlist):
                    i=i-len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()
            elif event.key==pg.K_LEFT:
                i=i-1
                if i<0:
                    i=i+len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()

    pg.display.flip()
    clock.tick(60)
                






''' For shuffle:
import random

def play_a_different_song():
    global curr_song, songlist
    next_song = random.choice(songlist)
    while next_song == curr_song:
        next_song = random.choice(songlist)
    curr_song = next_song
    pg.mixer.music.load(next_song)
    pg.mixer.music.play()
'''
'''For same sequence:

def play_next_song():
    global songlist
    songlist = songlist[1:] + [songlist[0]]
    pygame.mixer.music.load(sognlist[0])
    pygame.mixer.music.play()'''


'''
pg.mixer.music.play(0) 
pg.mixer.music.stop()
'''