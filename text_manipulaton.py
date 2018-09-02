"""Functions that manipulate text"""

from string import ascii_lowercase
from dictionaries import CHAR_TO_EMOJI_DICT

def text_to_emoji(msg):
    """Takes an input of text and returns the discord emojis for that message"""
    msg_dict = []
    for char in msg:
        if char in CHAR_TO_EMOJI_DICT.keys():
            msg_dict.append(CHAR_TO_EMOJI_DICT[char])
        elif char.lower() in ascii_lowercase:
            msg_dict.append(":regional_indicator_{0}:".format(char.lower()))
    return " ".join(msg_dict)

def clapping(msg):
    return " :clap: ".join(msg.split(" "))
