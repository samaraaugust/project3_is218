from flask import Blueprint, render_template
import csv
from app.songs.forms import csv_upload

songs = Blueprint('songs', __name__,
                        template_folder='templates')
@songs.route('/songs', methods=['POST', 'GET'])
def upload_playlist():
    form = csv_upload()
    return render_template('upload_form.html', form=form)