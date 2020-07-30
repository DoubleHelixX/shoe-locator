import os
from models import setup_db, Bay
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_moment import Moment
import manage as m
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from sqlalchemy import Column, String, Integer, create_engine

print('>>> 1')
def create_app(test_config=None):
  # create and configure the app
  print('>>> 2')
  
  app = Flask(__name__)
  print('>>> 3')
  
  setup_db(app)
  print('>>> 4')
  
  moment = Moment(app)
  return app



  # BOOTSTRAP DB migration command with migration file
  migration = m.migration(app, db)


  '''
    Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  #   '''
  # CORS(app, resources={r"/api/*": {"origins": "*"}})
    

  '''
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
  
  #----------------------------------------------------------------------------#
  # Controllers.
  #----------------------------------------------------------------------------#


  @app.route('/')
  def index():
    return render_template('index.html')


  #  Venues
  #  ----------------------------------------------------------------


  @app.errorhandler(404)
  def not_found_error(error):
      return render_template('errors/404.html'), 404

  @app.errorhandler(500)
  def server_error(error):
      return render_template('errors/500.html'), 500


  if not app.debug:
      file_handler = FileHandler('error.log')
      file_handler.setFormatter(
          Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
      )
      app.logger.setLevel(logging.INFO)
      file_handler.setLevel(logging.INFO)
      app.logger.addHandler(file_handler)
      app.logger.info('errors')

  #----------------------------------------------------------------------------#
  # Launch.
  #----------------------------------------------------------------------------#


  # Default port:
  if __name__ == '__main__':
      app.run()

  # Or specify port manually:
  '''
  if __name__ == '__main__':
      port = int(os.environ.get('PORT', 5000))
      app.run(host='0.0.0.0', port=port)
  '''
