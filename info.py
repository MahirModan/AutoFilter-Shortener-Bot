import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28445434'))
API_HASH = environ.get('API_HASH', '8cc2507d26a86d506a65e9af474e2a0f')
BOT_TOKEN = environ.get('BOT_TOKEN', "5855639065:AAHf6quh3zXclWffWP_G69muH56Yk_b9Us0")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/2c69dd2abd34484066cd6.jpg https://telegra.ph/file/119e2efb3eefb1ba09c9c.jpg https://telegra.ph/file/43a2894ded0adce5cdfb2.jpg https://telegra.ph/file/39cf8f9582e38f6b6c6d0.jpg https://telegra.ph/file/5ff0a3e2c57f537b5578b.jpg https://telegra.ph/file/cac93a49a9f46a48e9407.jpg https://telegra.ph/file/70186bd6a4e6a340e6d2d.jpg https://telegra.ph/file/6e4f031d926f7700620de.jpg https://telegra.ph/file/8b80c7415c91dd0ab8ddd.jpg https://telegra.ph/file/e23621e56620a2fce381c.jpg https://telegra.ph/file/10dc412061587e134724c.jpg https://telegra.ph/file/7f615cb92824621c927d1.jpg https://telegra.ph/file/2094686f491d441abcf70.jpg https://telegra.ph/file/c5eb5ba06b412053a330e.jpg https://telegra.ph/file/b157c91422be6f65e1c97.jpg https://telegra.ph/file/37aee885163eff9d6e8f0.jpg https://telegra.ph/file/7d1b551369902a01aaf2c.jpg https://telegra.ph/file/a2a851966c6f87cbb32f0.jpg https://telegra.ph/file/4597762206ab870ac0512.jpg https://telegra.ph/file/147a1e9dc050027b7f14c.jpg https://telegra.ph/file/33d5224a798e9c8c275c7.jpg https://telegra.ph/file/336b9c6bd6783794c452f.jpg https://telegra.ph/file/f120059caa49cad4aa4d1.jpg https://telegra.ph/file/b74ec255355e7648b50ed.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1366310017 1315219809').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001754951124').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://AnimeStore:AnimeStore@cluster0.8ihiyyk.mongodb.net/AnimeStore?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "AnimeStore")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001796592159'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'HenTaii_Store')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [CinemaRoom](https://t.me/HenTaii_Store)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [HAnime Store](https://t.me/HenTaii_Store)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @CinemaRoom")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001879875542')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'api.shareus.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'eL75TMbrd3Sh5LRZ4DOOIjZtRpR2')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/your.telegram.link"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Subscribe"
CAPTION_BUTTON_URL = "https://t.me/your.telegram.link"

   # Auto Delete For Bot Sending Files #
