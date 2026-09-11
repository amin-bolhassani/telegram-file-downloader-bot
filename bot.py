import os
import logging
import requests
import telebot
from dotenv import load_dotenv

load_dotenv()


logger= telebot.logger
logger.setLevel(logging.INFO)

DOWNLOAD_DIR = "downloads"
token = os.getenv("file_downloader_token")
if not token:
    raise ValueError("file_downloader_token پیدا نشد!")

bot = telebot.TeleBot(token)

if not os.path.exists("downloads"):
    os.makedirs("downloads")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Give me a valid URL for a file and I will download and upload it here for you."
        )

def download_file(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        stream=True,
        timeout=30,
    )

    response.raise_for_status()

    filename = url.split("/")[-1].split("?")[0]

    if not filename:
        filename = "downloaded_file"

    file_path = os.path.join(DOWNLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    response.close()

    return file_path

@bot.message_handler(func=lambda message: True)
def download_file_url(message):
    logger.info(message.text)
    url = message.text.strip()
    file_path = None
    try:
        file_path = download_file(url)
        with open(file_path, "rb") as file:
            bot.send_document(
                chat_id=message.chat.id,
                reply_to_message_id=message.message_id,
                document=file,
                caption="File downloaded successfully, ENJOY!"
    )
    except Exception as e:
        logger.exception("Download error")
        bot.reply_to(
            message,
            "Download failed"
    )
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

bot.infinity_polling()
