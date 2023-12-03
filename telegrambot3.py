from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import subprocess
import os
import shlex
import threading

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
TOKEN = ''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Use /echo to echo a message.')

def echo(update: Update, context: CallbackContext) -> None:
    # Parse additional arguments
    args = context.args
    if not args:
        update.message.reply_text('Please provide a message to echo.')
    else:
        message = ' '.join(args)
        update.message.reply_text(f'Echo: {message}')

def youtube_download_func(url):
    youtube_program = f"yt-dlp {url}"
    cmds = shlex.split(youtube_program)
    p = subprocess.Popen(cmds, start_new_session=True)

def youtube(update: Update, context: CallbackContext) -> None:
    # Parse additional arguments
    args = context.args
    if not args:
        update.message.reply_text('Please provide a youtube link to download')
    else:
        message = ' '.join(args)
        update.message.reply_text(f'Downloading youtube video: {message}')
        youtube_thread = threading.Thread(target=youtube_download_func, args=(message,))
        youtube_thread.start()

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("echo", echo, pass_args=True))
    dp.add_handler(CommandHandler("youtube", youtube, pass_args=True))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
