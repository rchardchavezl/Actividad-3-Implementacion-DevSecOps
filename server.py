import os
from datetime import timedelta
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32)
app.permanent_session_lifetime = timedelta(minutes=30)

# CWE-116: cabeceras HTTP de seguridad
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = (
        'max-age=31536000; includeSubDomains'
    )
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