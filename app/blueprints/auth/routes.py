from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.models import User
from flask_login import current_user

from . import bp
from app.forms import RegisterForm
from app.forms import SigninForm

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'Welcome back, {form.username.data}. You are signed in.', "success")
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash(f"{form.username.data}/password not found", "warning")
    return render_template('signin.jinja', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out', 'success')
    return redirect(url_for('main.home'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data,email=form.email.data,first_name=form.first_name.data,last_name=form.last_name.data)
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f"{form.username.data} registered!", "success")
            return redirect(url_for("auth.signin"))
        if user:
            flash(f'{form.username.data} is already taken, please try again', 'warning')
        else:
            flash(f'{form.email.data} is already taken, please try again', 'warning')
    return render_template('register.jinja', form=form)

@bp.route('/contact')
def contact():
    return render_template('contact.jinja')

@bp.route('/commission')
def commission():
    return render_template('commission.jinja')

@bp.route('/purchase')
@login_required
def purchase():
    return render_template('purchase.jinja')