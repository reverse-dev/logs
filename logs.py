import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="&", intents=intents)

intents.message_content=True
intents.members=True

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot connecté...")
    print("Commandes syncronisée...")
    print("Good")

@bot.command()
async def logs(ctx):
    category = discord.utils.get(ctx.guild.categories, name="logs")
    await category.guild.create_text_channel(name="logs-mods")
    await category.guild.create_text_channel(name="logs-roles")
    await category.guild.create_text_channel(name="logs-ban")
    embed = discord.Embed(title="Logs", description="Les logs ont été créés dans les catégories 'logs-mods', 'logs-roles', et 'logs-ban'.", color=discord.Color.blue())
    await ctx.send(embed=embed)


bot.run("")
