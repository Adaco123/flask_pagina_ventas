import os
from app import create_app
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
if __name__ == "__main__":
    os.environ['FLASK_DEBUG'] = "development"
    app.run(debug=True) 
