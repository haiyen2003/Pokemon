
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask
from .config import Config
from .models import db
from .routes import itemRoute, pokemonRoute
from flask_migrate import Migrate

import os

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(itemRoute.item_routes)
app.register_blueprint(pokemonRoute.pokenmon_routes)
db.init_app(app)
Migrate(app, db)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
