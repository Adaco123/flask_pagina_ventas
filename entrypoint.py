import os
from app import create_app
from config import dev, local, prod
settings_module = os.getenv('APP_SETTINGS_MODULE', dev)
app = create_app(settings_module)
#print("APP_SETTINGS_MODULE:", settings_module)

from flask import send_from_directory

@app.route('/media/posts/<filename>')
def media_posts(filename):
    dir_path = os.path.join(
        app.config['MEDIA_DIR'],
        app.config['POSTS_IMAGES_DIR'])
    return send_from_directory(dir_path, filename)