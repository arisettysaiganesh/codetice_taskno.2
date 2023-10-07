import pygame
import os
import time
import random
import config

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def play_random_song():
    pygame.mixer.init()
    while True:
        clear_screen()
        print("Song Log:\n")
        print("CTRL + C to Exit")
        try:
            song_file = random.choice(config.songs)
            print("Playing a random song... [{}]".format(time.ctime()))
            pygame.mixer.music.load("songs/{}".format(song_file))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        except KeyboardInterrupt:
            clear_screen()
            print("Exiting the Song Player...")
            break
        except Exception as e:
            clear_screen()
            print("Error: Unable to play/load a song!")
            print("Error Details:", str(e))
            input("Press Enter to continue...")

if __name__ == "__main__":
    clear_screen()
    print("Welcome to the SG Random Song Player!\n")
    play_random_song()
