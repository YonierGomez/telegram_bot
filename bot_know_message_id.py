import config
import telebot

bot = telebot.TeleBot(config.VAR_TK)


# @bot.message_handler(content_types=['text'])
# def bot_msj_texto(message):
#     """Gestiona los mensajes de texto recibidos"""

#     global sise
#     sise = message.chat.id
#     bot.send_message(message.chat.id, 'Hola') 
#     print(sise)

@bot.message_handler(func=lambda message: True)
def get_chat_id(message):
    chat_id = message.chat.id
    print(f'El Chat ID del grupo es: {chat_id}')

if __name__ == '__main__':

    print('Iniciando bot')
    bot.infinity_polling()
