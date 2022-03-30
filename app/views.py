"""
Flfile Documentation:     https://flfile.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db
from flask import flash, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import AddProperty
from app.models import Property


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
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods = ['GET', 'POST'])
def addproperty():
    """Render the website's new properties form."""
    formObj =  AddProperty()
    if request.method == 'GET':
        return render_template ('addproperty.html', createForm = formObj)

    if request.method == 'POST':
        if formObj.validate_on_submit():
            fileObj = request.files['photo']
            recvFiles = secure_filename(fileObj.filename)
            fileObj.save(os.path.join(app.config['UPLOAD_FOLDER'], recvFiles))
            if fileObj and recvFiles != "":
                property_add = Property(request.form['title'], request.form['num_bedrooms'], request.form['num_bathrooms'], request.form['location'], request.form['price'],  request.form['property_type'], request.form['description'], request.form['photo'])
                db.session.add(property_add)
                db.session.commit()
                flash('The property was successfully added!', 'success')
                return redirect(url_for('properties'))
    return render_template('addproperty.html', createForm = formObj)


@app.route('/properties')
def properties():
    """Render the list of all properties in the database"""
    if request.method == 'GET':
        propLst = Property.query.all()
        return render_template('properties.html', propInfo = propLst)


@app.route('/properties/<propertyid>')
def propertyID(propertyid):
    """Renders individual properties."""
    pID = db.session.query(Property).filter(Property.id==propertyid).first()
    return render_template('property.html', property=pID)


@app.route('/uploads/<filename>')
def image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flfile apps.
###

# Display Flfile WTF errors as Flash messages
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