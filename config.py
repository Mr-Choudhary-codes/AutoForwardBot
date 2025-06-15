# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "22025896")
    API_HASH = environ.get("API_HASH", "c35613da18ef75e322e979bc1f70b1c7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7595583195:AAFAZPvPBaTmfKSucO3jsk1CK48x0N4NKGI") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", 7767099543).split()]
    BOT_SESSION = environ.get("BOT_SESSION", "BQGPUn8AHhvwMphLtw4enXLJtkqEZgtuijqf-oWVH3uYaRZztpjfhUUE8r9XDCocoWdvW0Vf_7MGw7yPwJ4t-zwL0XuU6MjLV6rfieurqBEtXFXKT6Tmj5f16vg0gQMYkFNH1U4gQnDbEOtgSdWzlhSKden4QLScYMG-0KPELbsee_bCqIufrPpgw2_JloMNZBx4a4bClQC0PDe7azKSd5w75Ks5qQrlME13aEPots8Tp6q4ejbZEPHsPnyRgRBSuahbYUbDggGvswhW7ZaIiCxaRw0Yv_P_uW0caxJnG8I7R3mMB0P3VD-XrLYuB-7MW2PETThqs5GWR2ZjbQ36qDYyUlyhMwAAAAHG7fs5AA")

    PICS = (environ.get('PICS', 'https://graph.org/file/fd5ce10d938e2e6c67f58-3fbde42385e9cc0792.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://KingOfHell:Highspeedorg@cluster0.ha2cc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002031903841))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "yOur_DadDy_vIcky") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
