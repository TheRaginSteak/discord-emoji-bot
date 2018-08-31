"""Module to play sound effects"""

import sys
import discord
from discord import opus

async def on_ready():
    """Run when the bot connects, loads either an x64 or an x86 version of opus"""
    if sys.maxsize > 2 ** 32:
        opus.load_opus("libopus-0.x64.dll")
    else:
        opus.load_opus("libopus-0.x86.dll")