from server import app
from routes import auth, companies, companies_admin, users_admin, profile
from flask_wtf.csrf import CSRFProtect  # CWE-352: CSRF


csrf = CSRFProtect(app)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)