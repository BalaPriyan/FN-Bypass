from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from FZBypass.plugins.script import *

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    text = script.HELP_TXT.format(update.from_user.mention)
    keyboard = InlineKeyboardMarkup([ 
        [InlineKeyboardButton('Gdrive', callback_data='gdrive'),
         InlineKeyboardButton('shorten', callback_data='shorten')],
        [InlineKeyboardButton('scrape', callback_data='scrape'),
         InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    await message.reply(text=text, reply_markup=keyboard)

@Client.on_callback_query(filters.regex('help'))
async def help_callback(bot, update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keyboard = InlineKeyboardMarkup([ 
        [InlineKeyboardButton('Gdrive', callback_data='gdrive'),
         InlineKeyboardButton('shorten', callback_data='shorten')],
        [InlineKeyboardButton('scrape', callback_data='scrape'),
         InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    await update.message.edit(text=text, reply_markup=keyboard)

@Client.on_callback_query(filters.regex('scrape'))
async def scrape(bot,update):
    text = script.SCRAPE_TXT
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back",callback_data = "help")]])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('shorten'))
async def shorten(bot,update):
    text = script.SHORTENER_TXT
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back",callback_data = "help")]])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('gdrive'))
async def gdrive(bot,update):
    text = script.GDRIVE_TXT
    keybord = InlineKeyboardMarkup([  [InlineKeyboardButton("🔙 Back",callback_data = "help")]])
    await update.message.edit(text = text,reply_markup = keybord)
