# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
**This is Permanent Files Sharing Bot!**
Send Me Any File I Will Save It In My Database & Give You A Permanent Public Shareable Link. I Also Works For Channel. Add Me To Channel As Admin with Edit Permission, I Will Add Save Uploaded File in Channel & Add Shareable Button Link. Thanks For Using!

🤖 **My Name:** [SHAREit Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @I_Am_Only_One_1

👥 **Support Group:** [S1 Support BOT](https://t.me/safothebot)

"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @I_Am_Only_One_1

Developer is Super Noob. Just Learning from Official Docs. Please Donate The Developer For Keeping The Service Alive!✌️✌️

👻NB: Remember That, Developer Will Delete Adult Contents From Database. So Better Don't Store Those Kind of Things🤬🤬

👉To Donate Please [Contact Me!](https://t.me/I_Am_Only_One_1)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **SHAREit Bot**!! 🔥

Send Me Any File I Will Give You A Permanent Sharable Link. I Support Channel Also! Check Details In **About Bot** Button. Thank You!!
"""
