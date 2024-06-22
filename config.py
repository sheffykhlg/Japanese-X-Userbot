#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
from distutils.util import strtobool
from XDB.data import MASTERS
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://graph.org/file/ec99cb6dba229bd984537.jpg")
PM_PIC = getenv("PM_PIC", "https://graph.org/file/936ef33023a77fa9a6813.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "e118fcaad4259eee1733c4271044240d")
API_ID = getenv("API_ID", "21338586")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "4.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
BOT_TOKEN = getenv("BOT_TOKEN", "7185684182:AAHH-d3n8eyWBWJTqDf5_GJmAEXPCDQ8F2Q")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://vaibhavraut012:nikhil123@cluster0.ohkhwlk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "khjuhyg")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Team-Japanese/Japanese-X-Userbot")
MONGO_URL = getenv("MONGO_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOMgBuz1X92_2EruG_ozaouw4gj8uW7yS2iqRHXXkKk2TVJxsZBanMsSnojrybA3k-BnixTZ79aSoel6cFzvWGKbLJlmzxZRC45CgBDphBT5jUqKGkvObT8N7-OU5fkBYTPlnqvivN3d39XbAdCKgdhxzRZe0fm5R1OP1pNuWNkWfzLmG0x4RhVPot0nVwrXunurstYpJtaq7NCCBNKeB4attDvn6SaOIidUyngvj5NCb13Knt0bP3-iJ9Cf_u98nkWoJ_BqQup_3xu7j3oFtxNqnnCocJeM1RYmeT8Biz9BNIwtISpmpK1zY1Pgn6yWDrhKCtVS96aPFGJgb2kAAqjpGtuM=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDOS = os.getenv("SUDO_USERS", None)
SUDO_USERS = []

if SUDOS:
    sudos = str(SUDOS).split("7015501852")
    for sudo_id in sudos:
        try:
            SUDO_USERS.append(int(sudo_id))
        except ValueError:
            print(f"Warning: Invalid user ID '{sudo_id}' in SUDO_USERS environment variable.")
            continue
            
OWNER_ID = os.getenv("OWNER_ID", "7015501852")

SUDO_USERS.append(OWNER_ID)
SUDO_USERS.extend(MASTERS)

BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
