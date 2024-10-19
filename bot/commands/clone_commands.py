from pyrogram import Client, filters
from pyrogram.types import Message
import os

original_name = None
original_bio = None

@app.on_message(filters.command("clone", ".") & filters.me)
async def clone(client: Client, message: Message):
    global original_name, original_bio

    if message.reply_to_message:
        user_ = message.reply_to_message.from_user
        if user_:
            user_id = user_.id
        else:
            await message.edit("`Could not retrieve the user ID from the replied message.`")
            return
    else:
        args = message.text.split()
        if len(args) < 2:
            await message.edit("`Please provide a username or user ID to clone or reply to a user's message.`")
            return
        user_id = args[1]

    op = await message.edit("`Cloning...`")
    try:
        user_ = await client.get_users(user_id)
        await op.edit("`User found. Fetching user information...`")
    except Exception:
        await op.edit("`User not found.`")
        return

    user_info = await client.get_chat(user_.id)
    original_name = user_.first_name
    original_bio = user_info.bio if user_info.bio else "join - @frozensupport1"
    
    pic = user_.photo.big_file_id if user_.photo else None
    if pic:
        await op.edit("`Downloading profile picture...`")
        photo = await client.download_media(pic)
        await client.set_profile_photo(photo=photo)
        await op.edit("`Profile picture set.`")

    await op.edit("`Updating profile...`")
    await client.update_profile(first_name=original_name, bio=original_bio)
    
    await op.edit(f"**From now on, I'm** __{original_name}__")

@app.on_message(filters.command("revert", ".") & filters.me)
async def revert(client: Client, message: Message):
    global original_name, original_bio

    await message.edit("`Reverting...`")
    if not original_name or not original_bio:
        await message.edit("`Original name or bio not set.`")
        return

    try:
        await client.update_profile(first_name=original_name, bio=original_bio)
        photos = [p async for p in client.get_chat_photos("me")]
        if photos:
            await client.delete_profile_photos(photos[0].file_id)
        await message.edit("`I am back to my original identity!`")
    except Exception as e:
        await message.edit(f"`Error reverting: {str(e)}`")

