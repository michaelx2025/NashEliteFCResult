import json
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

app = firebase_admin.initialize_app()

cred = credentials.Certificate("./account.json")
firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection()

