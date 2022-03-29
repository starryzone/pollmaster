import os

class Secrets:
    def __init__(self):
        self.dbl_token = ''  # DBL token (only needed for public bot)
        self.mongo_db = os.environ.get('PM_DB')
        self.bot_token = os.environ.get('PM_BOT_TOKEN')
        self.mode = 'development' # or production

SECRETS = Secrets()