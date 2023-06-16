# Twitch API    pip install twitch-python
import twitch
import os
import time
import sys
import ctypes

bar_up = "/---------------------------------------------------\\"
bar_down = "\---------------------------------------------------/"
space = "                                                   "

def check_streamer_file():
    if (os.path.isfile("./streamer.txt") == False):
        print("Streamer file does not exist.")
        exit()

if (len(sys.argv) == 2 and sys.argv[1] == "help"):
    print("HELP:\n" + bar_up + "\n| WRITE: python ./main.py [name_of_streamer]        |\n|" + space + "|\n| (streamer name is saved in the streamer.txt file) |\n" + bar_down)
    exit()

if (len(sys.argv) == 2):
    file = open("streamer.txt", "w")
    file.write(sys.argv[1])
    streamer = sys.argv[1]
    if (streamer.isalpha() == False):
        print("Streamer name must only contains alphanumeric characters please.")
        exit()
    file.close

if (len(sys.argv) == 1):
    check_streamer_file()
    file = open("streamer.txt", "r")
    streamer = file.readline()
    if (streamer.isalpha() == False):
        print("Streamer name must only contains alphanumeric characters please.")
        exit()
    file.close

helix = twitch.Helix("HELLO", "WORLD")
condition = True

while (True):
    for user in helix.users([streamer]):
        print("Is " + user.display_name + " live ?", user.is_live)
    if (user.is_live == True):
        print("Opening his live.")
        time.sleep(1.5)
        user_response = ctypes.windll.user32.MessageBoxW(0, streamer + " is streaming, do I open his stream ?", "Twitch_routine", 4)
        if (user_response == 6):
            os.system("explorer https://www.twitch.tv/" + streamer)
        break
    time.sleep(180)
