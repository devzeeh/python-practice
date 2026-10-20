import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME", "My Application")
app_env = os.getenv("APP_ENV", "development")
db_host = os.getenv("DB_HOST", "localhost")
db_port = int(os.getenv("DB_PORT", "5432"))

print(f"Application: {app_name}")
print(f"Environment: {app_env}")
print(f"Database host: {db_host}")
print(f"Database port: {db_port}")