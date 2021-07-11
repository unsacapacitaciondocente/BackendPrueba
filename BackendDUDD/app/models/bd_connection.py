from app import app
from flask_sqlalchemy import SQLAlchemy

#Configuration 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tudbxlcyribgep:592c60d27fb885f4bc7048c14b0f6149c052924ac5a22d6b738c580a212bf20a@ec2-35-169-188-58.compute-1.amazonaws.com:5432/d85nt7mmna0ft6"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False