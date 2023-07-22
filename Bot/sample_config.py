class Config(object):
    LOGGER = True
    TOKEN = "5868970687:AAFN3AAe67rKVYEN8PBiRoUr20cGH2k8Elc"
    DB_URI = ""
    OWNER_ID = 734788724


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
