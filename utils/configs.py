import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", "1453690249"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgBB")

    START_PIC = "https://i.imgur.com/zYIllxt.jpg"
    HELP_PIC = "https://i.imgur.com/AmxAlix.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi {},
         I’m [ImgBBbot](telegram.me/xImgBBbot). I can generate shareable link for the images you send which will be uploaded to imgbb.com!

BTW, do press **Help** for more information about the process.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](telegram.me/xImgBBbot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Railway](https://railway.app)

👨‍💻 **Developer:** [𖤍 Λℓσηє 𖤍](t.me/xDune)

💡 **Source Code:** [Github](https://github.com/AmineSoukara/ImgBB-Bot)

👥 **Support Group:** [Marine Support](https://t.me/MarineChats)

📢 **Updates Channel:** [Marine Bots](https://t.me/MarineBots)
"""

    HELP_TEXT = """💡 Just Send Me An Image And I'll Upload it To You .  That's it!
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Has Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @xDune",

    WAIT = "💬 Please Wait !!"
