from flask import Blueprint, jsonify, session, request, render_template, redirect
from app.models import User, db, Business, Review
from app.forms.business_form import BusinessForm
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import or_, and_


business_routes = Blueprint('business', __name__)


@business_routes.route('')
def get_all_businesses():
    buis_list = Business.query.all()
    new_lst = []
    for bis in buis_list
        bis
    print(buis_list)

    return render_template('landing_page.html', buis=buis_list)


@business_routes.route('/new')
def create_new_buis():
    form = BusinessForm()

    if form.validate_on_submit():
        data = form.data
        new_buis = Business(
            name = data['name'],
            category = data['category']
            owner_id = 1
        )
        db.session.commit()
        return redirect('/api/business')

    return render_template('new_buisness.html', form=form)
