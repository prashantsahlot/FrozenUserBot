from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

@app.on_message(filters.command(["sayang", "lover"], ".") & filters.me)
async def zeyenk(client: Client, message: Message):
    e = await message.reply("I LOVE YOUUU 💕")
    await asyncio.sleep(0.2)
    await e.edit("💝💘💓💗")
    await asyncio.sleep(0.2)
    await e.edit("💞💕💗💘")
    await asyncio.sleep(0.2)
    await e.edit("💘💞💕💗")
    await asyncio.sleep(0.2)
    await e.edit("LOVE YOU 💝💖💘")
    await asyncio.sleep(0.2)
    await e.edit("LOVE YOU FOREVER 💕")
    await asyncio.sleep(0.2)
    await e.edit("💘 You're my star 💖")

