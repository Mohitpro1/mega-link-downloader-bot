import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("6959173063:AAE2xFI9pRGkcttvHJoMjv6C0ofQJ7vUU04") # Make a bot from https://t.me/BotFather and enter the token here
    #If deploying on vps edit the above value as example := TG_BOT_TOKEN = "Your-bot-token-inside-inverted-commas."
    
    APP_ID = int(os.environ.get("22714655")) # Get this value from https://my.telegram.org/apps
    #If deploying on vps edit the above value as example := APP_ID = Your-APP_ID-without-inverted-commas
    
    API_HASH = os.environ.get("e218e19a476b75107fcfeac7dc94233d") # Get this value from https://my.telegram.org/apps
    #If deploying on vps edit the above value as example := API_HASH = "Your-API_HASH-inside-inverted-commas."
    
    Mega_email = os.environ.get("palib61464@visignal.com") # This is not necessary! Enter your mega email only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."
    
    Mega_password = os.environ.get("GuMbpp3gz!p7jEmUQrR&") # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    
    Bot_username = os.environ.get("@MEGALINK_EXTRACTOR_BOT") # Your bot's telegram username (must enter with '@' in the front of the username)
    #If deploying on vps edit the above value as example := Bot_username = "Your-Bot_username-inside-inverted-commas."
    
    OWNER_ID = os.environ.get("6619999543") # Your(owner's) telegram id
    #If deploying on vps edit the above value as example := OWNER_ID = Your-telegram id-without-inverted-commas
    
    REDIS_URI = os.environ.get("redis-10973.c325.us-east-1-4.ec2.cloud.redislabs.com:10973") # Get This Value from http://redislabs.com/try-free (If you don't know how to obtain the a video tutorial is available here:- https://t.me/botzupdate/5)
    #If deploying on vps edit the above value as example := REDIS_URI = "Your-Redis-Endpoint-inside-inverted-commas."
    
    REDIS_PASS = os.environ.get("byvIIprElnn8AzCAAnzb3VJMKebsCTh4") # Get This Value from http://redislabs.com/try-free (If you don't know how to obtain the a video tutorial is available here:- https://t.me/botzupdate/5)
    #If deploying on vps edit the above value as example := REDIS_PASS = "Your-Redis-Password-inside-inverted-commas."

    AUTH_USERS = set(int(x) for x in os.environ.get("2123101495", "5376024745").split()) # Id's of the telegram users, who you want to allow for multitasking - downloading multiple links at once!
    
    #If deploying on heroku separate the ids by space. (don't put commas. Only separate each of the id's with space)
    
    #If deploying on vps edit the above value as example := 
    #AUTH_USERS = set(int(x) for x in (id1, id2)) 👈 Type exactly as that and replace id1 and id2 with the id's of the telegram users, who you want to allow for multitasking. You cand add many users like that!
    
    DOWNLOAD_LOCATION = "./DOWNLOADS" # The download location for users. (Don't change anything in this field!)
    ADMIN_LOCATION = "./ADOWNLOADS" # The download location for auth users. (Don't change anything in this field!)
    CREDENTIALS_LOCATION = "./CREDENTIALS" # Location where your mega.nz credentials for megatools gets saved if you provide them. (Don't change anything in this field!)
