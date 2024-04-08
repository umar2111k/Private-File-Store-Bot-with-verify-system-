# (c) @Illegal_Developer || @Kunal Singh

import os, re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
	ID = {}
	API_ID = int(os.environ.get("API_ID", "977080"))
	API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5991682088:AAFArp6xqU0vY52Lgo4YTy7Y65Dwvli3ACY")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "thunder_store3_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001896983424"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "onepagelink.in")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "4468800fe08226c1102ca7a0e72dc67f3fb72232")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "399726799"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.zglig1z.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001336576681")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001896983424") 
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True)) 
	# verification 
	VR_SITE = os.environ.get('VR_SITE', "onepagelink.in")
	VR_API = os.environ.get('VR_API', "4468800fe08226c1102ca7a0e72dc67f3fb72232")
	VERIFY = is_enabled((os.environ.get('VERIFY', "True")), True)	
	VERIFY_TXT = """Hey {},\n\nʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ. ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ ᴏɴᴇ ᴅᴀʏ\n\n<b>ಇಂದು ನೀವು verify ಮಾಡಿಲ್ಲ.. ಆದ ಕಾರಣ ಕೆಳಗಿರುವ ಲಿಂಕ್ ಅನ್ನು ಒತ್ತಿ verify ಮಾಡಿ indu ರಾತ್ರಿ 12am ತನಕ unlimited ಉಚಿತವಾಗಿ movie ಗಳನ್ನ ಪಡೆಯಿರಿ\n\n<b>इस बॉट को इस्तेमाल करने के लिए आपको रोजाना 1 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे"""
	VERIFY_COMPLETE_TEXT = """Hey. {}.\n\nʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪғɪᴇᴅ ғᴏʀ ᴛᴏɴɪɢʜᴛ 12:00ᴀᴍ ... ᴇɴɪᴏʏ ʏᴏᴜʀ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ʏᴏᴜʀ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ🧑‍🎤 ...\n\n#Completed"""	
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot By Illegal Developer

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [ILLEGAL DEVELOPER](https://t.me/illegaldeveloperbot) 
│
├🔸 **Update Channel:** [Update Channel](https://t.me/illegal_developer)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
 I am Super noob Please Support My Hard Work.
"""
	ABOUT_DEV_TEXT = """<b>Are You A Free User? Then Upgrade Your Plan.</b>
 
 Or Buy Premium Just  ₹30 or $ 0.55 And Use the Available Shortner Sites or Can Request Sites.
 
 You can Pay Using Upi Id 
 
 After Doing Payment Send Screenshots Of Payment To Admin"""
	
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

<b><u>How to Use Bot & it's Benefits??</b></u>

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ <b>PORNOGRAPHY CONTENTS</b> are strictly prohibited & get Permanent Ban..
"""
