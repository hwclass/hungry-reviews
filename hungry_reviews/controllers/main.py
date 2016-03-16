from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from flask_wtf.csrf import CsrfProtect

from hungry_reviews.extensions import cache
from hungry_reviews.forms import LoginForm
from hungry_reviews.forms import ReviewForm
from hungry_reviews.models import User
from hungry_reviews.models import Review

main = Blueprint('main', __name__)

csrf = CsrfProtect()

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')

@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))

@csrf.exempt
@main.route("/grades", methods=["GET", "POST"])
@login_required
def grades():
    """Review view"""
    """
    form = ReviewForm()
    if form.validate_on_submit():
        review = "%s <%s>" % (form.grades.data, form.optional_comment.data)
        message = form.message.data
        return redirect(request.args.get("next") or url_for(".grades"))
    return render_template('grades.html', form=form)
    """

    """Review view"""
    form = ReviewForm()
    if form.validate_on_submit():
        current_review_data = "%s <%s>" % (form.grades.data, form.optional_comment.data)
        print current_review_data
        return render_template("grades.html",
                           form=form)
    else:
        flash_errors(form)

    return render_template("grades.html",
                       form=form)
