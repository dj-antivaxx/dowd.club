from flask import Blueprint, render_template, request
from wtforms import Form, SubmitField, TextAreaField, validators


from database import insert_to_rsvp_schema

home = Blueprint('home', __name__)

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

@home.route('/', methods=('GET', 'POST'))
def index():
    form = RSVPForm(request.form)
    
    if request.method == 'POST' and form.validate():
        insert_to_rsvp_schema(form.name.data, form.referral.data, form.email.data)
        return render_template('success.html')      
        
    return render_template('index.html', form=form)
