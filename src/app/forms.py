from flask.ext.wtf import Form
from wtforms.fields import SelectField, HiddenField
from wtforms import TextAreaField
from wtforms.validators import Required

class ReviewForm(Form):
	user_id = HiddenField('user_id', default=989576934, validators = [Required()])
	point = SelectField(u'Select to Grade', choices=[('1', 'Bad'), ('2', 'Not So Bad'), ('3', 'Average'), ('4', 'Good'), ('5', 'Excellent')])
	optional_comment = TextAreaField('optional_comment', validators = [Required()])
