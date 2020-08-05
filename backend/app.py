import os
from models import setup_db, Bay
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_moment import Moment
from jinja2 import Environment, PackageLoader
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from sqlalchemy import Column, String, Integer, create_engine

def create_app(test_config=None):
    # env = Environment(loader=PackageLoader('flaskr', '..\\..\\frontend\\templates'))
    # template = env.get_template('testing.html')
    # create and configure the app
    app = Flask(__name__)
    configedDB = setup_db(app)
    if not configedDB:
      abort(500)
  
    # moment=Moment(app)
    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
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
    
    @app.route('/associate')
    def AssociateView():
        return render_template('associate-view.html')
    
    @app.route('/manager')
    def ManagerView():
        return render_template('manager-view.html')


    @app.route('/shoe/<style_code>', methods =['GET'])
    def GetShoe(style_code):
        #print('>>>4', style_code)
        try:
            listOfShoes=[]
            flashOutput=[]
            receivedShoe = Bay.query.filter(Bay.style == style_code).order_by(Bay.bay).all()  
            
            for shoe in receivedShoe:
                listOfShoes.append(Bay.format(shoe))
                flashOutput.append('Bay:' + Bay.bay + ' Row: '+ Bay.row + ' Col: '+ Bay.col)
            
            flashListToStr = ' '.join([str(value) for value in flashOutput]) 
            listToStr = ' '.join([str(value) for value in listOfShoes])                  
            flash('sdsds')
            
        except expression as identifier:
            flash('Shoe not in Records')
        finally:
            return jsonify({
                'success': True,
                'bay_info': listOfShoes,
                'total_bay_results': len(listOfShoes),
                })
        

    
       
    
    
    #  Error Handlers
    #  ----------------------------------------------------------------

@app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource or url not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422
    
  @app.errorhandler(405)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400


  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "Something is wrong with the server configuration"
      }), 500
    


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
        app.run(host = '127.0.0.1')

    # Or specify port manually:
    '''
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
    '''
    return app
