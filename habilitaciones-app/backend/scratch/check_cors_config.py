
import os
import sys

# Add the backend directory to sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

print(f"Working directory: {os.getcwd()}")
print(f"Backend directory: {backend_dir}")

from app.core.config import settings

print(f"BACKEND_CORS_ORIGINS: {settings.BACKEND_CORS_ORIGINS}")
print(f"Type: {type(settings.BACKEND_CORS_ORIGINS)}")
