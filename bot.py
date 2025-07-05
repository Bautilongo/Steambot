# Importamos las librerías necesarias
import discord
from discord.ext import commands
import os
import re
import requests
from typing import Optional
from config import TOKEN  # Token del bot importado desde un archivo externo para mayor seguridad

# Prefijo para los comandos del bot (ej: !comando)
PREFIX = "!"

# Clave de la API de Steam, se intenta obtener desde variables de entorno o se usa una por defecto
API_KEY = os.getenv('STEAM_API_KEY', 'TU CLAVE DE API AQUÍ SI NO ESTÁ EN VARIABLES DE ENTORNO')

# Configuración de los permisos que el bot va a manejar
intents = discord.Intents.default()
intents.messages = True               # Permite leer mensajes de texto
intents.guilds = True                 # Permite ver servidores (guilds)
intents.message_content = True       # Necesario para leer el contenido del mensaje
intents.voice_states = True          # Permite detectar cambios en canales de voz
intents.members = True               # Permite ver los miembros de los servidores

# Creación del bot con los intents definidos y sin comando de ayuda por defecto
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Evento que se ejecuta cuando el bot se conecta correctamente a Discord
@bot.event
async def on_ready():
    print(f"Conectado como {bot.user} (ID: {bot.user.id})")
    print("Bot listo para funcionar.")    

### Comando de ejemplo para probar la funcion steam_url_to_hex ###
# El comando sería usado: !steamhex <URL de Steam profile> y 
# devolvería el SteamId hexadecimal correspondiente a la URL
@bot.command()
async def steamhex(ctx, *, steam_url: str):
    hex_id = steam_url_to_hex(steam_url)
    if hex_id:
        await ctx.send(f"SteamID hexadecimal: `{hex_id}`")
    else:
        await ctx.send("No se pudo convertir la URL de Steam a SteamID hexadecimal.")

# Convierte una URL de perfil de Steam (ya sea por ID o Vanity URL) a SteamID hexadecimal
def steam_url_to_hex(steam_url: str) -> Optional[str]:
    steam_url = steam_url.strip().split('?')[0].rstrip('/')
    match = re.search(r'https:\/\/steamcommunity\.com\/(profiles|id)\/([\w\d]+)', steam_url)
    if not match:
        return None
    url_type, identifier = match.groups()
    if url_type == "profiles":
        return convert_steam_id_to_hex(identifier)  # Directamente es un SteamID64
    elif url_type == "id":
        steam_id = get_steam_id_from_vanity(identifier)  # Es un Vanity URL y se debe resolver
        return convert_steam_id_to_hex(steam_id) if steam_id else None
    return None

# Convierte un SteamID64 a formato hexadecimal
def convert_steam_id_to_hex(steam_id: str) -> Optional[str]:
    digits = re.findall(r'\d+', steam_id)
    return hex(int(digits[0]))[2:].lower() if digits else None

# Llama a la API de Steam para convertir un vanity URL (nombre personalizado) en SteamID64
def get_steam_id_from_vanity(vanity_url: str) -> Optional[str]:
    url = f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_KEY}&vanityurl={vanity_url}'
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('response', {}).get('steamid') if data.get('response', {}).get('success') == 1 else None
    except requests.RequestException as e:
        print(f"Error al obtener Steam ID: {e}")
        return None

# Corre el bot con el token proporcionado
bot.run(TOKEN)
