import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from models import *

cred=credentials.Certificate("./BackEnd/ServiceAccountKey.json")
app=firebase_admin.initialize_app(cred)
db=firestore.client(app)

def add_prodotto(nome:str):
    db.collection("prodotti").document(nome).set({"nome":nome})

def get_prodotti():
    prodotti=[]
    for prodotto in db.collection("prodotti").stream():
        prodotti+=[prodotto.to_dict()]
        # prodotti.append(prodotti.to_dict())
    return prodotti