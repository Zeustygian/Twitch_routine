# Twitch_channel_routine
This small code aim to check if a given twitch channel is online, and if so, to open it in your default browser.
If offline, ping again every 3 mins.

streamer.txt file is used to save the streamer username 

python ./main.py help

HELP:
/---------------------------------------------------\
| WRITE: python ./main.py [name_of_streamer]        |
|                                                   |
| (streamer name is saved in the streamer.txt file) |
\---------------------------------------------------/


python ./main.py -> use the name of the streamer in streamer.txt


python ./main.py [name] -> check if the streamer is online, if so, open his stream with default browser.
