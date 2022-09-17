## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACnQZYNYSHlkFt_0O2kOvrPxHSDSZ3Oa2fM5k5oSCkQewq0SiwFqfNHVYWPVoWWWBi2NFbPve7V2_XfkahUORP5Bunxj3gSLcIwzJ0CBMsAO2eI6-P8TS9KMD508JRheHPrHgEj_hqHy4luMxEx5jNekBRzFvdbSF6RTVqK0hLALWtk6N2RCKqiaYAixfdTWL3IS3g0LJFeQnunNrn96OBVW5yPH8TIvRv1vHpBY0qs1Q3sP_H8pFtJuCjCs-E73ZxG2lfOypVdoOTkTiAe9kelDo7LMaeX6-yepkdr0osoHNHPmzcxoH1fTWhjOokAiOY-HVzwW7hjfW-ewZxWlEtBAAAAAU4d7CUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5478749117:AAE5Ql3XR8F6cY9lQxYN7QnVNLKDMGVO_4s")
BOT_NAME = getenv("BOT_NAME", "ℤᎾℳᎯ")
API_ID = int(getenv("API_ID", "17026136"))
API_HASH = getenv("API_HASH", "091801a98d6e996b318677650fee8c97")
OWNER_NAME = getenv("OWNER_NAME", "𝐇𝐀𝐙𝐄𝐌 𝐄𝐌𝐀𝐌")
OWNER_USERNAME = getenv("OWNER_USERNAME", "M_R_D_A_D0")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐇𝐀𝐙𝐄𝐌 𝐄𝐌𝐀𝐌")
BOT_USERNAME = getenv("Zomaaa0bot", "")
OWNER_ID = getenv("OWNER_ID", "5739649413")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝙷𝙴𝙻𝙿𝙴𝚁 𝚉𝙾𝙼𝙰 🎼")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bar_zomaa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zomaa00")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5739649413").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
