from flask import Flask
from blueprint import api_v1

app = Flask(__name__)

app.register_blueprint(api_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)