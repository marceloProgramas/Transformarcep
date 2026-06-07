import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import GeoPoint

cred = credentials.Certificate("locais-das-tampinhas-firebase-adminsdk-fbsvc-50ddff0e8b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def salvar_local(name: str, endereco: str, latLong: list[float], horario: str, obs: str = ""):
    try:
        locais_ref = db.collection("locais")
        
        novo_local = {
            "name": name,
            "endereco": endereco,
            "LatLong": GeoPoint(latLong[0], latLong[1]),
            "horario": horario
        }
        
        if obs:
            novo_local["obs"] = obs
            
        doc_ref = locais_ref.add(novo_local)
        print(f"Sucesso! ID: {doc_ref[1].id}")
    except Exception as e:
        print(f"Erro: {e}")


