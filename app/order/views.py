from flask import Blueprint, render_template, flash, url_for
from flask_login import login_required
from sqlalchemy import desc
from werkzeug.utils import redirect

from app import db
from app.order.forms import OrderForm
from app.order.model import Order

bp_order = Blueprint('order', __name__, url_prefix='/order', template_folder='templates')


@bp_order.route('/', methods=["GET", "POST"])
@login_required
def orders():
    all_order = Order.query.order_by(desc(Order.date_created)).limit(100)

    form = OrderForm()

    if form.validate_on_submit():
        order = Order(name=form.name.data, shop=form.shop.data, info=form.info.data, deadline=form.deadline.data)

        db.session.add(order)
        db.session.commit()

        flash(f'Select products!')
        return redirect(url_for('order.orders'))

    return render_template('orders.html', orders=all_order, form=form)


@bp_order.route('/<int:article_id>')
@login_required
def order(order_id):
    one_order = Order.query.filter_by(id=order_id).first_or_404()
    return render_template('order.html', order=one_order)

