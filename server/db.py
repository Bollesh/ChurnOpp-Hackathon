from supabase import create_client, Client
from dotenv import load_dotenv
from os import environ

load_dotenv()

url: str = environ.get("SUPABASE_URL")
key: str = environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

