import pygame
import os
import time
import random
import config

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def list_songs():
    song_files = os.listdir("songs")
    return [song for song in song_files if song.endswith((".mp3", ".ogg"))]

def play_song(song):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(os.path.join("songs", song))
        pygame.mixer.music.play()
    except pygame.error:
        input("Unable to play/load the selected song. Press Enter to continue...")

def main():
    clear_screen()
    print("Welcome to SGPlayer!\n")
    
    songs = list_songs()
    
    if not songs:
        input("No songs found in the 'songs' directory. Press Enter to exit...")
        return
    
    while True:
        clear_screen()
        print("Choose a song:\n")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song}")
        print("\n0. Exit")
        
        choice = input("\nEnter the number of the song you want to play (0 to exit): ").strip()
        
        if choice == "0":
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(songs):
                selected_song = songs[choice - 1]
                clear_screen()
                print(f"Playing '{selected_song}'... [ {time.ctime()} ]\n")
                play_song(selected_song)
        except (ValueError, IndexError):
            input("Invalid input. Press Enter to continue...")

if __name__ == "__main__":
    main()
