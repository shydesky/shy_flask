from flask import Flask
from extensions import api

app = Flask(__name__)
app.config.from_object('config')
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
