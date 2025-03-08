from app import create_app
import os
app = create_app()

if __name__ == "__main__":
    os.environ['FLASK_DEBUG'] = "development"
    app.run(debug=True)

