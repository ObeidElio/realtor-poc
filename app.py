from flask import Flask
from flask_cors import CORS
import routes

app = Flask(__name__)
CORS(app,resources={r'/api/*':{'origins':'*'}})

app.register_blueprint(routes.comprehend_router)


if __name__ == "__main__":
    app.run(port=5001,debug=True)