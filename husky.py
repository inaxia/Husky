import discord
from discord.ext import commands
from datetime import datetime
import reading_from_gsheets
import writing_in_gsheets
from Private import private_keys


#? Setting Prefix
Husky = commands.Bot(command_prefix="!")


#? Husky details
husky_username = ""
husky_avatar_url = ""


#? On Ready event
@Husky.event
async def on_ready():
    husky_username = Husky.user
    husky_avatar_url = Husky.user.avatar_url
    print(f"\nHusky is ready \nusername: {husky_username} \navatar_url: {husky_avatar_url}")


#? Basic Registration Inforation
@Husky.command()
async def husky(ctx):

    # Getting username
    username = str(ctx.author.name)
    print(f"\nusername: {username}")

    # Creating embed
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
        colour = 10181046 # Purple
    )

    # Sending embed
    await ctx.send(embed = embed)


#? Registrtion Process
@Husky.command()
async def register(ctx, *, text): # "*" will take the full sentence

    # Getting timestamp & user avatar url
    timestamp = str(datetime.now()).split(" ")
    user_avatar_url = str(ctx.author.avatar_url)

    # Splitting text to get a list of details
    user = text.split("|")
    for i in range(len(user)):
        user[i] = user[i].strip()

    # Checking if user has alreay registered or not
    is_user_present = reading_from_gsheets.is_available(user[1])
    print(is_user_present)

    # If Already Registered
    if is_user_present[0]: 
        user_data = reading_from_gsheets.get_user_data(is_user_present[1])
        print(user_data)

        embed = discord.Embed(
            title = "Woof! You're Already Registered",
            description = "**Your Details:**\n1. Name: " + user_data[0]
                + "\n2. Email: " + user_data[1]
                + "\n3. Phone: " + user_data[2]
                + "\n4. Age: " + user_data[3]
                + "\n5. City: " + user_data[4]
                + "\n6. Country: " + user_data[5],
            colour = 15158332 # Red
        )
        embed.set_thumbnail(url = user_avatar_url)

        await ctx.send(embed = embed)

    # If Not Registered till now
    else: 
        # Taking more information about user
        user.append(timestamp[0]) # Date
        user.append(timestamp[1]) # Time
        user.append(str(ctx.author))
        user.append(str(ctx.author.id))
        user.append(str(ctx.author.created_at))
        user.append(user_avatar_url)
        user.append(str(ctx.author.permissions_in))
        print(f"\nUser: {user}")

        # Writing user details in sheets
        writing_in_gsheets.add_a_person(user)

        # Giving user MEMBER role
        member = ctx.author
        role = discord.utils.get(member.guild.roles, name="MEMBER")
        await member.add_roles(role)

        # Creating embed
        embed = discord.Embed(
            title = "Woof! Registration completed",
            description = "**Your Details:**\n1. Name: " + user[0]
                + "\n2. Email: " + user[1]
                + "\n3. Phone: " + user[2]
                + "\n4. Age: " + user[3]
                + "\n5. City: " + user[4]
                + "\n6. Country: " + user[5]
                + f"\n\nThank you **{ctx.author.name}** for registering",
            colour = 3066993 # Green
        )
        embed.set_thumbnail(url = user_avatar_url)

        # Sending embed
        await ctx.send(embed = embed)


#? Activate the bot(Husky)
Husky.run(private_keys.discord_token)
