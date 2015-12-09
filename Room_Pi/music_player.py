# play a music file using module pygame
# (does not create a GUI frame for now)
# Muzi

#play a list in order

import sys
import pygame as pg
import getopt


class music_player():
    def __init__(self):#build a playlist and play it in order
        print "1111111"
        #sys.path.append('/path/to/~/Documents/Music_player/playlist/') #from another folder
        self.play_list_END = pg.USEREVENT+1
        file = open('playlist.txt','r') #Three sound effects I have
        #lines = file.readlines()
        self.play_list = []
        for line in file :
            self.play_list.append(line.split("\n")[0])
            print "line in file",line
        #file.close()
        print "playlist",self.play_list
        self.index = 0
        song_volume = 0.2 #default volume
        pg.init()#init pygame
        #pg.display.set_mode((500,500)) #menu window
        pg.mixer.music.set_volume(song_volume)# set default volume
        pg.mixer.music.set_endevent(self.play_list_END)#used to check song ends
        pg.mixer.music.load(self.play_list[0])#start from the very first song
        pg.mixer.music.play()

        self.music_status = "stop" #stop pause playing
        self.track_name = {} #track song name, the default is the first one in playlist
        #check the end of a event(here i.e. song) if true then go to next track.
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == self.play_list_END:
                    song = (song+1)%len(self.play_list) #recycle the playlist when the last song is playing
                    pg.mixer.music.load(self.play_list[song])
                    pg.mixer.music.play()


    #Let user change volume
    def change_volume(self,vol):
        song_volume = vol
        pg.mixer.music.set_volume(song_volume)
        if command == "increase":
            song_volume =+ 0.1
            elif command == "decrease" :
                song_volume -= 0.1
            else song_volume = 0.2  #default if no "change" command received

    #when it's going to stop (not like pause)
    def music_fadeout(self, fade_out_time):
        pg.mixer.fadeout(fade_out_time)
        self.play_list[self.index].play()


    #activate the player and start playing music
    def activate_player(self,activate_command):
        if activate_command == 'activate':
            print"Player activated"
            #call init_player
            self.music_status = "playing"
            self.track_name = self.play_list[self.index]
        print "Play awaiting"
        #what if not activated ????

    #play the next song in list
    def go_next(self,voice_command):
        if pg.mixer.get_busy() : #currently playing
            pg.mixer.music.pause()
        print"Playing next song~~"
        self.index+=1 #point to the next
        if self.index >= len(self.play_list): #in case it's the last song in list
            self.index = 0
            #if not self.loop:
            #playNextSong = False
            pg.mixer.music.stop()
            #self.loadSong()
        self.track_name = self.play_list[self.index] #track the next song name
        pg.mixer.music.load(self.play_list[self.index])
        pg.mixer.music.play()

    #pause it
    def pause(self):
        """
        Pauses the current song.

        You can resume using `un_pause/play`.
        """
        pg.mixer.music.pause()
        self.playing = False

    def un_pause(self):
        pg.mixer.music.unpause()
        self.music_status = "playing"
        #self.playing = True # Does it work? or need to reload music?
        #pg.mixer.music.load(self.play_list[self.index])#start from the very first song
        #pg.mixer.music.play()

    def stop(self):
        #Stops the current song and goes to the beginning.
        pg.mixer.music.stop()
        self.music_status = "stopped"
        self.index = 0 #back to beginning of list(default 0)

    def previousSong(self):
        #Returns to the previous song in the playlist.
        if pg.mixer.get_busy() : #currently playing
            pg.mixer.music.pause()
        print"Playing previous song~~"
        self.index -= 1
        if self.index < 0:
            self.index = len(self.play_list) - 1
            self.stop()
        self.track_name = self.play_list[self.index]
        pg.mixer.music.load(self.track_name)
        pg.mixer.music.play()


def main(self):     # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        go_next(arg)


if __name__=="__main__":
    main()
    music_test = music_player() #Test to call this player class
    voice_command = (sys.argv[1:])
