class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5391039247"
    sudo_users = "5391039247", "1486727193", "1102584877", "7052570049", "6391328971", "7100617938", "7150190248", "5165804914", "7027685257", "6975280846"
    GROUP_ID = -1002102504910
    TOKEN = "6913009476:AAHPWb-EEcONeCglOREvP0jVJ48ibmYWwDU"
    mongo_url = "mongodb+srv://dripkosmic:Zacky4148@supremedomain.tjbs13p.mongodb.net/?retryWrites=true&w=majority&appName=Supremedomain"
    PHOTO_URL = ["https://te.legra.ph/file/6f9313f01e1742cc561ed.jpg", "https://te.legra.ph/file/bf8bb65383c6aaf437daf.jpg", "https://te.legra.ph/file/5a6922a3e94ec102cff38.jpg", "https://te.legra.ph/file/539101180b5a9e53e3c71.jpg"]
    SUPPORT_CHAT = "anime_chat_anicade"
    UPDATE_CHAT = "anime_chat_anicade"
    BOT_USERNAME = "guess_waifu_robot"
    CHARA_CHANNEL_ID = "-1002091239384"
    api_id = 6252332
    api_hash = "2bf5e96a75ca073fd4f37ca9562971d3"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
