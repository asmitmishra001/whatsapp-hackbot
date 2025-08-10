from pyrogram import Client, filters
from pyrogram.types import MenuButtonWebApp, WebAppInfo

api_id = 22528559
api_hash = "110d307010e3bb89b7f0c45fc00d013a"
bot_token = "8243889748:AAFObXM7IXrE_b4dvvYQLFeJBFbwiYEB_j0"

app = Client("simple_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Menu button जो @Kingxsellerg प्रोफ़ाइल खोले
    await client.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(
            text="CONTACT INDIAN RESELLER",
            web_app=WebAppInfo(url="https://t.me/Kingxsellerg")
        )
    )
    
    # स्वागत मैसेज (पूरी तरह बोल्ड में)
    caption = (
        "**🙏WELCOME 🥲**\n"
        "**👉YOU WILL GET TG ID TO NUM.**\n"
        "**👉INSTA ID TO NUMBER**\n"
        "**👉NUMBER TO ID**\n"
        "**🎉CONTACT FOR PREMIUM MEMBERSHIP FROM INDIAN RESELLER 👉 @Kingxsellerg 👈**"
    )
    
    await message.reply_text(caption)

app.run()





