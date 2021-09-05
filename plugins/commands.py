from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Hi {}
  
I am an Media Editor bot ...

You can edit document,video,gif,audio,photo etc..

For More hit /help **

"""


HELP_MSG = """
Follow the step..

🌀First send me an media that you need to replace the other one

🌀Send the link of the media that you need to Edit

NB: Note the bot is admin in the channel 

"""






@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="OWNER",url = "t.me/jack_of_tg")]]),
        reply_to_message_id=message.message_id
    )    



@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=HELP_MSG,
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )    
