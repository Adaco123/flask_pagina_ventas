import os
from app import create_app
from config import dev, local, prod
settings_module = os.getenv('APP_SETTINGS_MODULE', dev)
app = create_app(settings_module)
#print("APP_SETTINGS_MODULE:", settings_module)