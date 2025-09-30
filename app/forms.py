from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class AccessForm(FlaskForm):
    password = PasswordField('Access Password', validators=[DataRequired()])
    submit = SubmitField('Enter')

class JournalEntryForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), 
        Length(max=200, message='Title must be less than 200 characters')
    ])
    content = TextAreaField('Content', validators=[
        DataRequired(),
        Length(min=10, message='Content must be at least 10 characters long')
    ])
    submit = SubmitField('Save Entry')
