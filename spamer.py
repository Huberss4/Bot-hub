#!/usr/bin/python
import os
from datetime import datetime
from time import sleep
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Configuración de API y variables de telegram
api_id = '7639109623'  
api_hash = 'AAHPai4qAnTymaC2RtEH2oG9mq6DHYhw1mA'  
grupo_origen_id = -1002471895760        # ID de tu grupo de origen
tu_numero_telefono = '+51910740363'  # Tu número de teléfono asociado a la cuenta de Telegram
# Define la cantidad de segundos entre cada envío de mensaje
intervalo_entre_envios = 1  # Por ejemplo, 1 segundo de pausa entre cada mensaje

p = '\x1b[0m'
m = '\x1b[91m'
n = '\x1b[40m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

def logo():
    os.system('clear')
    auth = f"{h}  Author : {k}./kitsune"
    return f'''
{n}╭━┳━╭━╭━╮{b}╮╲╲╲╲╲╲{h}╔═╗╔═╗╔═╗╔╦╗
{n}┃┈┈┈┣▅╋▅┫┃{b}╲╲╲╲╲╲{h}╚═╗╠═╝╠═╣║║║
{n}┃┈┃┈╰━╰━━━━━━╮{b}╲╲{h}╚═╝╩  ╩ ╩╩ ╩
{n}╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣{b}╲{h}╔═╗╔╦╗╔═╗
{n}╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉{b}╲{h}╚═╗║║║╚═╗
{n}╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤{b}╲{h}╚═╝╩ ╩╚═╝
{n}╲┃┈┈┈┈╭━┳━━━━╯{b}╲╲{h}╔╦╗╔═ ╔  ╔═
{n}╲┣━━━━━━┫{b}╲╲╲╲╲╲╲{h} ║ ║═ ║  ║═
{n}╲┃┈┈┈┈┈┈┃{b}╲╲╲╲╲╲╲{h} ╩ ╚═ ╚═ ╚═ 
{p}{auth}{p}
'''

def iniciar_sesion():
    print(f"{h}BIENVENIDO A BOT SPAM v3.2{p}")  # Mensaje de bienvenida
    client = TelegramClient('session_name', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(tu_numero_telefono)
            client.sign_in(tu_numero_telefono, input(f"{h}Ingresa el código que has recibido: {p}"))
        except SessionPasswordNeededError:
            client.sign_in(password=input(f"{h}Ingresa la contraseña de la cuenta: {p}"))
    return client

def reenviar_mensajes(client):
    try:
        print(f"{h}Obteniendo mensajes 📚👉📱{p}")
        messages = client.iter_messages(grupo_origen_id)
        chats = client.get_dialogs()

        last_message_time = datetime.now()  # Guardar la hora del último mensaje enviado
        for message in messages:
            if message.message:
                for chat in chats:
                    if chat.is_group and chat.id != grupo_origen_id:
                        try:
                            client.forward_messages(chat.id, messages=[message])
                            print(f"{h}[*] 📲 {chat.title}:{k} {message.id}{p}")
                        except SessionPasswordNeededError:
                            # Si se requiere contraseña, intenta iniciar sesión nuevamente
                            client = iniciar_sesion()
                            client.forward_messages(chat.id, messages=[message])
                            print(f"{h}[*] 📲 {chat.title}: {message.id}{p}")
                        except Exception as e:
                            print(f"{m}Error al reenviar mensaje: {e}{p}")
                # Introduce una pausa antes de enviar el siguiente mensaje
                sleep(intervalo_entre_envios)

    except Exception as ex:
        print(f"{m}❌❌❌ Error general: {ex}{p}")


    print(logo())  # Llamada a la función logo() al inicio del script
    client = iniciar_sesion()
    
    while True:
        try:
            reenviar_mensajes(client)
            for i in range(15, 0, -1):  # Conteo regresivo de 15 minutos
                print(f"{h}[֍]  Esperar ⏳ {k}{i}{p} {h}minutos para reenviar mensajes{p}", end="\r")
                sleep(60)  # Esperar 1 minuto
        except Exception as ex:
            print(f"{m}Error general:{p} {ex}")
