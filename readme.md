# 🎮 Steam Hex Discord Bot

Un bot simple de Discord que convierte URLs de perfiles de Steam (ya sean directas o con Vanity URLs) al formato SteamID hexadecimal (`steam:HEXID`). Ideal para whitelists de servidores o sistemas de administración que usen SteamID en formato hexadecimal.

---

## 🚀 Funcionalidades

- ✅ Comando `!steamhex <url>` que convierte cualquier URL válida de Steam en un SteamID hexadecimal.
- 🌐 Soporte tanto para URLs de tipo `profiles` como `id` (vanity).
- 🧠 Lógica simple y directa, fácil de extender.
- 🔐 Usa tu clave personal de la API de Steam.

---

## 📦 Requisitos

- Python 3.8 o superior
- Una cuenta de Discord con permisos para crear bots
- Una cuenta de Steam con acceso a una [Steam Web API Key](https://steamcommunity.com/dev/apikey)

---

## 🔑 Cómo obtener tu Steam Web API Key

1. Iniciá sesión en tu cuenta de Steam.
2. Visitá [https://steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).
3. En el campo `Domain Name`, podés poner `localhost` o tu dominio si tenés uno.
4. Aceptá los términos y hacé clic en "Register".
5. Copiá la clave que te muestra: **esa es tu Steam Web API Key**.

---

## ⚙️ Instalación

1. Cloná este repositorio:

```bash
git clone https://github.com/tuusuario/steam-hex-discord-bot.git
cd steam-hex-discord-bot
```

2. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

3. Creá un archivo `config.py` con tu token del bot de Discord:

```python
# config.py
TOKEN = "TU_TOKEN_DEL_BOT"
```

4. En el código principal (`bot.py`), reemplazá esta línea:

```python
API_KEY = os.getenv('STEAM_API_KEY', 'TU_KEY')
```

🔁 Por defecto, el bot busca tu clave en la variable de entorno `STEAM_API_KEY`, y si no está, usará `'TU_KEY'`.  
Podés dejar tu clave directo en el código o usar una variable de entorno (recomendado):

#### 📁 Opción 1: Editar directamente el código
```python
API_KEY = os.getenv('STEAM_API_KEY', 'Aquí iría tu API KEY')
```

#### 🌱 Opción 2: Usar variable de entorno (más seguro)

En Linux/macOS:
```bash
export STEAM_API_KEY=tu_clave_api
```

En Windows (cmd):
```cmd
set STEAM_API_KEY=tu_clave_api
```

---

## 🧪 Uso

Una vez que el bot esté corriendo, podés usar el comando:

```
!steamhex <url_de_steam>
```

📌 Ejemplo:

```
!steamhex https://steamcommunity.com/id/gabenvn
```

📥 Respuesta esperada:

```
SteamID hexadecimal: 11000010b9e4ef3
```

---

## 🛡️ Seguridad

- **No subas `config.py` ni tu API key al repositorio.**
- Usá variables de entorno siempre que sea posible.

---

## 📁 Estructura de archivos

```
.
├── bot.py              # Código principal del bot
├── config.py           # Contiene tu TOKEN
├── LICENSE             # Licencia MIT
├── README.md           # Este archivo
└── requirements.txt    # Dependencias

```

---

## 👤 Autor

Desarrollado por [**Bautilongo**](https://github.com/Bautilongo)

---

## 📜 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).  
Podés copiar, modificar y usar libremente el código — incluso comercialmente — siempre que se conserve el aviso original.
