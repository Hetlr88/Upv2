import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7352645964:AAHjLhEQ17cBn2xnFWLazCwA_eOeP-JRWcE")
    
    API_ID = int(os.environ.get("API_ID", 29452145))
    
    API_HASH = os.environ.get("API_HASH","5a2784e571fe5043852d32396a34a13b")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "6169288210"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://KannadaMagaa:KannadaMagaa@kannadamagaaclone.kweqbmy.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
