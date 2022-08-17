
from pyrogram import filters #carbon by vegeta
from RocksAlexaRobot import pgram as pbot, BOT_USERNAME, UPDATES_CHANNEL
from RocksAlexaRobot.utils.errors import capture_err
from RocksAlexaRobot.utils.make_carbon import make_carbon

@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**🙄Reply to a text message to make carbon.**")
    if not message.reply_to_message.text:
        return await message.reply_text("**🙄Reply to a text message to make carbon.**")
    m = await message.reply_text("**⬇Downloading...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**⬆Uploading...**")
    msg = "**Made by @Alexa_Help**"
    await pbot.send_photo(message.chat.id, carbon,caption=msg)
    await m.delete()
    carbon.close()
