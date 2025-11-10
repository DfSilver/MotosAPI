from flask import Flask
from controllers.motorcycle_controller import motorcycle_bp
from controllers.auth_controller import auth_bp  

app = Flask(__name__)


# 🔐 Clave secreta para JWT
app.config["SECRET_KEY"] = "supersecretkey123" 

# Registrar el blueprint
app.register_blueprint(motorcycle_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def root():
    return (
        '<h3>Motorcycles API</h3>'
        '<p>Visita <a href="/motorcycles/tabla">/motorcycles/tabla</a> para ver la tabla en HTML.</p>'
        '<p>Para poblarla rápido: <code>POST /motorcycles/seed</code></p>'
    )

if __name__ == "__main__":
    from waitress import serve
    import os
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)
