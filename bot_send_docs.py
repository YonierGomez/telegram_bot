import config
import telebot
import time

bot = telebot.TeleBot(config.VAR_TK)

#RESPONDE AL COMANDO /start /ayuda /help
#UTILIZAMOS UN DECORADOR - USAMOS EL METODO message_handler y como param commands y le pasamos una list de comandos
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    """Da la bienvenida"""
    bot.reply_to(message, 'Bienvenid@, este BOT te dará noticias útiles sobre el mundo tecnológico.') #CITA EL MENSAJE ENVIADO AL BOT Y DA UNA RESPUESTA, RECIBE 1 PARAM

#REACCIONA A OTRAS COSAS QUE NO SON COMANDOS, EJ text, audio, document, photo, sticker, video. etc. 
@bot.message_handler(content_types=['text'])
def bot_msj_texto(message):
    """Gestiona los mensajes de texto recibidos"""

    # bot.send_message(message.chat.id, "Suscribete") #ENVIA UN MSJ SIN CITAR, RECIBE 2 PARAM, EL OBJETO MESSAGE TIENE UN METODO
    if message.text.startswith('/'):  #EN EL ATRIBUTO TEXT DEL OBJETO MESSAGE SE ALMACENA LO QUE EL USUARIO ENVIA
        bot.send_message(message.chat.id, 'Comando no disponible') #NO CITA EL MENSAJE ENVIADO RECIBE 2 PARAM EL CHATID - SE OBTIENE DEL OBJETO MESSAGE Y ATRIBUTO CHAT.ID
    else:
        with open('./docs/bot.pdf', 'rb') as mydoc:
            bot.send_document(message.chat.id, mydoc, caption="PDF bot python")
        mydoc.close


if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling() #ESCUCHA O COMPRUEBA SI SE RECIBEN MSJ NUEVOS, TODO SE DETIENE AQUI, 