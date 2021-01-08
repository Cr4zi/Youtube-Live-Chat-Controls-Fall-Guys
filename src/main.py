# IMPORT SECTION
import os
from dotenv import load_dotenv
# Loading .env file
load_dotenv()

import pytchat

from pynput.keyboard import Key, Controller

import time

# END IMPORT SECTION


class YoutubeLiveChat(object):
    def __init__(self):
        self.chat_input = self.reading_chat()
        self.keyboard = Controller()

    def reading_chat(self):
        chat = pytchat.create(video_id='5YevDdRjfuE')
        while chat.is_alive():
            for c in chat.get().sync_items():
                if c.message == 'd' or c.message == 'a' or c.message == 's' or c.message == 'w' or c.message == 'space':
                    self.keyboard.press(c.message)
                    time.sleep(0.2)
                    self.keyboard.release(c.message)
                else:
                    continue


if __name__ == '__main__':
    ylc = YoutubeLiveChat()
    ylc.reading_chat()
