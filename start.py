from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = """أهلاً وسهلاً! 🔥

أنا مساعدك الشخصي في متجر flame للملابس!

أقدر أساعدك في:
• الإجابة على الأسئلة الشائعة عن المتجر
• معلومات عن التوصيل والأسعار
• شروط الإرجاع والتبديل
• مواعيد العمل وطرق الدفع
الاستفسار عن المنتج وسعره.

ابعتلي أي سؤال وهرد عليك فوراً! 😊"""

    await update.message.reply_text(welcome_message)