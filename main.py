import os 

plugins = dict(root="plugins")

app = pyrogram.Client(
    "Media editor",
    bot_token=os.environ["TG_BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    plugins=plugins
)

app.run()
