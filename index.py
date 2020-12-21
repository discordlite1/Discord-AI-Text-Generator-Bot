import discord
from textgenrnn import textgenrnn
from discord.ext import commands
import string
import requests
import time, threading
import asyncio
from pathlib import Path
my_file = Path('/textgenrnn_weights.hdf5')
prefix = "?"
bot = commands.Bot(command_prefix = prefix)
async def textgenerator():
    await bot.wait_until_ready()
    channel = bot.get_channel(541495294857183244)
    while not bot.is_closed():
        if my_file.exists():
            t = textgenrnn('textgenrnn_weights.hdf5')
        else:
            t = textgenrnn()
        t.train_from_file('index.txt', num_epochs = 1)
        generation = (t.generate(1, temperature = 0.5, return_as_list=True,)[0])
        embed=discord.Embed(title="Machiavelli Text Generation", description = generation, color = (0xF48D1))
        await channel.send(embed=embed)
        await asyncio.sleep(1800)
bot.loop.create_task(textgenerator())
bot.run('put token here')
