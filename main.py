"""A discord bot to do dumb emoji stuff"""

import json
import discord
from text_manipulaton import text_to_emoji, clapping

with open("config.json") as data:
    BOT_CONFIG = json.load(data)

client = discord.Client() # pylint: disable=C0103

@client.event
async def on_ready():
    """Run when the bot connects to the server"""
    print('Logged in\nName: {}\nId: {}\n'.format(client.user.name, client.user.id))


@client.event
async def on_message(message):
    """For functions that trigger on a message"""
    # Ignores command if the bot sent it
    if message.author == client.user:
        return

    # A message will be sent to the chat with the command message written in emojis
    if message.content.startswith("$emoji"):
        await client.send_message(message.channel, text_to_emoji(message.content[7::]))
        print(("Message '{}' sent on server '{}'.").format(message.content[7::], message.server))

    # Sends the message with clap emojis between each word
    if message.content.startswith("$clap"):
        await client.send_message(message.channel, clapping(message.content[6::]))

    # Sends the sound effect to a voice channel
    if message.content.startswith("$sfx"):
        if message.author.voice_channel != None:
            voice_sample = message.content[5::]
            try:
                await client.send_message(message.channel, "Playing '{}.mp3'".format(voice_sample))
                voice = await client.join_voice_channel(message.author.voice_channel)
                player = voice.create_ffmpeg_player("sfx/{}.mp3".format(voice_sample))
                player.start()
                while True:
                    if player.is_done():
                        await voice.disconnect()
                        break

            except discord.errors.ClientException:
                pass
        else:
            await client.send_message(message.channel, "Error: Please join a voice channel")

    # If a command is attempted that doesn't exist, this is triggered
    elif message.content.startswith("$"):
        await client.send_message(message.channel, "Command '{}' not recognised".format(message.content.split(" ")[0]))

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    #await send_message

client.run(BOT_CONFIG["token"])
