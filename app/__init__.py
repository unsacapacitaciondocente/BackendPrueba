from flask import Flask

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'caja.pruebasaqp@gmail.com',
    MAIL_PASSWORD = 'ylsjxkhumlmhmbkj'
)

app.config['SECRET_KEY'] = 'e4956c1e746a439599292e267b8afa6a'

