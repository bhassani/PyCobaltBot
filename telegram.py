#https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/

#install via pip install python-telegram-bot
from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 

updater = Updater("your_own_API_Token got from BotFather", 
                  use_context=True) 

def start(update: Update, context: CallbackContext): 
    update.message.reply_text( 
        "Hello, Welcome to the CobaltBot.  Please write\ 
        /help to see the commands available.") 
  
def help(update: Update, context: CallbackContext):
  update.message.reply_text("""Available Commands :- 
    /help - To get the help menu
    /whoami - who get information about cobaltbot
    /search - To search the system for cobalt strike
    /ram - To search RAM for cobalt strike""") 
  
def whoami(update: Update, context: CallbackContext):
  update.message.reply_text("I am CobaltBot") 

def search(update: Update, context: CallbackContext): 
  update.message.reply_text("searching the system for cobalt strike") 

def ram(update: Update, context: CallbackContext): 
  update.message.reply_text("searching RAM for cobalt strike")
  
def unknown(update: Update, context: CallbackContext): 
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text) 
def unknown_text(update: Update, context: CallbackContext): 
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text) 

updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('whoami', whoami)) 
updater.dispatcher.add_handler(CommandHandler('start', start)) 
updater.dispatcher.add_handler(CommandHandler('search', search))
updater.dispatcher.add_handler(CommandHandler('ram', ram))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown)) 
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands 
#Filters out unknown messages. 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 
updater.start_polling() 
