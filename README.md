# PingTelegram - Verificador de Conectividad por Telegram

Este bot de Telegram permite verificar el estado de conexión (ping) de una lista de dispositivos conectados a la red. Es especialmente útil para administradores de sistemas o personal de IT que necesite monitorear rápidamente la conectividad de estaciones de trabajo, servidores o equipos NUC específicos.

## 🚀 Características

- Verifica conectividad a múltiples IPs con un solo comando.
- Diferenciación entre dispositivos generales y equipos NUC.
- Respuestas claras y en tiempo real a través de un bot de Telegram.
- Fácil de desplegar y configurar.

## 🛠️ Requisitos

- Python 3.6 o superior
- Las siguientes dependencias de Python:
  - `pythonping`
  - `python-telegram-bot`

Puedes instalar las dependencias con:

```bash
pip install pythonping python-telegram-bot
```

## 📦 Instalación
Clona este repositorio:
```bash
git clone https://github.com/speinador/PingBot.git
```
```bash
cd PingBot
```

Edita el archivo Ping.py y reemplaza el valor de telegram_token con tu token de bot de Telegram.

Ejecuta el bot:
```bash
python Ping.py
```

## 💬 Comandos disponibles
**/start**: Muestra un mensaje de bienvenida con las instrucciones.

**/ping**: Verifica el estado de dispositivos generales predefinidos en la red.

**/nuc**: Verifica el estado de los equipos NUC específicos.

## 📋 Listado de Dispositivos
El archivo contiene dos listas con IPs y nombres descriptivos:

- **Lista general:** servidores, dispositivos de red. etc.
- **Lista NUC:** terminales de usuario, equipos compactos, etc.

## 🔐 Seguridad
Ten en cuenta que el token de tu bot de Telegram debe mantenerse en secreto. Se recomienda cargarlo desde una variable de entorno o un archivo .env en lugar de dejarlo en el código fuente.
