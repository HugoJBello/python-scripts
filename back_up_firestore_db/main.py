#pip3 install --upgrade google-cloud-firestore
#pip3 install firebase_admin
from entries_firebase_dao import EntriesFirebaseDAO 

def main():
    entries_firebase_dao = EntriesFirebaseDAO()
    entries_firebase_dao.save_db()
if __name__ == '__main__':
	main()