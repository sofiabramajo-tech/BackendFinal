<div>
  <img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=100&section=header&reversal=false&text=BACKEND%20FINAL&fontSize=70&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&descSize=20&descAlign=50&descAlignY=50&color=gradient"  />
</div>

###

<p align="left">Para este proyecto BACKEND usamos FastAPI, base de datos Firebase, Pydantic, entorno virtual (venv), Github y .gitignore</p>

###

<p align="left">Archivo main.py<br><br>from fastapi import FastAPI<br>import firebase_admin<br>from firebase_admin import credentials, firestore<br>from pydantic import BaseModel<br>(Importamos libreria FastAPI, Firestore y BaseModel)<br><br>cred = credentials.Certificate("firebase.json")<br>firebase_admin.initialize_app(cred)<br>db = firestore.client()<br>(Cargamos el archivo de credenciales JSON) <br><br>app =FastAPI()<br>(aplicación FastAPI)<br><br>@app.get("/health")<br>def obtener_salud_sitio():<br>    return "sofiaa"<br>(Prueba get para verificar que el servidor está funcionando)<br><br>class Usuario(BaseModel):<br>    nombre:str<br>    email:str<br>    edad:int<br>    contraseña:str<br>    repetir_contraseña:str<br>(Datos que solicita para crear el usuario)</p>

###

<p align="left">class Curso(BaseModel):<br>    nombre:str<br>    año: int<br>    division: int  <br>(Datos que solicita para crear el curso)<br><br>@app.get("/usuarios")<br>def obtener_usuarios():<br>    collection = db.collection("usuarios").stream()<br>    return [c.to_dict() for c in collection]<br>(Usamos ruta get para obtener lista de usuarios)<br><br>@app.post("/usuarios")<br>def crear_usuarios (usuario:Usuario):<br>(Ruta post para subir usuario) <br>   <br>if usuario.contraseña != usuario.repetir_contraseña:<br>        return "Las contraseñas no coinciden"<br>    del usuario.repetir_contraseña<br>db.collection("usuarios").add(usuario.dict())<br>    return "Usuario creado con exito"<br>(Verificamos que las contraseñas coincidan)</p>

###

<p align="left">@app.get("/cursos")<br>def obtener_cursos():<br>    collection = db.collection("cursos").stream()<br>    return [c.to_dict() for c in collection]<br>(Obtener cursos)<br><br>@app.post("/cursos")<br>def subir_curso (curso:Curso):<br>    if curso.nombre == "admin":<br>        return "Ese nombre no es válido"<br>    del curso.division <br>db.collection("cursos").add(curso.dict())<br>    return "Curso agregado"<br>(Ruta post para publicar curso y verificacion con "if" de que el nombre del curso sea válido)<br><br><br>Archivo .gitignore<br><br>venv<br>firebase.json<br>(Este archivo le dice a Git qué carpetas o archivos no debe subir a GitHub)</p>

###
