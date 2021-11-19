from pyrogram import Client, filters
from pyromod import listen
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InputMediaPhoto,InputMediaDocument,InputMediaVideo,InputMediaAnimation,InputMediaAudio
from asyncio import TimeoutError
import os
PACK = filters.animation | filters.document| filters.video|filters.audio |filters.photo
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(PACK  & filters.private)
async def media(client, message):
     if message.chat.id not in Config.AUTH_USERS:
        return
     if message.photo:
        file_id = message.photo.file_id
        mid = InputMediaPhoto(file_id, caption=message.caption and message.caption.html)

     elif message.document:
        file_id = message.document.file_id
        mid = InputMediaDocument(file_id, caption=message.caption and message.caption.html)

     elif message.video:
        file_id = message.video.file_id
        mid = InputMediaVideo(file_id, caption=message.caption and message.caption.html)

     elif message.animation:
        file_id = message.animation.file_id
        mid = InputMediaAnimation(file_id, caption=message.caption and message.caption.html)

     elif message.audio:
          file_id  = message.audio.file_id
          mid = InputMediaAudio(file_id, caption=message.caption and message.caption.html)
     else:
         print('no way')

     try:
         a = await client.ask(message.chat.id,'Now send me the link of the message of the channnel that you need to edit',
                    filters=filters.text, timeout=30)

     except TimeoutError:
           await message.reply_text(
             "```Session Timed Out. Resend the file to Start again```",
             parse_mode="md",
             quote=True
           )
           return
     link = a.text
     a = "-100"
     try:
         id = link.split('/')[4]
         msg_id = link.split('/')[5]
         cd = a + str(id)
         chid = int(cd)

     except:
          chid = link.split('/')[3]
          msg_id = link.split('/')[4]    
     try:
         is_admin=await client.get_chat_member(chat_id=chid, user_id=message.from_user.id)
     except UserNotParticipant:
          await message.reply("It seems you are not a member of this channel and hence you can't do this action.")
          return
     if not is_admin.can_edit_messages:
        await message.reply("You are not permited to do this, since you do not have the right to edit posts in this channel.")
        return
            
     try:
        await client.edit_message_media(
               chat_id = chid,
               message_id = int(msg_id),
               media = mid
              )
     except Exception as e:
           await message.reply_text(e)
           return
     await message.reply_text("**successfully Edited the media**",
             parse_mode="md",
             quote=True
           )

         
   
