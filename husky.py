import discord
from discord.ext import commands
from datetime import datetime
import reading_from_gsheets
import writing_in_gsheets
from Private import private_keys


Husky = commands.Bot(command_prefix="*")


#? Husky details
husky_username = ""
husky_avatar_url = ""


#? Basic details
username = ""
name = ""
email = ""
age = ""
city = ""


@Husky.event
async def on_ready():
    husky_username = Husky.user
    husky_avatar_url = Husky.user.avatar_url
    print(husky_username)
    print(husky_avatar_url)


@Husky.command()
async def husky(ctx):
    username = str(ctx.author)
    avatar_url = str(ctx.author.avatar_url)
    print("\nusername: ", username, "\navatar_url: ", avatar_url)

    embed = discord.Embed(
        title = "Woof! Hii there, I'm Husky",
        description = '''
            Hello **''' + username + '''**, I'm here to help you out with Registration Process.

            I'd need some basic information from you to know you more and register you in our event. This includes:
             > 1. Your full name
             > 2. Your professional email address
             > 3. Your valid phone number
             > 4. Your age
             > 5. City from where you're hacking
             > 6. Country you are living in

            ***register 1 | 2 | 3 | 4 | 5 | 6**  
            Please follow this format and provide us the above details.
        ''',
        colour = 10181046 #? purple
    )
    embed.set_thumbnail(url = avatar_url)
    embed.set_footer(
        icon_url = husky_avatar_url,
        text = "Your data will be kept private"
    )
    await ctx.send(embed = embed)


@Husky.command()
async def register(ctx, *, text): #? "*" will take the full sentence
    timestamp = datetime.now()
    username = str(ctx.author.username)

    user = text.split("|")
    for i in range(len(user)):
        user[i] = user[i].strip()

    user.append(username)
    user.append(timestamp)
    print(user)

    writing_in_gsheets.add_a_person(user)
    await ctx.send("Registration completed successfully🐶")


Husky.run(private_keys.discord_token)
