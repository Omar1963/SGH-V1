
import os
import sys

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_dir)

print("Importing Pydantic Settings...")
try:
    from pydantic_settings import BaseSettings
    print("Pydantic Settings imported successfully.")
except Exception as e:
    print(f"Failed to import Pydantic Settings: {e}")

print("Importing app.core.config...")
try:
    from app.core.config import Settings
    print("Settings class imported successfully.")
    s = Settings()
    print(f"BACKEND_CORS_ORIGINS: {s.BACKEND_CORS_ORIGINS}")
except Exception as e:
    print(f"Failed to import/init settings: {e}")
