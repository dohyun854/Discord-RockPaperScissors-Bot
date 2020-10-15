import discord
import configparser
import asyncio
import random
import os


client = discord.Client()


@client.event
async def on_ready():
    a = configparser.ConfigParser()
    print(client.user.id)
    print("ready")
    game = discord.Game("+help+")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('+RPS+'):
        rsp = ["Rock","Paper","Scissors"]
        embed = discord.Embed(title="Rock Paper Scissors",description="Playing Rock Paper Scissors. Please type [Rock/Paper/Scissors] in 10 seconds!", color=0x00aaaa)
        channel = message.channel
        msg1 = await message.channel.send(embed=embed)

        def check(m):
            return m.author == message.author and m.channel == channel

        try:
            msg2 = await client.wait_for('message', timeout=10.0, check=check)

        except asyncio.TimeoutError:
            await msg1.delete()
            embed = discord.Embed(title="Rock Paper Scissors",description="10 second time out!", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return

        else:
            await msg1.delete()
            bot_rsp = str(random.choice(rsp))
            user_rsp  = str(msg2.content)
            answer = ""
            if bot_rsp == user_rsp:
                answer = "I chose " + bot_rsp + " and you chose " + user_rsp + ".\n" + "Draw!"
            elif (bot_rsp == "Scissors" and user_rsp == "Rock") or (bot_rsp == "Paper" and user_rsp == "Scissors") or (bot_rsp == "Rock" and user_rsp == "Paper"):
                answer = "I chose " + bot_rsp + " and you chose " + user_rsp + ".\n" + "Congrats! You won!"
            elif (bot_rsp == "Rock" and user_rsp == "Scissors") or (bot_rsp == "Scissors" and user_rsp == "Paper") or (bot_rsp == "Paper" and user_rsp == "Rock"):
                answer = "I chose " + bot_rsp + " and you chose " + user_rsp + ".\n" + "You lost, I won!!"
            else:
                embed = discord.Embed(title="Rock Paper Scissors",description="Choose Rock, Paper, or Scissors!!", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title="Rock Paper Scissors",description=answer, color=0x00aaaa)
            await message.channel.send(embed=embed)
            return

    if message.content.startswith("+help+"):
        embed = discord.Embed(title="Discord Best [Rock Paper Scissors] Game Bot.", color=0x9694ff)
        embed.set_author(name="Bot Commands")
        embed.add_field(name="+help+", value="Get help", inline=True)
        embed.add_field(name="+invite+", value="Invite this bot", inline=True)
        embed.add_field(name="+support+", value="Get support", inline=True)
        embed.add_field(name="+donate+", value="Donate to bot developer", inline=True)
        embed.add_field(name="+RPS+", value="Play [Rock Paper Scissors] game with this bot", inline=False)
        embed.set_footer(text="Bot made by Codeman#0001")
        await message.channel.send(embed=embed)

    if message.content.startswith("+invite+"):
        embed = discord.Embed(title="Invite Me!",
                                  url="https://discord.com/oauth2/authorize?client_id=742716258394439691&scope=bot&permissions=60416",
                                  color=0xffe66b)
        embed.set_author(name="RPS Bot Invite")
        embed.set_footer(text="Thanks for inviting me!")
        await message.channel.send(embed=embed)

    if message.content.startswith("+support+"):
        embed = discord.Embed(title="DM Codeman#0001 to get support", color=0x8095ff)
        embed.set_author(name="Get Bot Support")
        embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMDA4MjhfMjM4/MDAxNTk4NTg1MTcwNDU3.tw9dy7KDcWJ02-g50DeSeGN57JCS5zoxmVhuxT2bWSkg.ibbzJQ2xtgOQ3_EuUGI3gP3poeDHbFHzbNIVF_Td6Mog.JPEG.dohyun854/8biticon_512.jpg?type=w1")
        embed.set_footer(text="No spam DMing!!")
        await message.channel.send(embed=embed)

    if message.content.startswith("+donate+"):
        embed = discord.Embed(title="Donate to Bot Developer", url="https://www.patreon.com/Codeman_IT", color=0xceff85)
        embed.set_author(name="Donate")
        embed.set_thumbnail(
            url="https://blogfiles.pstatic.net/MjAyMDA4MjhfMjM4/MDAxNTk4NTg1MTcwNDU3.tw9dy7KDcWJ02-g50DeSeGN57JCS5zoxmVhuxT2bWSkg.ibbzJQ2xtgOQ3_EuUGI3gP3poeDHbFHzbNIVF_Td6Mog.JPEG.dohyun854/8biticon_512.jpg?type=w1")
        embed.set_footer(text="Join developer's fan server too! Link: https://discord.gg/xbn8hzM")
        await message.channel.send(embed=embed)

    if message.content.startswith("+easter-egg+"):
        await client.get_user(718457550038761583).send("이름, 프사 바꿔")

    if message.content.startswith("이름, 프사 바꿔"):
        user = client.get_user(718457550038761583)
        await user.send("이름, 프사 바꿔")

client.run(os.environ['token'])

#invite: https://discord.com/oauth2/authorize?client_id=742716258394439691&scope=bot&permissions=60416
