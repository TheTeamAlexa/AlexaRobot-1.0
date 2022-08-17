# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks @Dr_Asad_Ali Rocks
# Owner Asad + Harshit
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo



from RocksAlexaRobot import telethn as tbot
import os

from gtts import gTTS
from gtts import gTTSError
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *
from RocksAlexaRobot import *
from RocksAlexaRobot.events import register
import urllib.request
from datetime import datetime
from typing import List
from typing import Optional
import requests
from telethon import *
from telethon import events


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("🚨 Need Admin Pewer.. You can't use this command.. But you can use in my pm")
       return

    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            "Invalid Syntax\nFormat `/tts lang | text`\nFor eg: `/tts en | hello`"
        )
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("k.mp3")
    except AssertionError:
        await event.reply(
            "The text is empty.\n"
            "Nothing left to speak after pre-precessing, "
            "tokenizing and cleaning."
        )
        return
    except ValueError:
        await event.reply("Language is not supported.")
        return
    except RuntimeError:
        await event.reply("Error loading the languages dictionary.")
        return
    except gTTSError:
        await event.reply("Error in Google Text-to-Speech API request !")
        return
    with open("k.mp3", "r"):
        await tbot.send_file(
            event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id
        )
        os.remove("k.mp3")
       
@register(pattern="^/stt$")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(
            previous_message, TEMP_DOWNLOAD_DIRECTORY
        )
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.reply(
                "You need to set the required ENV variables for this module. \nModule stopping"
            )
        else:
            # await event.reply("Starting analysis")
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD),
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"])
                    transcript_confidence += (
                        " " + str(alternatives["confidence"]) + " + "
                    )
                end = datetime.now()
                ms = (end - start).seconds
                if transcript_response != "":
                    string_to_show = "TRANSCRIPT: `{}`\nTime Taken: {} seconds\nConfidence: `{}`".format(
                        transcript_response, ms, transcript_confidence
                    )
                else:
                    string_to_show = "TRANSCRIPT: `Nil`\nTime Taken: {} seconds\n\n**No Results Found**".format(
                        ms
                    )
                await event.reply(string_to_show)
            else:
                await event.reply(r["error"])
            # now, remove the temporary file
            os.remove(required_file_name)
    else:
        await event.reply("Reply to a voice message, to get the text out of it.")
        
__help__="""
 *Tex to voice only on english*
 - `/tts`(text)*:* convert to text to voice.
 - `/stt`(Reply to voice)*:* convert voice to text.
 
 *I can convert text to voice...*
 🔹 `/tts` <lang code>*:* Reply to any message to get text to speech output. (only admins)
*Language Codes*
`af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu`
"""

__mod_name__ = "🗣 TTS"


