import discord
from discord.ext import commands
import reading_from_gsheets
import writing_in_gsheets
from Private import private_keys

Husky = commands.Bot(command_prefix="*")

#* Basic details
username = ""
name = ""
email = ""
age = ""
city = ""

@Husky.event
async def on_ready():
    print("{0.user} is ready".format(Husky))

@Husky.command()
async def husky(ctx):
    await ctx.send("Please provide your details like this:\n*register name | email | age | city")

@Husky.command()
async def register(ctx, *, text): #? "*" will take the full sentence
    username = str(ctx.author)
    print(username, type(username), "\n")

    user = text.split("|")
    for i in range(4):
        user[i] = user[i].strip()
    print(user, "\n")

    user.append(username)
    print(user)

    writing_in_gsheets.add_a_person(user)
    await ctx.send("Registration completed successfully🐶")

Husky.run(private_keys.discord_token)
