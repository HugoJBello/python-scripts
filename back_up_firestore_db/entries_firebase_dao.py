from google.cloud import firestore
import google.cloud.exceptions
from firebase_admin import credentials
from firebase_admin import firestore 
from mongodb_data_recorder import MongoDBDataRecorder
import firebase_admin

class EntriesFirebaseDAO:

    def __init__(self):
        self.collection_name="entries-pod3c"
        cred = credentials.Certificate("podemos3cantos-firebase-adminsdk-cthls-6a90ff6ec6.json")
        firebase_admin.initialize_app(cred, {
        'projectId': 'podemos3cantos',
        'apiKey': 'AIzaSyC5Zs6etNV_7LbbnKK7rg7XtnP2f0VfaK0',
        'authDomain': 'podemos3cantos.firebaseapp.com',
        'databaseURL': 'https://podemos3cantos.firebaseio.com',
        'storageBucket': 'podemos3cantos.appspot.com',
        'messagingSenderId': '985731376808'
        })

        self.db = firestore.client()
        self.save_db()
    
    def save_db(self):
        entries_ref = self.db.collection(self.collection_name)
        mongoDBDataRecorder=MongoDBDataRecorder() 
        docs = entries_ref.get()
        for doc in docs:
            mongoDBDataRecorder.post_data(doc.to_dict())
        