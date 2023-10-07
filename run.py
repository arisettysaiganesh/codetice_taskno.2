import os
import subprocess
import webbrowser

IS_WINDOWS = os.name == "nt"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice(options):
    while True:
        choice = input("\n>>> ").lower().strip()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

def play_songs():
    clear_screen()
    print("SGPlayer Audio\n"
          "===================")
    print("\n"
          "1. Play Playlist (Python)\n"
          "2. Play A Song (Python 3)\n"
          "i. Info\n"
          "0. Back")
    choice = user_choice(["1", "2", "i", "0"])
    
    if choice == "1":
        subprocess.call(("python", "play.py"))
    elif choice == "2":
        subprocess.call((sys.executable, "playr.py"))
    elif choice == "i":
        clear_screen()
        print("PiePlayer Audio\n"
              "===================")
        print("\n"
              "Playlist:\n"
              "The Playlist is looped and shuffled!\n"
              "\n"
              "Play Song:\n"
              "Choose a song to play (is not looped)")
        input("\n"
              "Back")

def main():
    clear_screen()
    print("SGPlayer\n"
          "================")
    print("\n"
          "l. Play Songs\n"
          "w. Find Songs on the web")
    choice = user_choice(["l", "w"])

    if choice == "l":
        play_songs()
    elif choice == "w":
        webbrowser.open("https://ganna.com")
        print("Opening, please wait...")
        input("Press Enter to continue.")
        main()

if __name__ == "__main__":
    main()
