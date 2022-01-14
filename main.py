import discord
from discord.ext import commands
import os
import platform
from server import deploy
# The Discord module is needed so that we can login to your account
# The OS module is for protecting your Discord token (essentially a password to your discord account, do not share it with anyone)
# Platform module is used to make the program easier to use
# to make it Always-Online
# Don't worry, we won't actually log into your account, it's a self bot to do it!

# This is for educational purposes only. I am not responsible
# for your actions.
# I do not encourage Self Bots.
# Self bots are strictly against Discord's TOS and can get you permanantly banned.
# I am displaying this video on an alt account (alternate account)

# Let's go!

# I expect you to have a .env file if you're running the script on a windows PC.
# It'll automatically adjust if it's on Replit.

global TOKEN

deploy() # Get a flask server for UptimeRobot

Client = commands.Bot(intents = Discord.Intents.default()) # Define Client object for user
Client.remove_command("help") # Remove help command so that people can't find out you're using a self bots

if platform.system() == "Windows":
    TOKEN = os.getenv("TOKEN")
else:
    TOKEN = os.environ["TOKEN"]

Client.run(TOKEN)

# Now it's logged into the account!
# Now we'll set up UptimeRobot!
