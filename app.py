from flask import Flask
from controllers.motorcycle_controller import motorcycle_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(motorcycle_bp)

@app.route("/")
def root():
    return (
        '<h3>Motorcycles API</h3>'
        '<p>Visita <a href="/motorcycles/tabla">/motorcycles/tabla</a> para ver la tabla en HTML.</p>'
        '<p>Para poblarla rápido: <code>POST /motorcycles/seed</code></p>'
    )

if __name__ == "__main__":
    app.run(debug=True)
