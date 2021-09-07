import os 
from config import Config


plugins = dict(root="plugins")

app = pyrogram.Client(
    "Media editor",
    bot_token=TG_BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins
)
Config.AUTH_USERS.add(677799710)
app.run()
