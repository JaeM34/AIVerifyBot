import discord

botToken = "Private token key, message officer for key"
botUser = "Verify"

# Required for bot to be able to view user actions, such as a new member joining
intents = discord.Intents.all()
intents.members = True
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# All IDs for necessary functions
guildID = 918304572311752725
verifyChannelID = 935966588262289419
memberRoleID = 933949657795690517
unverifiedRoleID = 935966800934502470


# This event is fired when a new user joins the discord
# Puts new user a visitor role
# Notifies user that they must type their CSUN email to get access
@client.event
async def on_member_join(member):
    await member.add_roles(client.get_guild(guildID).get_role(unverifiedRoleID))
    await client.get_channel(verifyChannelID).send("Welcome to the AI discord " + member.mention + "!")
    await client.get_channel(verifyChannelID).send("Please send your CSUN email to gain access to the discord")


# This event is fired every time a message is sent, check discord.py API for more information
# Method will check if the message originated from the verification channel linked via channel ID
# If true, message will go through verify_csun_email method
# Once message is verified to be a valid CSUN email, will add member role to user and remove visitor role
# Author: Justin
@client.event
async def on_message(message):
    # Message author id is the bot's ID. This is so that the bot does not check its own message
    if message.channel.id == verifyChannelID and message.author.id != 935242311519076433:
        if await verify_csun_email(message.content):
            await message.author.add_roles(client.get_guild(guildID).get_role(memberRoleID))
            await message.author.remove_roles(client.get_guild(guildID).get_role(unverifiedRoleID))


# Checks if given string contains @my.csun.edu
# Author: Daniel
# Modification: Justin
def check_Email(str):
    return "@my.csun.edu" in str


# first we will have the bot check for everyone with a @everyone role
# verified users will have member role
# dm users with @everyone role
# Author: Daniel
# Modification: Justin

# bot will say "please enter your csun email"
async def verify_csun_email(message):
    email = message
    # bot check if email contains @my.csun.edu
    if check_Email(email):
        # give user the role of Member within the discord
        await client.get_channel(verifyChannelID).send("You email has been verified")
        return True
    else:
        # bot will say "This email is invalid, please check and make sure the email you sent was correct"
        await client.get_channel(verifyChannelID).send("Invalid CSUN email, please try again")
    return False


# Starts up the discord bot, check the discord API for more information
client.run(botToken)
