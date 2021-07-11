from flask import Flask

app = Flask(__name__)

from Service import app

app.run(debug=True)