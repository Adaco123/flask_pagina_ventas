import os
from app import create_app
from config import dev
settings_module = os.getenv('APP_SETTINGS_MODULE', dev)
app = create_app(settings_module)
print("APP_SETTINGS_MODULE:", settings_module)


if __name__ == "__main__":
    os.environ['FLASK_DEBUG'] = "development"
    app.run(debug=True) 
