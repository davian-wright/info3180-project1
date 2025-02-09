"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
import flask
from flask import Flask, render_template, flash, request, redirect, url_for
from .forms import NewPropertiesForm
import  random


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Davian Wright")


@app.route('/Property/', methods=['GET', 'POST'])
def Property():
    """Render the websites New property page  """
    form = NewPropertiesForm()
    propertyid= random.randint(0,100)
    if form.validate_on_submit():
        if request.method == 'POST':
            
            flash(("File uploaded."), "success")
        return redirect("/Properties/")
    
    return render_template('properties.html',form=form,template="form-template",propertyid=propertyid)


@app.route('/Properties/')
def Properties():
    """Render the websites properties page  """
    return render_template('property.html')




 
@app.route('/Property/<propertyid>')
def Propertybyid(propertyid):

    return render_template('propertybyid.html')


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
