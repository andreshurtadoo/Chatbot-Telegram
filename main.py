from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

TOKEN='6478999042:AAGWbcLy6PmK7rDoj9l5lNiFVkSoGLcEEAM'

# Definiendo los estados
NAME, ADVICE = range(2)

# Función para el comando /start
# Función para el comando /start que inicia la conversación
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        'Hola! ¿Cómo te llamas?',
        reply_markup=ForceReply(selective=True),
    )
    return NAME

# Función para manejar el estado NAME
async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    name = update.message.text
    context.user_data['name'] = name  # Guardamos el nombre en los datos del usuario
    await update.message.reply_text(f'Encantado de conocerte, {name}. ¿Quieres algún consejo? (sí/no)')
    return ADVICE

# Función para manejar el estado ADVICE
async def receive_advice_decision(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    decision = update.message.text.lower()
    if decision == 'sí' or decision == 'si':
        await update.message.reply_text('Aquí va un consejo: siempre toma un momento para relajarte.')
    else:
        await update.message.reply_text('Está bien, no hay problema. Si necesitas algo más, sólo pregúntame!')
    return ConversationHandler.END  # Esto termina la conversación

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

# Función para cancelar la conversación
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Conversación cancelada.')
    return ConversationHandler.END

# Creando la aplicación del bot
application = Application.builder().token(TOKEN).build()

# Agregando los manejadores de comando al bot
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("custom", custom))

# Iniciando el bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Definiendo el handler de la conversación
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            ADVICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_advice_decision)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
