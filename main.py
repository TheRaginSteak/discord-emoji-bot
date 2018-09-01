"""A discord bot to do dumb emoji stuff"""

import json
import discord
import text_manipulaton
import sfx

with open("config.json") as data:
    BOT_CONFIG = json.load(data)

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

    if message.content.startswith("$sfx"):
        if message.author.voice_channel != None:
            voice_sample = message.content[5::]
            try:
                await client.send_message(message.channel, "Playing '{}.mp3'".format(voice_sample))
                voice = await client.join_voice_channel(message.author.voice_channel)
                player = voice.create_ffmpeg_player("{}.mp3".format(voice_sample))
                player.start()
            except discord.errors.ClientException:
                pass
        else:
            await client.send_message(message.channel, "Error: Please join a voice channel")
        try:
            while True:
                if player.is_done():
                    await voice.disconnect()
                break
        except discord.errors.ClientException:
            pass


client.run(BOT_CONFIG["token"])
