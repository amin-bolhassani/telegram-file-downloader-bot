# Iran Market Telegram Bot

A Telegram bot built with Python that provides real-time gold and currency prices using the BRS API. The bot allows users to retrieve market information directly from Telegram and receive fast, accurate, and well-formatted responses.

This project was developed to practice working with APIs, asynchronous programming, error handling, environment variables, and Telegram bot development.

---

## Features

* Real-time gold price updates
* Real-time currency exchange rates
* Telegram bot integration
* API communication using HTTP requests
* Error handling for connection and timeout exceptions
* Secure storage of sensitive information using environment variables
* Clean and maintainable code structure

---

## Supported Data

The bot can retrieve information such as:

* Gold prices
* Foreign exchange rates
* Market symbols
* Units and formatted prices

---

## Technologies Used

* Python
* Python Telegram Bot
* Requests
* Python Dotenv
* BRS API

---

## Project Structure

```text
iran-market-telegram-bot/
│
├── bot.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amin-bolhassani/iran-market-telegram-bot.git
```

Move to the project directory:

```bash
cd iran-market-telegram-bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add the following variables:

```text
BOT_TOKEN=your_telegram_bot_token
BRSAPI_KEY=your_api_key
```

---

## Usage

Run the project with the following command:

```bash
python bot.py
```

---

## Error Handling

The application handles several common situations, including:

* Connection errors
* Request timeouts
* Missing data
* Invalid symbols
* Unexpected exceptions

---

## Future Improvements

* Support for cryptocurrencies
* Historical price analysis
* Price alerts and notifications
* Database integration
* Logging support
* Docker support

---

## License

This project is licensed under the MIT License.
