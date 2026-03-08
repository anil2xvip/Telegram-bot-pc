import telebot
from telebot import types

TOKEN = "8796751372:AAFMqQmS2Ec2dhkE76EQrIOMFgWWjuZD8xs"
CHANNEL = "@primepc1"

bot = telebot.TeleBot(TOKEN)


def check_join(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()

    main = types.InlineKeyboardButton("📢 Main Channel", url="https://t.me/primepc1")
    files = types.InlineKeyboardButton("📂 Files Channel", url="https://t.me/primepcfiles")
    youtube = types.InlineKeyboardButton("▶️ YouTube", url="https://youtube.com/primepcff")
    insta = types.InlineKeyboardButton("📸 Instagram", url="https://instagram.com/anil2x")
    check = types.InlineKeyboardButton("✅ Joined / Verify", callback_data="verify")

    markup.row(main)
    markup.row(files)
    markup.row(youtube, insta)
    markup.row(check)

    bot.send_message(
        message.chat.id,
        "⚠️ Bot use karne ke liye pehle main channel join karo.\n\nJoin karne ke baad 'Joined / Verify' dabao.",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):

    if check_join(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id," OWNER @primepc2\n\n♥😎💀")
    else:
        bot.answer_callback_query(call.id,"❌ Pehle main channel join karo!")


bot.infinity_polling()