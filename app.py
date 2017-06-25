from flask import Flask
from extensions import api
from shy_flask import (module1)
app = Flask(__name__)
app.config.from_object('config')
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
