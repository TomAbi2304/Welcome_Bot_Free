import json
import discord
import asyncio
from colorama import *
from discord.ui import *
from discord.ext import commands
from discord.utils import get

def get_config(name):
    with open("config.json", "r") as f:
        json_file = json.load(f)
        return json_file[name]

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = get_config("prefix"), intents = intents)

client.remove_command('help')

servers = [int(get_config("guild_id"))]

@client.event
async def on_ready():
    print("██████╗  ██████╗ ████████╗    ██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗")
    print("██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝")
    print("██████╔╝██║   ██║   ██║       ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ")
    print("██╔══██╗██║   ██║   ██║       ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ")
    print("██████╔╝╚██████╔╝   ██║       ██║  ██║███████╗██║  ██║██████╔╝   ██║   ")
    print("╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ")

    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f"Made by TomAbi"),
        status=discord.Status.do_not_disturb)
    await asyncio.sleep(5)

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, id=int(get_config("role_id")))
    channel = client.get_channel(int(get_config("welcome_channel")))
    embed = discord.Embed(title="\👋 Willkommen", color=0xff0000)
    embed.add_field(name="Name:", value=f"{member.name}", inline=False)
    embed.add_field(name="Mention:", value=f"{member.mention}", inline=False)
    embed.add_field(name="Discord-ID:", value=f"{member.id}", inline=False)
    embed.add_field(name="Account erstellt:", value=f"<t:{int(round(member.created_at.timestamp()))}:R> (<t:{int(round(member.created_at.timestamp()))}:f>)", inline=False)
    embed.add_field(name="Server beigetreten:", value=f"<t:{int(round(member.joined_at.timestamp()))}:R> (<t:{int(round(member.joined_at.timestamp()))}:f>)", inline=False)
    embed.set_author(name="TomAbi", icon_url="")
    embed.set_footer(text="Offizieller Bot by !Tomabi", icon_url="")
    embed.set_image(url="")
    embed.set_thumbnail(url=member.avatar.url)
    
    embed2 = discord.Embed(title="\👋 Willkommen", description=f"Hey, {member.mention} welcome to **TomAbi**", color=0xff0000) # Sendet eine DM an den Member

    await channel.send(embed=embed)
    await member.send(embed=embed2)
    await member.add_roles(role)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(int(get_config("leave_channel")))
    embed = discord.Embed(title = "\👋 Verlassen", description=f"**{member.name}** hat den Server verlassen.", color=0xff0000)
    await channel.send(embed=embed)

client.run(get_config("token"))
