from flask import Blueprint

email_bp = Blueprint('email', __name__, template_folder='templates',static_folder='static',static_url_path="/email/static")

from . import routes
