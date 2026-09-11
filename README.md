# Telegram File Downloader Bot

A lightweight Telegram bot built with Python that allows users to download files from direct URLs and receive them directly in Telegram.

The project was developed to practice working with HTTP requests, file handling, environment variables, error handling, logging, and Telegram bot development using Python.

---

## Features

* Download files from direct URLs
* Send downloaded files directly to Telegram
* Stream files to reduce memory usage
* Automatically delete temporary files after sending
* Environment variable support for secure bot configuration
* Basic error handling and logging
* Simple and maintainable project structure

---

## Technologies Used

* Python
* pyTelegramBotAPI
* Requests
* python-dotenv

---

## Project Structure

```text
telegram-file-downloader-bot/
│
├── bot.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amin-bolhassani/telegram-file-downloader-bot.git
```

Move to the project directory:

```bash
cd telegram-file-downloader-bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
file_downloader_token=your_telegram_bot_token
```

Replace `your_telegram_bot_token` with your actual Telegram bot token.

**Never upload your `.env` file or expose your bot token publicly.**

---

## Usage

Run the bot with:

```bash
python bot.py
```

Open the bot in Telegram and send:

```text
/start
```

Then send a direct URL to a file.

For example:

```text
https://example.com/file.zip
```

The bot will download the file and send it back to you through Telegram.

---

## How It Works

```text
User
  ↓
Sends a file URL
  ↓
Bot receives the URL
  ↓
Requests downloads the file
  ↓
File is temporarily stored
  ↓
Bot uploads the file to Telegram
  ↓
Temporary file is deleted
```

---

## Error Handling

The bot handles common errors during the download and upload process, including:

* Connection errors
* Request timeouts
* Invalid responses
* Download failures
* Unexpected exceptions

Errors are also logged using Python logging.

---

## Limitations

This project is designed primarily for **direct file URLs**.

Some websites may not work because they:

* Require authentication
* Use temporary download links
* Require cookies or special headers
* Redirect to web pages instead of files
* Block automated requests
* Use unsupported server configurations

---

## Future Improvements

Possible future improvements include:

* File size limits
* Better URL validation
* Improved filename handling
* Download progress updates
* Support for additional download services
* More advanced error handling
* Security improvements for public deployment
* Docker support

---

## What I Learned

Building this project helped me practice:

* Telegram bot development
* HTTP requests with `requests`
* Streaming file downloads
* File handling in Python
* Environment variables
* `.env` configuration
* Exception handling
* Logging
* Temporary file management

---

## License

This project is licensed under the MIT License.
