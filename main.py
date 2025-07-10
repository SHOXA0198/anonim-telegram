from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

BOT_TOKEN = '7575139637:AAF6X9k8scoxL2MqdBD-91rBNfKDGfKEf_8'
ADMIN_ID = 6415949804

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📨 Shohjahonga xabaringizni yozing.")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text
        sender = update.message.from_user
        sender_info = f"👤 From: @{sender.username}" if sender.username else f"👤 From: {sender.first_name}"
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Yangi xabar:\n\n{text}\n\n{sender_info}"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_admin))
    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()