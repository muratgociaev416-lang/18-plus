import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

MEDIA_PATH = "media"

CATEGORIES = {
    "breasts": "🔥 Сиськи",
    "ass": "🍑 Жопы",
    "blowjob": "😮 Минет",
    "hardcore": "💦 Хардкор",
    "videos": "🎥 Видео"
}
