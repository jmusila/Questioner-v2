import os

from app.apps import create_app

app = create_app('development')

if __name__ == "__main__":
    app.run(debug=True)