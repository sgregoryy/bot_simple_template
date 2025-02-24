import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admin_ids_str = os.getenv('ADMIN_IDS', '')
ADMIN_IDS = [int(id_str) for id_str in admin_ids_str.split(',') if id_str]

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')