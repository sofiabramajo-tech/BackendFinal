from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
from pydantic import BaseModel

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app =FastAPI()


@app.get("/health")
def obtener_salud_sitio():
    return "sofiaa"

class Usuario(BaseModel):
    nombre:str
    email:str
    edad:int
    contraseña:str
    repetir_contraseña:str
    
class Curso(BaseModel):
    nombre:str
    año: int
    division: int  
      

@app.get("/usuarios")
def obtener_usuarios():
    collection = db.collection("usuarios").stream()
    return [c.to_dict() for c in collection]

@app.post("/usuarios")
def crear_usuarios (usuario:Usuario):
    if usuario.contraseña != usuario.repetir_contraseña:
        return "Las contraseñas no coinciden"
    
    del usuario.repetir_contraseña
    db.collection("usuarios").add(usuario.dict())
    return "Usuario creado con exito"

@app.get("/cursos")
def obtener_cursos():
    collection = db.collection("cursos").stream()
    return [c.to_dict() for c in collection]

@app.post("/cursos")
def subir_curso (curso:Curso):
    if curso.nombre == "admin":
        return "Ese nombre no es válido"
    
    del curso.division 
    db.collection("cursos").add(curso.dict())
    return "Curso agregado"