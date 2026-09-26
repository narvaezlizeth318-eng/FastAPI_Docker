from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="EV02 - narvaezlizeth318")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db_productos = []
db_usuarios = []

class Producto(BaseModel):
    id: int = None
    nombre: str
    precio: float
    stock: int = 0

class Usuario(BaseModel):
    id: int = None
    nombre: str
    email: str
    rol: str

@app.get("/")
def inicio():
    return {"mensaje": "API EV02 funcionando"}

@app.get("/productos")
def listar_productos():
    return db_productos

@app.post("/productos")
def crear_producto(p: Producto):
    p.id = len(db_productos)+1
    db_productos.append(p.dict())
    return p

@app.delete("/productos/{id_prod}")
def borrar_producto(id_prod: int):
    global db_productos
    db_productos = [x for x in db_productos if x['id'] != id_prod]
    return {"ok": True}

@app.get("/usuarios")
def listar_usuarios():
    return db_usuarios

@app.post("/usuarios")
def crear_usuario(u: Usuario):
    u.id = len(db_usuarios)+1
    db_usuarios.append(u.dict())
    return u

@app.delete("/usuarios/{id_user}")
def borrar_usuario(id_user: int):
    global db_usuarios
    db_usuarios = [x for x in db_usuarios if x['id'] != id_user]
    return {"ok": True}
