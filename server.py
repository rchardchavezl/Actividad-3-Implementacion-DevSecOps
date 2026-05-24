import os
from datetime import timedelta
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect  # CWE-352: proteccion CSRF

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32)
app.permanent_session_lifetime = timedelta(minutes=30)

# CWE-352: inicializar CSRFProtect para que los tokens csrf_token()
# de los templates sean validados en cada POST
csrf = CSRFProtect(app)

@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403