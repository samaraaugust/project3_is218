from flask import Blueprint, render_template

songs = Blueprint('songs', __name__,
                        template_folder='templates')
@songs.route('/songs')
def upload_playlist():
    return render_template('upload_form.html')