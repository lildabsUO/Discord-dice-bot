import discord
from typing import Optional
from discord import app_commands
from discord.ext.commands import MissingPermissions
from random import randint

class aclient(discord.Client): 
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def  on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await bot.sync()
            self.synced = True
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

client = aclient()
bot = app_commands.CommandTree(client)



@bot.command(name="roll", description="roll a dice")
async def self(interaction: discord.Interaction):

    Num1 = randint(1, 6)
    Num2 = randint(1, 6)
    Num3 = randint(1, 6)

    await interaction.response.send_message(f"{Num1}, {Num2}, {Num3}")



client.run("Youre token here")