from dotenv import load_dotenv
from os import environ

load_dotenv()

TOKEN = environ.get("TOKEN")

PG_URL = environ.get("PG_URL")