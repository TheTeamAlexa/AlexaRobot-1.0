# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo



import html
import re
from datetime import datetime
from typing import List
import random
from telegram import ChatAction
from gtts import gTTS
import time
from telegram import ChatAction
from feedparser import parse
import json
import urllib.request
import urllib.parse
import requests
from RocksAlexaRobot import (DEV_USERS, OWNER_ID, DRAGONS, SUPPORT_CHAT, DEMONS,
                          TIGERS, WOLVES, dispatcher,updater)
from RocksAlexaRobot.__main__ import STATS, TOKEN, USER_INFO
from RocksAlexaRobot.modules.disable import DisableAbleCommandHandler
from RocksAlexaRobot.modules.helper_funcs.filters import CustomFilters
from RocksAlexaRobot.modules.helper_funcs.chat_status import sudo_plus, user_admin
from telegram import MessageEntity, ParseMode, Update, constants
from telegram.error import BadRequest
from emoji import UNICODE_EMOJI
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

@run_async
def tts(update: Update, context: CallbackContext):
    args = context.args
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    lang="ml"
    tts = gTTS(reply, lang)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        lang = "en"
        tts = gTTS(reply, lang)
        tts.save("k.mp3")
    with open("k.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)


TTS_HANDLER = DisableAbleCommandHandler("tts", tts, pass_args=True)
dispatcher.add_handler(TTS_HANDLER)

__mod_name__ = "🗣️ ᴛᴛs"
__command_list__ = ["tts"]
__handlers__ = [TTS_HANDLER]
