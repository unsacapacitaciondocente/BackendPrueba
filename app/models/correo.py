from app import app
from flask_mail import Mail, Message 
  
mail = Mail(app) 
def send_email(data):
   dest=data["destinatario"].split(sep=';')
   msg = Message(data["asunto"],
              sender=app.config['MAIL_USERNAME'],
              recipients=dest)
   msg.html = data["mensaje"]
   mail.send(msg)
   return 'Enviado'
   