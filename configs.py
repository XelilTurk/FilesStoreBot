# (c) @I_Am_Only_One_1

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
**This Is Permanent Files Store Bot!**
__Send Me Any File I will Save It in My Database & Give You A Permanent Shareable Link. I Also Works For Channel. Add Me To Channel As Admin with Edit Permission, I will Save Uploaded File in Channel & Add Shareable Button Link. Wanna Try Now?__

π€ **My Name:** [Store & Share](https://t.me/{BOT_USERNAME})

π **Language:** [Python-3](https://www.python.org)

π **Library:** [Pyrogram](https://docs.pyrogram.org)

π‘ **Hosted on:** [Heroku](https://heroku.com)

π§π»βπ» **Developer:** [Asm Safone](https://t.me/I_Am_Only_One_1)

π₯ **Support Group:** [Bots Support](https://t.me/safothebot)

"""
	ABOUT_DEV_TEXT = f"""
π§π»βπ» **Developer:** [Asm Safoneβ€οΈ](https://t.me/I_Am_Only_One_1)

Developer is Super Noob. Just Learning from Official Docs. Please Donate The Developer For Keeping The Service Alive!βοΈβοΈ

πRemember That, Developer will Delete Adult Contents From Database. So Better Don't Store Those Kind of Things. Be Careful !π€¬π€¬

π»__Any Issue Please [Contact Me](https://m.me/cadet.safone) (Facebook)!__
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **Store & Share Bot!!** π₯

Send Me Any File I will Give You Permanent Shareable Link. Supports Channel Also! For Details Click On **About Bot** Button. Thank You !!π
"""
