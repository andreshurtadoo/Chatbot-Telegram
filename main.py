from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes

TOKEN='6478999042:AAGWbcLy6PmK7rDoj9l5lNiFVkSoGLcEEAM'
username='andreshurtadoo_bot'

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hola! Soy tu bot. Escribe /help para ver los comandos disponibles.')

# Función para el comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "/start - Inicia la interacción con el bot\n"
        "/help - Muestra este mensaje de ayuda\n"
        "/custom - Ejecuta una acción personalizada"
    )
    await update.message.reply_text(help_text)

# Función para el comando /custom
async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Puedes personalizar esta función para hacer algo especial
    await update.message.reply_text('Este es el comando custom. Aquí puedes añadir funcionalidades específicas.')

# Creando la aplicación del bot
application = Application.builder().token(TOKEN).build()

# Agregando los manejadores de comando al bot
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("custom", custom))

# Iniciando el bot
if __name__ == '__main__':
    application.run_polling()