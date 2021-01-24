from flask import Blueprint, render_template

from app import login_manager
from app.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


bp_main = Blueprint('main', __name__, url_prefix='/', template_folder='templates')


@bp_main.route('/', methods=['GET'])
def home():
    return render_template('home.html')
