import discord

botToken = ""
botUser = "Verify"


#first we will have the bot check for everyone with a @everyone role
#verified users will have member role
#dm users with @everyone role

#bot will say "please enter your csun email"
for i in range(0,3):
    email = "" 
    #bot check if email contains @my.csun.edu
    def check_Email(str):
        if "@my.csun.edu" in str:
            return True
        return False
    if check_Email(email):
        #give user the role of Member within the discord
        print("hurray!")
        break
        None
    else:
        #bot will say "This email is invalid, please check and make sure the email you sent was correct"
        print("booo!")
        None
if i == 2:
    print("please contact one of the club officers to have this issue resolved")

