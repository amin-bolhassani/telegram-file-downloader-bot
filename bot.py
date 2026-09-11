import requests
from dotenv import load_dotenv
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BRSAPI_KEY = os.getenv('BRSAPI_KEY')

COIN_NAMES_FA = {
    "bitcoin": "بیت‌کوین",
    "ethereum": "اتریوم",
    "tether": "تتر",
    "binancecoin": "بایننس کوین",
    "solana": "سولانا",
    "ripple": "ریپل",
    "cardano": "کاردانو",
    "dogecoin": "دوج‌کوین",
    "avalanche-2": "اولانچ",
    "polkadot": "پولکادات"
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام! برای دیدن قیمت‌ها از دستور /price استفاده کن.')


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("بیت‌کوین", callback_data="crypto_bitcoin")],
        [InlineKeyboardButton("اتریوم", callback_data="crypto_ethereum")],
        [InlineKeyboardButton("تتر", callback_data="crypto_tether")],
        [InlineKeyboardButton("بایننس کوین", callback_data="crypto_binancecoin")],
        [InlineKeyboardButton("سولانا", callback_data="crypto_solana")],
        [InlineKeyboardButton("ریپل", callback_data="crypto_ripple")],
        [InlineKeyboardButton("کاردانو", callback_data="crypto_cardano")],
        [InlineKeyboardButton("دوج‌کوین", callback_data="crypto_dogecoin")],
        [InlineKeyboardButton("اولانچ", callback_data="crypto_avalanche-2")],
        [InlineKeyboardButton("پولکادات", callback_data="crypto_polkadot")],
        [InlineKeyboardButton("طلای ۱۸ عیار", callback_data="market_IR_GOLD_18K")],
        [InlineKeyboardButton("طلای ۲۴ عیار", callback_data="market_IR_GOLD_24K")],
        [InlineKeyboardButton("سکه امامی", callback_data="market_IR_COIN_EMAMI")],
        [InlineKeyboardButton("نیم سکه", callback_data="market_IR_COIN_HALF")],
        [InlineKeyboardButton("ربع سکه", callback_data="market_IR_COIN_QUARTER")],
        [InlineKeyboardButton("دلار", callback_data="market_USD")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("یکی از موارد زیر رو انتخاب کن:", reply_markup=reply_markup)


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    category, item = data.split("_", 1)

    if category == "crypto":
        await handle_crypto(query, item)
    elif category == "market":
        await handle_iran_market(query, item)


async def handle_crypto(query, coin_name):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if coin_name not in data:
            await query.edit_message_text("متأسفانه قیمت این ارز پیدا نشد.")
            return

        coin_price = data[coin_name]['usd']
        persian_name = COIN_NAMES_FA.get(coin_name, coin_name)
        await query.edit_message_text(f"قیمت {persian_name}: ${coin_price}")

    except requests.exceptions.Timeout:
        await query.edit_message_text("درخواست بیش از حد طول کشید. لطفاً دوباره امتحان کن.")
    except requests.exceptions.ConnectionError:
        await query.edit_message_text("اتصال به سرویس قیمت برقرار نشد. لطفاً دوباره امتحان کن.")


async def handle_iran_market(query, symbol):
    url = f"https://Api.BrsApi.ir/Market/Gold_Currency.php?key={BRSAPI_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        item = None
        for entry in data['gold'] + data['currency']:
            if entry['symbol'] == symbol:
                item = entry
                break

        if item is None:
            await query.edit_message_text("قیمت این مورد پیدا نشد.")
            return

        item_price = item['price']
        item_name = item['name']
        item_unit = item['unit']
        await query.edit_message_text(f"{item_name}: {item_price:,} {item_unit}")

    except requests.exceptions.Timeout:
        await query.edit_message_text("درخواست بیش از حد طول کشید. لطفاً دوباره امتحان کن.")
    except requests.exceptions.ConnectionError:
        await query.edit_message_text("اتصال برقرار نشد. لطفاً دوباره امتحان کن.")

async def check_prices(context: ContextTypes.DEFAULT_TYPE):
    print("در حال چک کردن قیمت‌ها...")

app = (
    Application.builder()
    .token(BOT_TOKEN)
    .connect_timeout(30)
    .read_timeout(30)
    .build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CallbackQueryHandler(button_click))

app.job_queue.run_repeating(check_prices, interval=30, first=5)

print("Bot is running...")
app.run_polling()