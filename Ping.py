import os
# import requests
from pythonping import ping
import logging
from telegram.ext import Updater, CommandHandler

# Configura el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configura los detalles del bot de Telegram
telegram_token = [INSERTAR_TOKEN_DE_TELEGRAM]

# Función para iniciar el bot
def start(update, context):
    update.message.reply_text(
        '¡Hola! Soy un bot que verifica el estado de conexión de dispositivos.\n'
        'Usa /ping para verificar dispositivos generales.\n'
        'Usa /nuc para verificar dispositivos NUC.'
    )

# Función para manejar el comando /ping
def ping_command(update, context):
    ip_list = [
        # Modificar INSERTAR_IP_DISPOSITIVO por los IP que necesitamos verificar
        'INSERTAR_IP_DISPOSITIVO','INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO',
        'INSERTAR_IP_DISPOSITIVO','INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO'
    ]
    ip_name = [
        # Modificar INSERTAR_NOMBRE_DISP por los NOMBBRES de los dispositivos que necesitamos verificar
        'INSERTAR_NOMBRE_DISP','INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP',
        'INSERTAR_NOMBRE_DISP','INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP'
    ]
    
    for idx, ip_address in enumerate(ip_list):
        response = ping(ip_address, count=1)
        if response.success():
            message = f"✅ Ping exitoso a {ip_name[idx]}: {ip_address}"
        else:
            message = f"❌ No se puede hacer ping a {ip_name[idx]}: {ip_address}"
        update.message.reply_text(message)

# Función para manejar el comando /nuc
def nuc_command(update, context):
    ip_list = [
        'INSERTAR_IP_DISPOSITIVO','INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO',
        'INSERTAR_IP_DISPOSITIVO','INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO', 'INSERTAR_IP_DISPOSITIVO'
    ]
    ip_name = [
        'INSERTAR_NOMBRE_DISP','INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP',
        'INSERTAR_NOMBRE_DISP','INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP', 'INSERTAR_NOMBRE_DISP'
    ]
    
    for idx, ip_address in enumerate(ip_list):
        response = ping(ip_address, count=1)
        if response.success():
            message = f"✅ Ping exitoso a {ip_name[idx]}: {ip_address}"
        else:
            message = f"❌ No se puede hacer ping a {ip_name[idx]}: {ip_address}"
        update.message.reply_text(message)

# Función principal
def main():
    # Crea el actualizador y el despachador para el bot de Telegram
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    
    # Agrega controladores de comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ping", ping_command))
    dispatcher.add_handler(CommandHandler("nuc", nuc_command))
    
    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()