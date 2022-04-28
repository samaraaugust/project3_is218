import os

from click.testing import CliRunner

from app import create_database

runner = CliRunner()

"""
def test_create_log_folder():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    #logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    logdir = os.path.exists("./app/logs")
    #assert os.path.exists(logdir) == True
    assert logdir == True
"""
"""
def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True
"""
"""
def test_create_uploads():
    response = runner.invoke(create_uploads_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    updir = os.path.join(root, '../uploads')
    # make a directory if it doesn't exist
    assert os.path.exists(updir) == True
"""