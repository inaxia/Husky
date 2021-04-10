## What's the difference between `event` & `command`?

> @Husky.event <br>
Event is a piece of code that is triggered when the bot detects something has happened

> @Husky.command() <br>
Command is a piece of coed which is triggered when a user tells the bot to trigger


## For assigning roles as soon as user joins
```
intents = discord.Intents.default()
intents.members = True

#? Setting Prefix
Husky = commands.Bot(command_prefix="!", intents=intents)

@Husky.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="MEMBER")
    await member.add_roles(role)
```
*You also have to enable privileged intents in the [developer portal](https://discord.com/developers/applications) - [GUIDE](https://discordpy.readthedocs.io/en/latest/intents.html?highlight=intents)


## For commands starting with a number
```
@Husky.commands(aliases=["4to5"])
async def _4to5(ctx):
    ...
```


## References
Documentation: [discordpy.readthedocs.io](https://discordpy.readthedocs.io/en/stable/)<br>
Youtube: [youtube.com/playlist](https://www.youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)<br>
Colors codes for embeds: [gist.github.com/thomasbnt/...](https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812)<br>
Access google sheets in python using Gspread: [codingpub.dev/access-google-sheets-in-python-using-gspread](https://codingpub.dev/access-google-sheets-in-python-using-gspread)<br>
