"""A discord bot to do dumb emoji stuff"""

import discord
import text_manipulaton

TOKEN = "NDAyNTU5NTc2NDU4OTE5OTQ2.DmnfFw.ixCEUKx5bX2kecgE2qyhyEiRcVs"

client = discord.Client()

@client.event
async def on_ready():
    """Run when the bot connects to the server"""
    print('Logged in\nName: {}\nId: {}\n'.format(client.user.name, client.user.id))


@client.event
async def on_message(message):
    """For functions that trigger on a message"""
    if message.author == client.user:
        return

    if message.content.startswith("$emoji"):
        await client.send_message(message.channel, text_manipulaton.text_to_emoji(message.content[7::]))
        print(("Message '{}' sent on server '{}'.").format(message.content[7::], message.server))

    ##if message.content.startswith("$tts"):
    ##   voice_msg = message.content[5::]
    ##

    #if message.content.startswith("$sfx"):
    #    voice_channel = message.member.voiceChannel


client.run(TOKEN)
