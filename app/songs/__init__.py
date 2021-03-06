from flask import Blueprint, render_template, abort, current_app, url_for
import csv
import logging
import os
from app.db import db
from app.db.models import Song
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename, redirect
from jinja2 import TemplateNotFound
from flask_login import current_user, login_required

songs = Blueprint('songs', __name__,
                        template_folder='templates')

@songs.route('/songs_tables', methods=['GET'])
@login_required
def browse_all_songs():
    data = Song.query.all()
    log3 = logging.getLogger("request")
    log3.info("Request Method: browse_all_songs")
    try:
        return render_template('browse_songs.html', data=data)
    except TemplateNotFound:
        abort(404)

@songs.route('/songs', methods=['POST', 'GET'])
@login_required
def upload_playlist():
    log3 = logging.getLogger("request")
    log3.info("Request Method: upload_playlist")
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        log2 = logging.getLogger("csv")
        filename = secure_filename(form.file.data.filename)
        log2.info("CSV Uploaded: " + filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        songsL = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                songsL.append(Song(row['Name'], row['Artist'], row['Year'], row['Genre']))

        current_user.songs = songsL
        db.session.commit()
        return redirect(url_for('songs.browse_all_songs'))

    try:
        return render_template('upload_form.html', form=form)
    except TemplateNotFound:
        abort(404)