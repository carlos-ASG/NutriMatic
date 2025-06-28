import os
import reflex as rx
from dotenv import load_dotenv
load_dotenv()

USER=os.getenv("user")
PASSWORD=os.getenv("password")
HOST=os.getenv("host")
PORT=os.getenv("port")
DBNAME=os.getenv("dbname")

DB_URL=f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'

config = rx.Config(
    app_name="NutriMatic",
    db_url=DB_URL,
    tailwind=None
)