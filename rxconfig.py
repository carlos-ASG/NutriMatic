import os
import reflex as rx
from dotenv import load_dotenv
load_dotenv()

USER=os.getenv("user")
PASSWORD=os.getenv("password")
HOST=os.getenv("host")
PORT=os.getenv("port")
DBNAME=os.getenv("dbname")

class CustomConfig(rx.Config):
    database_url: str

config = CustomConfig(
    app_name="NutriMatic",
    database_url=f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
)