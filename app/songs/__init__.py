from flask import Blueprint, render_template, abort, current_app
import csv
import logging
import os
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename
from jinja2 import TemplateNotFound

songs = Blueprint('songs', __name__,
                        template_folder='templates')

@songs.route('/songs', methods=['POST', 'GET'])
def upload_playlist():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
    try:
        return render_template('upload_form.html', form=form)
    except TemplateNotFound:
        abort(404)