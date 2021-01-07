# IMPORT SECTION
import os
from dotenv import load_dotenv
# Loading .env file
load_dotenv()

from pynput import mouse, keyboard

from googleapiclient.discovery import build

# END IMPORT SECTION


class YoutubeLiveChat(object):
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))

    def reading_chat(self):
        pass

    def move_in_game(self):
        pass


if __name__ == '__main__':
    ylc = YoutubeLiveChat()
