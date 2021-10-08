from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4956c1e746a439599292e267b8afa6a'

from Service import app

app.run(debug=True)
