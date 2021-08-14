#Libraries
from flask_cors import CORS
from app import app
from app.routes import api
#Configuration 
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)




