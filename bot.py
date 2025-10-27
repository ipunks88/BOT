import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! 🤖 Bot aktif 24 jam di GitHub Actions ✅\nKetik /run untuk menjalankan fix_merah.py")

async def run_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Menjalankan fix_merah.py ...")
    try:
        result = subprocess.run(["python3", "fix_merah.py"], capture_output=True, text=True)
        output = result.stdout or result.stderr or "✅ Script selesai tanpa output"
        if len(output) > 4000:
            output = output[:4000] + "\n\n(Output terpotong)"
        await update.message.reply_text(f"📜 Output:\n\n{output}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("run", run_script))

print("🤖 Bot Telegram aktif di GitHub Actions...")
app.run_polling()
