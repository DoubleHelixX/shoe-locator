""" Constants file for Auth0's seed project
"""
AUTH0_CLIENT_ID = 'AUTH0_CLIENT_ID'
AUTH0_CLIENT_SECRET = 'AUTH0_CLIENT_SECRET'
AUTH0_CALLBACK_URL = 'AUTH0_CALLBACK_URL'
AUTH0_DOMAIN = 'AUTH0_DOMAIN'
AUTH0_AUDIENCE = 'AUTH0_AUDIENCE'
PROFILE_KEY = 'profile'
SECRET_KEY = 'ThisIsTheSecretKey'
JWT_PAYLOAD = 'jwt_payload'


""" Constants file for Auth0's seed project
"""


bearer_tokens = {
    "store_manager" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJpZzd3T0p6dEo1MnZDMzFBN2FyNyJ9.eyJpc3MiOiJodHRwczovL2RvdWJsZS1oZWxpeHgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMGNmMTI2MmViMzAzMDAxOWM4NzFkYyIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTk3NjE1OTk1LCJleHAiOjE1OTc3MDIzOTUsImF6cCI6Imw2eW5nNUxGdEtaSUZaNkk1NmZnUHlKcWJmSjN5ZzhVIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGU6YmF5cyIsImRlbGV0ZTpiYXlzIiwiZGVsZXRlOmRyaW5rcyIsImdldDpiYXlzIiwiZ2V0OmRhdGEiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmJheXMiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.qmiqpwbCMeT2qyF5B-f5V26yWKLT96gCaDyH4Bb8Bp3y14Jq2mlso_aGYhSsFF49BZf8QszEHdqJZtLbgKocTBBVadxpcYaEfvcKAK4qUKthURBid6lYblIm5wRcuOy4NFldEAPNNDKIswbfzVIpKpxmIt4Q4vzWSbUe84_i_QM50-6dXEAIRmOTnl_JeuIMNt_f2FMGJsxlq7o7kfawarr_dKMICU5XO43Lxs41a13MNwR6EWcmmyiTRiJtosQSLIiu0WGHlc0706U6uJPDabBagDVA3FcQ_9cXYkb2K_ym-KM-1U7VBC_qe128KmTBgZKJ4gueRBrlFubs7zrS-g",
    "assistant_manager" : " Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJpZzd3T0p6dEo1MnZDMzFBN2FyNyJ9.eyJpc3MiOiJodHRwczovL2RvdWJsZS1oZWxpeHgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMGNmMWM3MmViMzAzMDAxOWM4NzFkZSIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTk3NjE2MDU2LCJleHAiOjE1OTc3MDI0NTYsImF6cCI6Imw2eW5nNUxGdEtaSUZaNkk1NmZnUHlKcWJmSjN5ZzhVIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YmF5cyIsImdldDpkYXRhIiwiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.cuxcKUelwasWXsy7q7TST7czRQV1CHXqtm2fQlfpHerw68ohOt236jEnSy1oBKtbviQJJMAAMdDirWaEP-9VX8pLAu03NGJC2fy0PFWGrKfPkIMXMD7nRfQfPi59vgJKsbbZASCBHy3m660lt-GpyGx1MyceokiCmlrfTKnoVlRISo0LQE4Q6wT_xVu9mpUMZGUXZNHOyO5QQRlHtCOzrz4FTfvi8F9MbkQxqQtTDsP4LsI7dabxxU2L3FwYrT-xJYOvFxwa4jHyVnk2nAY3EZAPMZ7xSGd0SxSwk5NbgbIvM5EfKS6D_mzimkVq3Q9bDR0c4y78Czl6P6NbQOeDrA"
}

database_setup = {
    "database_name" : "shoe_locate",
    "user_name" : "postgres",
    "password" : "1",
    "port" : "localhost:5432"
}

# auth0_config = {
#     "AUTH0_DOMAIN" : "",
#     "ALGORITHMS" : ["RS256"],
#     "API_AUDIENCE" : "image"
# }



jsonData= [{
	"bay": "1" ,
	"data" : [
 	{
        "section": "B"  ,
        "name":  "Work out plus" ,
        "style": "2759"  ,
        "row": "5"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/8f83e3f50e9848fe9999aaf101308ce3_9366/Workout_Plus_Shoes_White_2759_01_standard.jpg" 
	},
    {
        "section": "B"  ,
        "name":  "Club C 1985 TV" ,
        "style": "DV6434"  ,
        "row": "4"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/09a42ecf48904d0cb7c1aa8e016bae5f_9366/Club_C_1985_TV_Shoes_White_DV6434_01_standard.jpg" 
	},
    {
        "section": "B"  ,
        "name":  "RBK Fusium" ,
        "style": "9922"  ,
        "row": "3"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/821af0d430e045fbab4eab1300da40e2_9366/Fusion_Run_2_Shoes_White_EG9922_01_standard.jpg" 
	},
     {
        "section": "B"  ,
        "name":  "Legacy Lifter" ,
        "style": "FU7872"  ,
        "row": "1"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/47c766470b4c4ea5a838ab10016ff115_9366/Reebok_Legacy_Lifter_Flexweave(r)_Men's_Shoes_Black_FU7872_01_standard.jpg" 
	},
     {
        "section": "A"  ,
        "name":  "Work out plus black" ,
        "style": "2760"  ,
        "row": "5"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/ea362c8c7d084a479c48aaf801454fe8_9366/Workout_Plus_Shoes_Black_2760_01_standard.jpg" 
	},
    {
        "section": "A"  ,
        "name":  "Reebok Classic Slide" ,
        "style": "EH0667"  ,
        "row": "5"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "U" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/e50bbdbdca89459abeb8aafd0150d2ee_9366/Reebok_Classic_Slide_Black_EH0667_01_standard.jpg" 
	}

    ]
 },
{
	"bay": "2" ,
	"data" : [
 	{
        "section": "A"  ,
        "name":  "Classic Leather" ,
        "style": "9771"  ,
        "row": "5"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/a604d220136c496f9be3ab52010c5e38_9366/Classic_Leather_Men's_Shoes_White_9771_9771_01_standard.jpg" 
	},{
        "section": "A"  ,
        "name":  "Classic Leather" ,
        "style": "9771"  ,
        "row": "5"  ,
        "col": "2"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/a604d220136c496f9be3ab52010c5e38_9366/Classic_Leather_Men's_Shoes_White_9771_9771_01_standard.jpg" 
	},
    {
        "section": "A"  ,
        "name":  "Classic Leather Black" ,
        "style": "116"  ,
        "row": "4"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/cee2fbde7f3543f38c95ab6701799e4f_9366/Classic_Leather_Men's_Shoes_Black_116_01_standard.jpg" 
	},
    {
        "section": "A"  ,
        "name":  "Flash Film Train" ,
        "style": "FW2745"  ,
        "row": "3"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/699634c7eed247bebdc6ab26011c9767_9366/Flashfilm_Trainer_Men's_Training_Shoes_Black_FW2745_01_standard.jpg" 
	},
     {
        "section": "A"  ,
        "name":  "FloatRide Run 2.0" ,
        "style": "DV6771"  ,
        "row": "2"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/96ea3294a3cc4a7bafeeaa5e014e96fd_9366/Floatride_Run_2_Men's_Running_Shoes_Black_DV6771_01_standard.jpg" 
	},
     {
        "section": "A"  ,
        "name":  "Daytana DMX MU" ,
        "style": "FV6077"  ,
        "row": "1"  ,
        "col": "1"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_2000,f_auto,q_auto:sensitive,fl_lossy/094968f838db4245aa95ab3d01615cd6_9366/Daytona_DMX_x_GOK_Shoes_White_FV6077_01_standard.jpg" 
	},
    {
        "section": "A"  ,
        "name":  "Ex-o-Fit HI" ,
        "style": "3477"  ,
        "row": "4"  ,
        "col": "2"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/60cdf95300db45b28ffdaaf70109a03a_9366/EX_O_FIT_Hi_Men's_Shoes_White_3477_01_standard.jpg" 
	},
     {
        "section": "A"  ,
        "name":  "Pyro" ,
        "style": "DV7298"  ,
        "row": "3"  ,
        "col": "2"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/41889602c8674492b4a6aa78016b1f5b_9366/Pyro_Shoes_Grey_DV7298_01_standard.jpg" 
	},
     {
        "section": "A"  ,
        "name":  "Pyro" ,
        "style": "DV5640"  ,
        "row": "2"  ,
        "col": "2"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "" 
	}
    , {
        "section": "A"  ,
        "name":  "Club C 85 MU" ,
        "style": "EF3246"  ,
        "row": "1"  ,
        "col": "2"  ,
        "notes":  "" ,
        "gender":  "M" ,
        "img":  "https://assets.reebok.com/images/h_2000,f_auto,q_auto:sensitive,fl_lossy/c6985f64c8e044fcb9bfaadc01708696_9366/Club_C_85_Men's_Shoes_Blue_EF3246_01_standard.jpg" 
	}

    ]
 }
]
