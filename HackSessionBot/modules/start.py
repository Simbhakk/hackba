from pyrogram import filters, Client
from HackSessionBot import app , START_PIC , CHANNEL
from HackSessionBot.Helpers.data import PM_TEXT,PM_BUTTON,HACK_MODS,HACK_TEXT
from pyrogram.types import CallbackQuery
from HackSessionBot.Helpers.steve import handle_force_subscribe

@app.on_message(filters.command("start") & filters.private)
async def _start(_, message):
    if CHANNEL:
      fsub = await handle_force_subscribe(_, message)
      if fsub == 400:
        return
    user = message.from_user.mention
    bot = (await _.get_me()).mention 
    await message.reply_photo(
       photo = START_PIC,
       caption = PM_TEXT.format(user, bot),
       reply_markup = PM_BUTTON) 


@app.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    if CHANNEL:
      fsub = await handle_force_subscribe(_, message)
      if fsub == 400:
        return
    await message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


