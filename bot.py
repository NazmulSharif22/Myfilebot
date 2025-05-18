from pyrogram import Client, filters
from pyrogram.types import Message
import json, string, random
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("file_store_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

try:
    with open("database.json", "r") as f:
        file_db = json.load(f)
except:
    file_db = {}

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.on_message(filters.document | filters.video | filters.audio & filters.private)
async def save_file(client, message: Message):
    file_id = generate_id()
    file_db[file_id] = message.document.file_id if message.document else (
        message.video.file_id if message.video else message.audio.file_id
    )
    with open("database.json", "w") as f:
        json.dump(file_db, f)

    link = f"https://t.me/{(await app.get_me()).username}?start={file_id}"
    await message.reply(f"✅ ফাইল সংরক্ষিত হয়েছে!\n🔗 লিংক: {link}")

@app.on_message(filters.command("start"))
async def send_file(client, message: Message):
    args = message.text.split()
    if len(args) == 2:
        file_id = args[1]
        if file_id in file_db:
            await message.reply_document(file_db[file_id])
        else:
            await message.reply("❌ এই ফাইল পাওয়া যায়নি।")
    else:
        await message.reply("👋 হ্যালো! ফাইল পাঠাও, আমি লিংক দিব।")

app.run()
