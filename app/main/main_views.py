from flask import Blueprint, render_template, url_for
from flask_login import current_user
from werkzeug.utils import redirect

from app import login_manager
from app.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


bp_main = Blueprint('main', __name__, url_prefix='/', template_folder='templates')


@bp_main.route('/', methods=['GET'])
def home():
    if current_user.is_anonymous:
        return redirect(url_for("auth.login"))
    return render_template("home.html")

