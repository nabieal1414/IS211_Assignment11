from flask import Flask
from flask_migrate import Migrate 

from routes.todo import todo_bp

app=Flask(__name__)

app.register_blueprint(todo_bp, url_prefix='/')


if __name__ == '__main__':
    app.debug = True
    app.run()
