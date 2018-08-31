"""A discord bot to do dumb emoji stuff"""

from string import ascii_lowercase
import discord
import opus_api
from dictionaries import CHAR_TO_EMOJI_DICT

TOKEN = "NDAyNTU5NTc2NDU4OTE5OTQ2.DmnfFw.ixCEUKx5bX2kecgE2qyhyEiRcVs"

client = discord.Client()

#voice_client = discord.VoiceClient()

@client.event
async def on_message(message):
    """For functions that trigger on a message"""
    if message.author == client.user:
        return

    if message.content.startswith("$emoji"):
        msg = message.content[7::]
        msg_dict = []
        for char in msg:
            if char in CHAR_TO_EMOJI_DICT.keys():
                msg_dict.append(CHAR_TO_EMOJI_DICT[char])
            elif char.lower() in ascii_lowercase:
                msg_dict.append(":regional_indicator_{0}:".format(char.lower()))
        await client.send_message(message.channel, " ".join(msg_dict))

    ##if message.content.startswith("$tts"):
    ##   voice_msg = message.content[5::]
    ##

    #if message.content.startswith("$sfx"):
        

client.run(TOKEN)
