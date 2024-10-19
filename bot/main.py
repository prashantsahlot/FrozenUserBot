from pyrogram import Client
from bot.commands import emoji_commands, clone_commands, love_commands
from bot.helpers.flask_helper import keep_alive
import os

# Load session data from environment
session_string = os.getenv("SESSION_STRING")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)

# Start Flask server to keep the bot running
keep_alive()

# Add your other commands here (already imported)
app.run()

