import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# کلیدهای API
openai.api_key = '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'
TELEGRAM_TOKEN = '7467637126:AAG_PP7dd4Xtqzut-gmmf1pwp-DuuGg71-M'

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
