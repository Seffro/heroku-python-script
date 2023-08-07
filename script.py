import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Créer une fonction qui gère la commande /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenue dans notre boutique de vêtements! Pour voir nos produits, tapez /produits")

# Créer une fonction qui gère la commande /produits
def produits(update, context):
    # Envoyer une liste de produits avec leurs prix
    context.bot.send_message(chat_id=update.effective_chat.id, text="Voici nos produits: \n1. T-shirt - 20€ \n2. Jean - 50€ \n3. Robe - 35€")

# Créer une fonction qui gère les messages de l'utilisateur
def message(update, context):
    # Envoyer une réponse personnalisée à l'utilisateur
    context.bot.send_message(chat_id=update.effective_chat.id, text="Désolé, je ne comprends pas ce que vous voulez dire. Pour voir nos produits, tapez /produits")

# Configurer l'updater et ajouter des gestionnaires de commandes et de messages
updater = Updater(token='VOTRE_TOKEN_TELEGRAM', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('produits', produits))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))

# Démarrer le bot
updater.start_polling()
