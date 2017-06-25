from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object('config')

csrf = CSRFProtect(app)
csrf.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
