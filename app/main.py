import os
from flask import Flask

app = Flask(__name__)

config_type = {
    "development":  "config.Development",
    "testing": "config.Testing",
}

app.config.from_object(config_type.get(os.getenv('FLASK_APP_ENV', 'development')))


@app.route('/')
def hello_world():

    return "Hello World"


if __name__ == '__main__':
    app.run()
