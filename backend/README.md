# Backend
The backend consist of these files:
- app.py
- auth.py
- constants.py
- models.py
- manage.py
- test_api.py

## app.py
There are currently 8 classes for handling enpoints:
    - AssociateView() : `/associate` :  Renders the associate-view.html.
    - ManagerView() : `/manager` : Renders the manager-view.html.
    - GetShoe() : `/associate/shoe/<style_code>` : returns information on the shoe given via the style_code variable.
    - ShowBay() : `/manager/bay/<string:bay>` : returns information on the bay given via the bay variable.
    - EditBay() : `/manager/bay` : Edits existing bay : returns info pertaining to the new changes.
    - DeleteBay() : `/manager/bay` : Deletes existing bay : returns info pertaining to the deletion.
    - CreateBay() : `/manager/bay` : Creates a new bay : returns info pertaining to the creation.


### Running
In order to run the application:
1)  **First make sure your environment is active:**
    - [How to set up a python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
    
2) **Next navigate to the backend folder and run the following commands:**
    - **Install the requirements:**
        ```
        pip install -r requirements.txt
        ``` 
    - **set Flask App:** `Set according to your path`
        ```
        set FLASK_APP=app.py
        ```   
    - **Run Application:**
        ```
        flask run
        ``` 
3) This project uses the `Better Comments` Extension for showcasing comments. Install [Here](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
4) Omit the  `db_drop_and_create_all()` & ` db_initialize_tables_json() ` methods to pump starter data in the database.

### Alternate starter data initialization Locally
#### CSV PSQL CMD
1) Place the `[bays_csv](bays_.csv)` file located in the backend folder to a public directory similar to `C:\Users\Public\`
2) within PSQL CMD, run these commands
```
COPY bays(id,bay, section, name, style, row, col, notes, img, gender)
FROM 'C:\Users\Public\bays_.csv'
DELIMITER ','
CSV HEADER;
```
3) The response from the PSQL CMD should showcase something similar to `COPY 16`.

#### CSV Pandas - programmingly
**`This method of data initialization is currently not implemented correctly yet.`**
- The method `db_initialize_tables_csv_pandas()` is similar to CSV PSQL CMD however, you only follow step 1.
- Next you omit any commented code within `models.py` pertaining to CSV Pandas and run the app.

## auth.py
In order to set up your auth0 account and understand the auth logic in this app please read below.

### Auth0 for locally use
#### Create an App & API

1. Login to https://manage.auth0.com/ 
2. Click on Applications Tab
3. Create Application
4. Give it a name like `Show` and select "Regular Web Application"
5. Go to Settings and find `domain`. Copy & paste it into config.py => auth0_config['AUTH0_DOMAIN'] (i.e. replace `"test.auth0.com"`)
6. Click on API Tab 
7. Create a new API:
   1. Name: `Show`
   2. Identifier `show`
   3. Keep Algorithm as it is
8. Go to Settings and find `Identifier`. Copy & paste it into config.py => auth0_config['API_AUDIENCE'] (i.e. replace `"Example"`)

#### Create Roles & Permissions

1. Before creating `Roles & Permissions`, you need to `Enable RBAC` in your API (API => Click on your API Name => Settings = Enable RBAC => Save)
2. Also, check the button `Add Permissions in the Access Token`.
2. First, create a new Role under `Users and Roles` => `Roles` => `Create Roles`
3. Give it a descriptive name like `Store Manager`.
4. Go back to the API Tab and find your newly created API. Click on Permissions.
5. Create & assign all needed permissions accordingly 
6. After you created all permissions this app needs, go back to `Users and Roles` => `Roles` and select the role you recently created.
6. Under `Permissions`, assign all permissions you want this role to have. 

# <a name="authentification-bearer"></a>
### Auth0 to use existing API
If you want to access the real, temporary API, bearer tokens for all 2 roles are included in the `constant.py` file.

## Existing Roles

They are 3 Roles with distinct permission sets:

1. Public Endpoints:
    - GET /associate/shoe/<shoe_id>: Can see shoe information
2. Assistant Store Manager: (everything from public plus)
    - GET /manager/bay/<bay_id> (get:bays): Can get Bay information.
3. Store Manager (everything from assistant store manager plus)
    - POST /manager/bay (post:bays): Can create new Bays.
    - PATCH /manager/bay (patch:bays): Can edit existing Bays.
    - DELETE /manager/bay (delete:bays): Can remove existing Bays from database.

In your API Calls, add them as Header, with `Authorization` as key and the `Bearer token` as value. Don´t forget to also
prepend `Bearer` to the token (seperated by space).

For example: (Bearer token for `Assistant store manager`)
```js
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJpZzd3T0p6dEo1MnZDMzFBN2FyNyJ9.eyJpc3MiOiJodHRwczovL2RvdWJsZS1oZWxpeHgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMGNmMWM3MmViMzAzMDAxOWM4NzFkZSIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTk3ODAwNjY3LCJleHAiOjE1OTc4ODcwNjcsImF6cCI6Imw2eW5nNUxGdEtaSUZaNkk1NmZnUHlKcWJmSjN5ZzhVIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YmF5cyIsImdldDpkYXRhIiwiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.mmh-UKWgoFs0ciZlgkgRFLQ2uo93hBTP1-LiOl2TV6p6ycBpFP4LtAwgQS1iB-hJsNIBytpR8V7NxB_HmoD3s14_MxT0I6uAtg8O4rRyuuTUeTcMVi5Bc-6emHcioNp6KSV5YxtV3lqPkcSe1OPkNlTvTtDb-RDaKLrpO2aaFzZVHb8Cl04EBoTWcCAeYRepiK8z8NLWAH3OnFv0BVzmAL4lXwvA8by8Bh6A825MLKC67qnQsNetQ_-2hSj-fXeSyR_pl-SGjJZktllm8POWvvtFBJCjIKcgqLVTHZf9g6p7-GvroskxKtsoJpiE0eetykKiqXOP2QMsXhV546yOEA"
}
```
## Constants.py
This file contains all the constant data that will be needed to run the app correctly.
 - Includes
    - Auth config variables
    - JSON Data for bays
    - Bearer tokens for Auth

## models.py
`models.py` contains all the logic for setting up the database and mapping it to sqlalchemy, dropping the database, creating the database, and pumping starter data in the database.

## manage.py
`manage.py` contains the migration configuration for running flask migrations library.
    - Useful migrate commands.
        - flask db init
        - flask db migrate
        - flask db upgrade
        - flask db downgrade
        - etc

## test_api.py
This is unit test for testing `app.py`.
**` DO NOT TOUCH`**