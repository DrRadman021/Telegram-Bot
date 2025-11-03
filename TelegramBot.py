from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Someone sent /start")
    await update.message.reply_text("سلام! ربات فعاله 🤖")

app = ApplicationBuilder().token("8595286301:AAFF0kuUWIDlzz3O7JUhJ8eQbdLfJHGg-Mg").build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
