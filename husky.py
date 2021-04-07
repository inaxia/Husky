import discord
from discord.ext import commands
from datetime import datetime
import reading_from_gsheets
import writing_in_gsheets
from Private import private_keys


Husky = commands.Bot(command_prefix="!")


#? Husky details
husky_username = ""
husky_avatar_url = ""


@Husky.event
async def on_ready():
    husky_username = Husky.user
    husky_avatar_url = Husky.user.avatar_url
    print(f"\nHusky is ready \nusername: {husky_username} \navatar_url: {husky_avatar_url}")


@Husky.command()
async def husky(ctx):
    username = str(ctx.author.name)
    print(f"\nusername: {username}")

    embed = discord.Embed(
        title = "Woof! Hii there, I'm Husky",
        description = f"Hello **{username}**, I'm here to help you out with Registration Process."+
            '''
            \nI'd need some basic information from you to know you more and register you in our event. This includes:
            > 1. Your full name
            > 2. Your professional email address
            > 3. Your phone number (with country code)
            > 4. Your age
            > 5. City from where you're hacking
            > 6. Country you are living in
            '''
            +"*All details are compulsory"
            +"\n\n**!register 1 | 2 | 3 | 4 | 5 | 6**"
            +"\nPlease follow this format and provide us the above details."
            +"\n\neg, **!register Husky | husky@gmail.com | +919876543210 | 4 | Delhi | India**",
        colour = 10181046 #? purple
    )
    await ctx.send(embed = embed)


@Husky.command()
async def register(ctx, *, text): #? "*" will take the full sentence
    timestamp = str(datetime.now()).split(" ")
    user_avatar_url = str(ctx.author.avatar_url)

    user = text.split("|")
    for i in range(len(user)):
        user[i] = user[i].strip()

    user.append(timestamp[0]) #* Date
    user.append(timestamp[1]) #* Time
    user.append(str(ctx.author))
    user.append(str(ctx.author.id))
    user.append(str(ctx.author.created_at))
    user.append(user_avatar_url)
    user.append(str(ctx.author.permissions_in))
    print(f"\nUser: {user}")

    writing_in_gsheets.add_a_person(user)

    embed = discord.Embed(
        title = "Woof! Registration completed",
        description = "**Your Details:**\n1. Name: " + user[0]
            + "\n2. Email: " + user[1]
            + "\n3. Phone: " + user[2]
            + "\n4. Age: " + user[3]
            + "\n5. City: " + user[4]
            + "\n6. Country: " + user[5]
            + f"\n\nThank you **{ctx.author.name}** for registering",
        colour = 3066993 #? Green
    )
    embed.set_thumbnail(url = user_avatar_url)

    await ctx.send(embed = embed)


Husky.run(private_keys.discord_token)
