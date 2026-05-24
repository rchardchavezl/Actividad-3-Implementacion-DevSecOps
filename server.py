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


# CWE-116: inyecta cabeceras HTTP de seguridad en todas las respuestas.
# Render.com no las añade automaticamente; deben configurarse en Flask
@app.after_request
def set_security_headers(response):
    # Evita que el navegador adivine el tipo MIME (MIME sniffing)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Bloquea que la pagina sea incrustada en iframes (clickjacking)
    response.headers['X-Frame-Options'] = 'DENY'
    # Fuerza HTTPS durante 1 año en navegadores que ya visitaron el sitio
    response.headers['Strict-Transport-Security'] = (
        'max-age=31536000; includeSubDomains'
    )
    # Politica de contenido: solo recursos del mismo origen
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' cdn.jsdelivr.net; "
        "style-src 'self' cdn.jsdelivr.net; "
        "font-src 'self' cdn.jsdelivr.net; "
        "img-src 'self' data:; "
        "frame-ancestors 'none'"
    )
    return response

@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403