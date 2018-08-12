import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

print default_app.name
