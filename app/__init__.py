from flask import Flask

app = Flask(__name__)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.forms import bp as forms_bp
app.register_blueprint(forms_bp)