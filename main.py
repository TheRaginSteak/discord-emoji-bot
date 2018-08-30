"""A discord bot to do dumb emoji stuff"""

from string import ascii_lowercase
import discord

TOKEN = "NDAyNTU5NTc2NDU4OTE5OTQ2.DmnfFw.ixCEUKx5bX2kecgE2qyhyEiRcVs"

client = discord.Client()

CHAR_TO_EMOJI_DICT = {
    "a":":a:",
    "b":":b:",
    "o":":o2:",
    "!":":exclamation:",
    "?":":question:",
    "0":":zero:",
    "1":":one:",
    "2":":two:",
    "3":":three:",
    "4":":four:",
    "5":":five:",
    "6":":six:",
    "7":":seven:",
    "8":":eight:",
    "9":":nine:",
    "+":":heavy_plus_sign:",
    "-":":heavy_minus_sign:",
    "$":":heavy_dollar_sign:",
    " ":" "
}

@client.event
async def on_message(message):
    """For functions that trigger on a button press"""
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


client.run(TOKEN)
