import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BOT_TOKEN = os.environ.get('BOT_TOKEN')  # Discord bot OAuth token

DATABASE_URL = os.environ.get('DATABASE_URL')  # e.g. postgres://user:pass@localhost:5432/databasename
