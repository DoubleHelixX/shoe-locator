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