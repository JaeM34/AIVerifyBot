import discord

botToken = "OTM1MjQyMzExNTE5MDc2NDMz.Ye7yRw.GBmK9dc7VIeGphZ0qD5w7SGZoLw"
verifyChannelID = 935243599359119410
botUser = "Verify"

client = discord.Client()

verifyChannel = client.get_channel(verifyChannelID)


# This event is fired when a new user joins the discord
# Notifies user that they must type their CSUN email to get access
@client.event
async def on_member_join(member):
    await verifyChannel.send("Welcome to the AI discord " + member.nick + "!")
    await verifyChannel.send("Please send your CSUN email to gain access to the discord")


# This event is fired every time a message is sent, check discord.py API for more information
# Method will check if the message originated from the verification channel linked via channel ID
# If true, message will go through verify_csun_email method
# Author: Justin
@client.event
async def on_message(message):
    # Message author id is the bot's ID. This is so that the bot does not check its own message
    if message.channel.id == verifyChannelID and message.author.id != 935242311519076433:
        verify_csun_email(message)


# Checks if given string contains @my.csun.edu
# Author: Daniel
def check_Email(str):
    if "@my.csun.edu" in str:
        return True
    return False


# first we will have the bot check for everyone with a @everyone role
# verified users will have member role
# dm users with @everyone role
# Author: Daniel

# bot will say "please enter your csun email"
def verify_csun_email(message):
    for i in range(0, 3):
        email = message
        # bot check if email contains @my.csun.edu
        if check_Email(email):
            # give user the role of Member within the discord
            verifyChannel.send("hurray!")
            break
            None
        else:
            # bot will say "This email is invalid, please check and make sure the email you sent was correct"
            verifyChannel.send("booo!")
            None
    if i == 2:
        verifyChannel.send("please contact one of the club officers to have this issue resolved")


# Starts up the discord bot, check the discord API for more information
client.run(botToken)
