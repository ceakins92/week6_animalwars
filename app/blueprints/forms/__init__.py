from flask import Blueprint

bp = Blueprint('forms', __name__, url_prefix='/forms')

from app.blueprints.forms import routes