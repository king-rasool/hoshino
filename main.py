import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# کلیدهای API
openai.api_key = 'a'
TELEGRAM_TOKEN = 'a'

async def start(update: Update, context):
    await update.message.reply_text("سلام! من هوشینو هستم، از من هر سوالی داری بپرس.")

async def handle_message(update: Update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    await update.message.reply_text(answer)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
