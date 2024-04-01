from flask import Blueprint, render_template, request
from wtforms import Form, SubmitField, TextAreaField, validators


from database import insert_to_rsvp_schema, insert_to_feedback_schema, insert_to_email_schema

home = Blueprint('home', __name__)
rsvp_blueprint = Blueprint('rsvp', __name__)
feedback_blueprint = Blueprint('feedback', __name__)


class EmailForm(Form):
    email = TextAreaField('ur email', validators=[
        validators.InputRequired(message="??"), 
        validators.Length(min=5, message="too short!"), 
        validators.Length(max=30, message="too long!")],
        render_kw={'rows': 1, 'cols': 20, 'style':'resize:none;', 'placeholder': 'email'})
    submit = SubmitField('subscribe', render_kw={'style':"border:none; background: lightgrey;"})

class RSVPForm(Form):
    name = TextAreaField('name / alias', validators=[
        validators.InputRequired(message="what"), 
        validators.Length(min=2, message="too short!"), 
        validators.Length(max=20, message="too long!")],
        render_kw={'rows': 1, 'cols': 20, 'style':'resize:none;', 'placeholder': 'ur name / alias'})
    referral = TextAreaField('person who invited u', validators=[
        validators.InputRequired(message="who"), 
        validators.Length(min=2, message="too short!"), 
        validators.Length(max=20, message="too long!")],
        render_kw={'rows': 1, 'cols': 20, 'style':'resize:none;','placeholder': 'person who invited u'})
    email = TextAreaField('email', validators=[
        validators.InputRequired(message="uhh"), 
        validators.Email(message="this is not email"),
        validators.Length(min=2, message="too short!"), 
        validators.Length(max=50, message="too long!")],
        render_kw={'rows': 1, 'cols': 20, 'style':'resize:none;','placeholder': 'ur email'})
    submit = SubmitField('follow the white rabbit', render_kw={'style':"border:none; background: lightgrey;"})


class FeedbackForm(Form):
    feedback = TextAreaField('ur anonymous and honest feedback', validators=[
        validators.InputRequired(message="?"), 
        validators.Length(min=5, message="pls at least 5 characters!"), 
        validators.Length(max=1000, message="appreciate the effort but thats a bit too long")],
        render_kw={'rows': 10, 'cols': 50, 'style':'resize:none;', 'placeholder': 'ur anonymous and honest feedback'})
    submit = SubmitField('submit', render_kw={'style':"border:none; background: lightgrey;"})

@rsvp_blueprint.route('/rsvp', methods=('GET', 'POST'))
def rsvp():
    form = RSVPForm(request.form)
    
    if request.method == 'POST' and form.validate():
        insert_to_rsvp_schema(form.name.data, form.referral.data, form.email.data)
        return render_template('success.html')      
        
    return render_template('rsvp.html', form=form)

@feedback_blueprint.route('/feedback', methods=('GET', 'POST'))
def index():
    form = FeedbackForm(request.form)
    
    if request.method == 'POST' and form.validate():
        insert_to_feedback_schema(form.feedback.data)
        return render_template('success.html')      
        
    return render_template('feedback.html', form=form)

@home.route('/', methods=('GET', 'POST'))
def index():
    form = EmailForm(request.form)
    
    if request.method == 'POST' and form.validate():
        insert_to_email_schema(form.email.data)
        return render_template('success.html')      
        
    return render_template('index.html', form=form)


