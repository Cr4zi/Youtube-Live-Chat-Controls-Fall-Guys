# IMPORT SECTION
import os
from dotenv import load_dotenv
# Loading .env file
load_dotenv()

import pytchat

from pynput import mouse, keyboard

# END IMPORT SECTION


class YoutubeLiveChat(object):
    def __init__(self):
        self.chat_input = self.reading_chat()

    def reading_chat(self):
        chat = pytchat.create(video_id='Yfr1zUw3o1I')
        while chat.is_alive():
            for c in chat.get().sync_items():
                if c.message == 'd' or c.message == 'a' or c.message == 's' or c.message == 'w':
                    return c.message
                else:
                    continue

    def move_in_game(self):
        pass


if __name__ == '__main__':
    ylc = YoutubeLiveChat()
    ylc.reading_chat()
