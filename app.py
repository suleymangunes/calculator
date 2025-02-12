import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")

print(f"Veritabanı urlsi: {database_url}")
print(f"Apı anahtari: {api_key}")
print(f"Gizli anahtar: {secret_key}")
print(f"debu modu: {debug_mode}")
