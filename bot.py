from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', #Запись лога о работе бота
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():

    updater = Updater("548253987:AAFZTH-rmT7xQH6LQhUPYEd32-XvGWa9AwA") # Персональный токен
    
    def greet_user(bot, update):
        text = 'Вызван /start'
        print(text)
        update.message.reply_text(text)

    def talk_to_me(bot, update):
        user_text = update.message.text 
        print(user_text)
        update.message.reply_text(user_text)



    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) # Вызов greet_user командой start
    dp.add_handler(MessageHandler(Filters.text,talk_to_me)) #В случае получения текстового сообщения вызывает talk_to_me



    updater.start_polling() # Подключение
    updater.idle()          # бота

main()