# from flask_moment import Moment
from models import setup_db, Bay, db_drop_and_create_all, db_drop_all
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from jinja2 import Environment, PackageLoader
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort,session
from sqlalchemy import Column, String, Integer, create_engine,and_
from auth import AuthError, requires_auth
from functools import wraps
from os import environ as env
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
import json
import constants




ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_CALLBACK_URL = env.get(constants.AUTH0_CALLBACK_URL)
AUTH0_CLIENT_ID = env.get(constants.AUTH0_CLIENT_ID)
AUTH0_CLIENT_SECRET = env.get(constants.AUTH0_CLIENT_SECRET)
AUTH0_DOMAIN = env.get(constants.AUTH0_DOMAIN)
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = env.get(constants.AUTH0_AUDIENCE)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
  
    # oauth = OAuth(app)
    # auth0 = oauth.register(
    #     'auth0',
    #     client_id=AUTH0_CLIENT_ID,
    #     client_secret=AUTH0_CLIENT_SECRET,
    #     api_base_url=AUTH0_BASE_URL,
    #     access_token_url=AUTH0_BASE_URL + '/oauth/token',
    #     authorize_url=AUTH0_BASE_URL + '/authorize',
    #     client_kwargs={
    #         'scope': 'openid profile email',
    #     },
    # )  
    
    app.secret_key = constants.SECRET_KEY
    app.debug = True
    configedDB = setup_db(app)
    if not configedDB:
      abort(500)
  
    # @app.errorhandler(Exception)
    # def handle_auth_error(ex):
    #     response = jsonify(message=str(ex))
    #     response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    #     return response
    
    

    '''
    CORS set up. Allowed '*' for origins. 
    '''
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    '''
    Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
        return response

    #----------------------------------------------------------------------------#
    # Controllers.
    #----------------------------------------------------------------------------#
    #db_drop_and_create_all()
    #db_drop_all()
    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/callback')
    def callback_handling():
        #auth0 = app.config['auth0']
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()
        print('>>>USER_INFO',userinfo)
        session[constants.JWT_PAYLOAD] = userinfo
        session[constants.PROFILE_KEY] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        return redirect('/manager/bay/all')

    @app.route('/login')
    def login():
        #auth0 = app.config['auth0']
        #state = uuid.uuid4().hex
        #redirect_url = url_for("auth.callback", _external=True)
        #auth0.save_authorize_state(redirect_uri=redirect_url, state=state)
        return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL, audience=AUTH0_AUDIENCE) #, state=state


    @app.route('/logout')
    def logout():
        session.clear()
        params = {'returnTo': url_for('home', _external=True), 'client_id': AUTH0_CLIENT_ID}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

    
    @app.route('/associate')
    def AssociateView():
        return render_template('associate-view.html')
    
    @app.route('/manager')
    def ManagerView():
        return render_template('manager-view.html')


    @app.route('/associate/shoe/<style_code>', methods =['GET'])
    def GetShoe(style_code):
        # *See if data is being passed and accepted through the url.*
        #print('>>>Shoe code: ', style_code)
        unprocessable = False
        searchFailure = False
        count=0
        try:
            listOfShoes=[]
            # *USING FLASH TO RELAY GET RESPONSE INSTEAD. Currently disabled in HTML as well*
            #flashOutput=[]
            
            receivedShoe = Bay.query.filter(Bay.style == style_code).order_by(Bay.bay).all()  
           
            
            if len(receivedShoe):   
                for shoe in receivedShoe:
                    listOfShoes.append(Bay.format(shoe))
                    
                    # countOfShoe = Shoes.query.filter(shoe.id == Shoes.id).one_or_none()
                    # if countOfShoe:
                    #     count+=1
                        
                    # *USING FLASH TO RELAY GET RESPONSE INSTEAD. Currently disabled in HTML as well*
                    #flashOutput.append('Bay:' + Bay.bay + ' Row: '+ Bay.row + ' Col: '+ Bay.col)
            else:  
                print('>>> no shoe results. Length is: ' , len(receivedShoe))
                searchFailure=True
           
            # *USING FLASH TO RELAY GET RESPONSE INSTEAD. Currently disabled in HTML as well*
            #flashListToStr = ' '.join([str(value) for value in flashOutput]) 
            #listToStr = ' '.join([str(value) for value in listOfShoes])                  
            #flash(flashListToStr)
            
        except expression as identifier:
            #flash('Shoe not in Records')
            unprocessable = true
            print('except Expression: ', identifier)
        finally:
            if searchFailure:
                abort(404)
            elif unprocessable:
                abort(422)
            else:
                return jsonify({
                    'success': True,
                    'shoe_info': listOfShoes,
                    'total_shoe_results': len(listOfShoes),
                    })
            


    @app.route('/manager/bay/<string:bay>', methods =['GET'])
    @requires_auth('get:bays')
    def ShowBay(*args, **kwargs): #*args, **kwargs
        bayData =[]
        bay = kwargs.get('bay', 'all')
        # *See if data is being passed and accepted through the url.*
        print('>>>Bay #: ',bay)
        unprocessable = False
        searchFailure = False
        bayCategories=None
        listOfBays=None
        blankPage=False
        
        try:
            if bay == 'all':
                listOfBays = Bay.query.order_by(Bay.bay , Bay.section).all()  
                print('>>>', listOfBays)
            else:
                listOfBays = Bay.query.filter(Bay.bay == bay).order_by(Bay.section).all()  
            
            if listOfBays:   
                for shoe in listOfBays:
                    #print('>>>1', listOfBays)
                    bayData.append(Bay.format(shoe))
                    #print('>>>2', shoe)
                    distinctBays = Bay.query.with_entities(Bay.bay).distinct().order_by(Bay.bay).all()
                    bayCategories = [str(char) for bay in distinctBays for char in bay if isinstance(char, int)]
                    #print('>>> distinct' , distinctBays,  'Bay Categories: ', bayCategories)                    
            elif not listOfBays and bay=='all':
                blankPage= True
            else:  
                print('>>> no such Bay. Length is: ' , listOfBays)
                searchFailure=True
        except:
            unprocessable = true
            print('Error Message: ', sys.exc_info())
        finally:
            if searchFailure:
                abort(404)
            elif unprocessable:
                abort(422)
            elif blankPage:
                responseData={ 
                                'success': True,
                                'baySelected': bay,
                                'bay_info': 'None'
                                }
                return jsonify(responseData)
                # return render_template('manager-view.html', responseData=responseData)
            else:
                return jsonify(responseData={ 
                                'success': True,
                                'baySelected': bay,
                                'bay_info': bayData,
                                'bay_categories': bayCategories,
                                'total_bay_results': len(listOfBays)
                                })
                # responseData={ 
                #                 'success': True,
                #                 'baySelected': bay,
                #                 'bay_info': bayData,
                #                 'bay_categories': bayCategories,
                #                 'total_bay_results': len(listOfBays)
                #                 }
                # return render_template('manager-view.html', responseData=responseData)
    
    
    @app.route('/manager/bay', methods =['PATCH'])
    @requires_auth('patch:bays')
    def EditBay(*args, **kwargs): 
        # *See if data is being passed and accepted through the url.*
        #print('>>>Bay #: ',bay)
        unprocessable = False
        searchFailure = False
        bayCategories=None
        listOfBays=None
        bayID= request.get_json()['bay']
        data =  request.get_json()['data']
        try:
            outdated_bay=[]
            updated_bay=[]
           
            #print(">>> outdated_bay: ", outdated_bay )
                
            for updatedShoe in data:
                print('@shoe: ', updatedShoe )
                
                outdatedShoe = Bay.query.filter(and_(Bay.id== int(updatedShoe['shoe_id'].strip()) , Bay.bay==bayID)).one_or_none()
                outdated_bay.append(Bay.format(outdatedShoe))
                print('@shoe: ', outdatedShoe )
                print('@OutdatedBay: ', outdated_bay )
                
                
                if outdatedShoe:
                    
                    outdatedShoe.section=updatedShoe['section'].strip()
                    
                    outdatedShoe.name=updatedShoe['name'].strip()
                           
                    outdatedShoe.style=updatedShoe['style'].strip()
                    
                    outdatedShoe.row=updatedShoe['row'].strip()
                    
                    outdatedShoe.col=updatedShoe['col'].strip()
                    
                    outdatedShoe.notes=updatedShoe['notes'].strip()

                    if(updatedShoe['img'].strip() != 'None'):
                        outdatedShoe.img=updatedShoe['img'].strip()
                        print('@img: ',  outdatedShoe.img )
                    else:
                        outdatedShoe.img=""
                    
                    outdatedShoe.gender=updatedShoe['gender'].strip()
                    print('@gender: ',  outdatedShoe.gender )
                    
                    outdatedShoe.update()
                    updatedShoe = Bay.query.filter(and_(Bay.id== int(updatedShoe['shoe_id'].strip()) , Bay.bay==bayID)).one_or_none()
                    print('@updatedShoe: ',  updatedShoe )
                    
                    updated_bay.append(Bay.format(updatedShoe))
                    print('@ updated_bay: ',   updated_bay )
                    
                else:  
                    print('@>>> no such Bay. Length is: ' , len(outdatedShoe))
                    searchFailure=True
                     
        except:
            unprocessable = true
            print('Error Message: ', sys.exc_info())
        finally:
            if searchFailure:
                abort(404)
            elif unprocessable:
                abort(422)
            else:
                responseData={ 
                                'success': True,
                                'bay':bayID,
                                'outdated_shoes': outdated_bay,
                                'updated_shoes': updated_bay,
                                'total_bay_results': len(updated_bay)
                                }
                return jsonify(responseData)
            
    @app.route('/manager/bay', methods =['DELETE'])
    @requires_auth('delete:bays')
    def DeleteBay(*args, **kwargs): 
        # *See if data is being passed and accepted through the url.*
        #print('>>>Bay #: ',bay)
        unprocessable = False
        searchFailure = False
        bayCategories=None
        listOfBays=None
        bayID= request.get_json()['bay']
        try:
            deleted_bay=[]
            deleted = Bay.query.filter(Bay.bay==bayID).all()
            if deleted:
               for gone in deleted:
                   deleted_bay.append(Bay.format(gone))
                   gone.delete()        
            else:  
                print('@>>> no such Bay.')
                searchFailure=True
                    
        except:
            unprocessable = true
            print('Error Message: ', sys.exc_info())
        finally:
            if searchFailure:
                abort(404)
            elif unprocessable:
                abort(422)
            else:
                responseData={ 
                                'success': True,
                                'bay':bayID,
                                'deleted_shoes': deleted_bay
                                }
                return jsonify(responseData)

    @app.route('/manager/bay', methods =['POST'])
    @requires_auth('create:bays')
    def CreateBay(*args, **kwargs): 
        # *See if data is being passed and accepted through the url.*
        #print('>>>Bay #: ',bay)
        unprocessable = False
        existFailure = False
        bayCategories=None
        listOfBays=None
        created=None
        bayID=int(request.get_json()['bay'].strip())
        data = request.get_json()['data']
        try:
            print('@bay' , bayID)
            createdBay=[]
            exist = Bay.query.filter(Bay.bay==bayID).all()
            print('@ exist' ,exist)
            if not exist:
                for shoe in data:
                    #print('@ shoe', shoe)
                    toBeCreated = Bay(bay=bayID, section=shoe['section'].strip() , name=shoe['name'].strip() , style=shoe['style'].strip() , row=shoe['row'].strip() , col=shoe['col'].strip() , notes=shoe['notes'].strip() , img=shoe['img'].strip() , gender=shoe['gender'].strip() )
                    # print('@ created', toBeCreated)
                    
                    toBeCreated.insert()
            
                created = Bay.query.filter(Bay.bay==bayID).all()
                
                if created:
                    for shoe in created:
                        createdBay.append(Bay.format(shoe))
            else:
                existFailure=True
        except:
            unprocessable = true
            print('Error Message: ', sys.exc_info())
        finally:
            if unprocessable:
                abort(422)
            elif existFailure:
                responseData={ 
                                'success': False,
                                'exist': existFailure,
                                'bay':bayID,
                                }
                return jsonify(responseData)
            else:
                responseData={ 
                                'success': True,
                                'exist': existFailure,
                                'bay':bayID,
                                'created_bay': createdBay
                                }
                return jsonify(responseData)

    
    # @app.route('/manager/data/<string:bay_id>', methods =['GET'])
    # @requires_auth('get:data')
    # def ShowData(*args, **kwargs): #*args, **kwargs
    #     bayData =[]
    #     bay_id = kwargs.get('bay_id', 'all')
    #     # *See if data is being passed and accepted through the url.*
    #     print('>>>Bay #: ',bay)
    #     unprocessable = False
    #     searchFailure = False
    #     bayCategories=None
    #     listOfBays=None
    #     blankPage=False
        
    #     try:
    #         if bay_id == 'all':
    #             listOfBayData = Data.query.order_by(Data.bay_id).all()  
    #             print('>>>', listOfBayData)
    #         else:
    #             listOfBayData = Data.query.filter(Data.bay_id == bay_id).one_or_none()  
            
    #         if listOfBayData:   
    #             for bay in listOfBayData:
    #                 #print('>>>1', listOfBays)
    #                 bayData.append(Data.format(bay))                     
    #         else:  
    #             print('>>> no such Data for this Bay.')
    #             searchFailure=True
    #     except:
    #         unprocessable = true
    #         print('Error Message: ', sys.exc_info())
    #     finally:
    #         if searchFailure:
    #             abort(404)
    #         elif unprocessable:
    #             abort(422)
    #         else:
    #             return jsonify(responseData={ 
    #                             'success': True,
    #                             'bay_data': bayData,
    #                             'total_data_results': len(listOfBayData)
    #                             })
                
                
    #  ----------------------------------------------------------------
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
