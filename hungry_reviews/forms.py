from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators

from .models import User


class LoginForm(Form):
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.optional()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our the exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True

class ReviewForm(Form):
    user_id = TextField(u'user_id', validators=[])
    grade = TextField(u'grade', validators=[validators.required()])
    optional_comment = TextField(u'comment', validators=[])

    def validate(self):
        check_validate = super(ReviewForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our the exist
        grade = Review.query.filter_by(grade=self.grade.data).first()
        if not grade:
            self.grade.errors.append('Please fill the grade')
            return False

        # Does our the exist
        optional_comment = Review.query.filter_by(grade=self.optional_comment.data).first()
        if not optional_comment:
            self.grade.errors.append('Please fill the optional comment')
            return False

        return True
