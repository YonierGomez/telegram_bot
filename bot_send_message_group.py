import config
import telebot
import threading

bot = telebot.TeleBot(config.VAR_TK)

def send_msj_texto():
    """Envía un msj al grupo"""

    bot.send_message(config.VAR_GROUP_CHAT_ID, 'Saludos al grupo') #NO CITA EL MENSAJE ENVIADO RECIBE 2 PARAM EL CHATID - SE OBTIENE DEL OBJETO MESSAGE Y ATRIBUTO CHAT.ID

def listen():
    """Bucle infinito"""
    bot.infinity_polling() #ESCUCHA O COMPRUEBA SI SE RECIBEN MSJ NUEVOS, TODO SE DETIENE AQUI, 
    

if __name__ == '__main__':
    print('Iniciando bot')
    send_msj_texto()
    hilo_bot = threading.Thread(listen())
    hilo_bot.start()
    