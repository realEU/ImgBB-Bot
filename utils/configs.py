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

    OWNER_ID = int(os.environ.get("OWNER_ID", "-1001418249477"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgBB")

    START_PIC = "https://telegra.ph/file/e162f5f8554a9bf66e830.jpg"
    HELP_PIC = "https://telegra.ph/file/e162f5f8554a9bf66e830.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi {},
         I’m **[ImgBB](telegram.me/xImgBBbot)**. I can upload images on **ImgBB.com** & generate shareable link for it! 

BTW, do press **Help** for more information about the process.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](telegram.me/xImgBBbot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Railway](https://railway.app)

👨‍💻 **Developer:** [𖤍 Λℓσηє 𖤍](t.me/xDune)

👥 **Support Group:** [Marine Support](https://t.me/MarineChats)

📢 **Updates Channel:** [Marine Bots](https://t.me/MarineBots)
"""

    HELP_TEXT = """You may have already known my function. As you have seen in the start message, I can upload images on **ImgBB.com** & generate shareable link for it, which can be deleted after a specific time or stay there forever ~ according to your selection...🙃

Steps:
• Post/Forward an image...
• Select an option ~ whether to delete it automatically within the given period or keep it permanently...
• BOOM!💥 Your image is uploaded! You will be provided with a link to view the image, as well as, a link to delete it."""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Has Expired, Revoked, Malformed Or Invalid For Other Reasons. Report this at @MarineBots",

    WAIT = "💬 Please Wait !!"
