from flask import Blueprint, render_template, abort, current_app, url_for
import csv
import logging
import os
from app.db import db
from app.db.models import Song
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename, redirect
from jinja2 import TemplateNotFound
from flask_login import current_user

songs = Blueprint('songs', __name__,
                        template_folder='templates')
"""
#@songs.route('/songs', methods=['GET'], defaults={"page": 1})
@songs.route('/songs/<int:page>', methods=['GET'])
def songs_browse(page):
    page = page
    per_page = 10
    pagination = Song.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_songs.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)
"""
@songs.route('/songs_tables/', methods=['GET'])
def browse_all_songs():
    data = Song.query.all()
    try:
        return render_template('browse_songs.html', data=data)
    except TemplateNotFound:
        abort(404)

@songs.route('/songs', methods=['POST', 'GET'])
def upload_playlist():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        filename = secure_filename(form.file.data.filename)
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