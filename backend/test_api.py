import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from constants import database_setup, bearer_tokens
from app import create_app
from models import setup_db, Bay, db_drop_and_create_all,  db_initialize_tables_json


assistant_manager_auth_header = {
            'Authorization': bearer_tokens['assistant_manager']
            }

store_manager_auth_header = {
            'Authorization': bearer_tokens['store_manager']
            }
        
class ShoeLocateTestCase(unittest.TestCase):
    """This class represents the shoe locate test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql+psycopg2://{}:{}@{}/{}".format(database_setup['user_name'], database_setup['password'], database_setup['port'], database_setup['database_name'])
        setup_db(self.app, self.database_path)
        
        
        self.new_bay = {
            "bay": "12",
            "data": [{
                "section": "A",
                "name":  "new bay",
                "style": "S5454",
                "row": "4",
                "col": "2",
                "notes":  "Box color is Yellow.",
                "gender":  "M",
                "img":  "https://bit.ly/31sgwi5"
            }]
        }

        self.edit_bay = {
            "bay": "1" ,
            "data" : [{
            "shoe_id": "5",
            "section": "A"  ,
            "name":  "CHANGED BABY" ,
            "style": "S5454"  ,
            "row": "4"  ,
            "col": "2"  ,
            "notes":  "SOME NOTES" ,
            "gender":  "F" ,
            "img":  "https://images.unsplash.com/photo-1536787175219-c199c3100742?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80" 
            }]
        }

        self.edit_bay_403 = {
            "bay": "1" ,
            "data" : [{
            "shoe_id": "10",
            "section": "B"  ,
            "name":  "CHANGED BABY" ,
            "style": "4554"  ,
            "row": "5"  ,
            "col": "1"  ,
            "notes":  "SOME NOTES" ,
            "gender":  "M" ,
            "img":  "" 
            }]
        }
        
        self.delete_bay = {
	        "bay": "2"
        }

        self.edit_bay_404= {
            "bay": "9999" ,
            "data" : [{
            "shoe_id": "10",
            "section": "A"  ,
            "name":  "CHANGED BABY" ,
            "style": "S5454"  ,
            "row": "4"  ,
            "col": "2"  ,
            "notes":  "SOME NOTES" ,
            "gender":  "F" ,
            "img":  "https://images.unsplash.com/photo-1536787175219-c199c3100742?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80" 
            }]
        }      
          
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            # self.db.session.close()
            # self.db.session.remove()
            # db_drop_and_create_all()
            # db_initialize_tables_json()
           
            
              
            
        

    def tearDown(self):
        """Executed after each test"""
        pass

    # * ----- TESTING GET ON SHOE ROUTE ----- *

    def test_200_get_shoe(self):
        res = self.client().get('/associate/shoe/2759')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['shoe_info'])
        self.assertEqual(data['total_shoe_results'],1)

    def test_404_get_unknown_shoe(self):
        res = self.client().get('/associate/shoe/99999999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource or url not found')

    
    # * ----- END OF TESTING GET ON SHOE ROUTE ----- *
      
    # * ----- TESTING GET ON BAY ROUTE ----- *
    
    def test_200_get_bay_all_authroized(self):
        res = self.client().get('/manager/bay/all', headers =store_manager_auth_header )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['baySelected'], 'all')
        self.assertTrue(len(data['bay_info']))
        self.assertEqual(len(data['bay_categories']),2)
        self.assertEqual(data['total_bay_results'],16)
        
    def test_200_get_bay_all_authroized_second_group(self):
        res = self.client().get('/manager/bay/all', headers = assistant_manager_auth_header )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['baySelected'], 'all')
        self.assertTrue(len(data['bay_info']))
        self.assertEqual(len(data['bay_categories']),2)
        self.assertEqual(data['total_bay_results'],16)
        
    def test_200_get_bay_specific(self):
        res = self.client().get('/manager/bay/1', headers =store_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['baySelected'], '1')
        self.assertTrue(len(data['bay_info']))
        self.assertTrue(len(data['bay_categories']))
        self.assertEqual(data['total_bay_results'], 6)
        
    def test_401_get_bay_all_no_header(self):
        res = self.client().get('/manager/bay/all')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')
    
    def test_404_get_unknown_bay(self):
        res = self.client().get('/associate/shoe/99999999', headers =store_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource or url not found')
        
    
    # * ----- END OF TESTING GET ON BAY ROUTE ----- *  
    
      
    # # * ----- TESTING PATCH BAY ROUTE ----- *
    
    def test_patch_new_bay(self):
        res = self.client().patch('/manager/bay', json=self.edit_bay, headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_shoes'])
        self.assertTrue(data['outdated_shoes'])
        self.assertEqual(data['bay'], '1')
        self.assertEqual(data['total_bay_results'], 1)
        
        
    def test_422_if_bay_patch_fails(self):
        res = self.client().patch('/manager/bay', json="", headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
    def test_403_patch_bay_unauthorized(self):
        res = self.client().patch('/manager/bay', json=self.edit_bay_403, headers =assistant_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')
        
 
    def test_404_patch_unknown_bay(self):
        res = self.client().patch('/manager/bay', json=self.edit_bay_404, headers =store_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource or url not found')
    # * ----- END OF TESTING PATCH BAY ROUTE ----- *

        
    # * ----- TESTING DELETE BAY ROUTE ----- *

    def test_delete_bay_authorized(self):
        res = self.client().delete('/manager/bay', json= self.delete_bay,headers =store_manager_auth_header)
        data = json.loads(res.data)

        bay = Bay.query.filter(Bay.bay == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_total'], 10)
        self.assertTrue(data['deleted_shoes'])
        self.assertEqual(data['bay'],'2')
        self.assertEqual(bay, None)
        
    def test_403_delete_bay_unauthorized(self):
        res = self.client().delete('/manager/bay', json= {'bay' : '1'}, headers=assistant_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')
        
    def test_404_delete_unknown_bay(self):
        res = self.client().delete('/manager/bay', json= {'bay':9999999}, headers=store_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource or url not found')
        
    def test_422_if_delete_bay_fails(self):
        res = self.client().delete('/manager/bay', json= {'bay':'asfasfafa'},headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
    
    # * ----- END OF TESTING DELETE BAY ROUTE ----- *
    
    
    # * ----- TESTING CREATE BAY ROUTE ----- *
    
    def test_create_new_bay(self):
        res = self.client().post('/manager/bay', json=self.new_bay, headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['exist'], False)
        self.assertTrue(data['created_bay'])
        self.assertEqual(data['bay'], 12)
        
       
    def test_422_if_bay_creation_fails(self):
        res = self.client().post('/manager/bay', json={"difficulty":[1,2,3]}, headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
    def test_403_create_bay_unauthorized(self):
        res = self.client().post('/manager/bay', json= self.new_bay, headers=assistant_manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')
        
    def test_exist_Failure(self):
        res = self.client().post('/manager/bay', json=self.new_bay, headers =store_manager_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['exist'], True)
        self.assertEqual(data['bay'], 12)
  
    
    # * ----- END OF TESTING CREATE BAY ROUTE ----- *
    
   

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
