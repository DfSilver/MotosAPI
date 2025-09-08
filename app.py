from flask import Flask
from controllers.motor_controller import motor_bp         
from controllers.motorcycle_controller import motorcycle_bp  

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(motor_bp)
app.register_blueprint(motorcycle_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
