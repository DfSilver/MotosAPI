# 🏍️ Motorcycles API - Flask + SQLite + JWT

API REST desarrollada en **Flask** que gestiona motocicletas y usuarios con autenticación **JWT** y control de **roles (admin / user)**.  
Proyecto estructurado por módulos, con separación entre controladores, servicios y modelos.

---

## 🚀 Tecnologías
- Python 3.11+
- Flask
- SQLAlchemy
- SQLite
- PyJWT
- Werkzeug (para hashing de contraseñas)

---

## 🧩 Estructura del Proyecto
📦 project/
┣ 📂 config/
┃ ┗ database.py
┣ 📂 controllers/
┃ ┣ auth_controller.py
┃ ┗ motorcycle_controller.py
┣ 📂 models/
┃ ┗ user_model.py
┣ 📂 services/
┃ ┣ auth_service.py
┃ ┗ motorcycle_service.py
┣ 📂 utils/
┃ ┗ jwt_utils.py
┣ main.py
┗ requirements.txt

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/motorcycles-api.git
cd motorcycles-api

2️⃣ Crear entorno virtual
bash
Copiar código
python -m venv venv
source venv/bin/activate  # (Linux / macOS)
venv\Scripts\activate     # (Windows)

3️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt

4️⃣ Ejecutar el servidor
bash
python main.py
El servidor iniciará en:
👉 http://127.0.0.1:5000

🧠 Endpoints
🔐 Autenticación

1. Registro

bash
POST /register
Content-Type: application/json

{
  "email": "admin@example.com",
  "password": "123456",
  "role": "admin"
}
📤 Respuesta:

json
{
  "id": 1,
  "email": "admin@example.com",
  "role": "admin"
}

2. Login
bash
POST /login
Content-Type: application/json

{
  "email": "admin@example.com",
  "password": "123456"
}
📤 Respuesta:

json
{ "token": "JWT_GENERADO_AQUI" }

🏍️ Motocicletas
Todas las rutas (excepto /tabla y /seed) requieren autenticación JWT.

##listar motocicletaS

bash
GET /motorcycles
Authorization: Bearer TU_TOKEN
Crear motocicleta
bash
POST /motorcycles
Authorization: Bearer TU_TOKEN
Content-Type: application/json

{
  "brand": "Yamaha",
  "reference": "MT-07"
}

## Actualizar motocicleta

bash
PUT /motorcycles/1
Authorization: Bearer TU_TOKEN
Content-Type: application/json

{
  "brand": "Honda",
  "reference": "CB500F"
}

## Eliminar motocicleta (solo user)

bash
DELETE /motorcycles/1
Authorization: Bearer TU_TOKEN_ADMIN
Ver tabla HTML
bash
GET /motorcycles/tabla

## Cargar datos de ejemplo
bash
POST /motorcycles/seed
🔑 Roles y Autorización
Rol	Permisos
admin	CRUD completo (crear, actualizar, eliminar motos)
user	Solo listar y ver motos

Las rutas protegidas usan los decoradores:

python
@token_required
@role_required(["admin"])
🧱 Commits Realizados
#	Tipo	Descripción
1️⃣	init	Estructura base del proyecto
2️⃣	feat	CRUD de motocicletas con SQLite
3️⃣	feat	Endpoint /motorcycles/tabla (vista HTML)
4️⃣	feat	Autenticación JWT (login / register)
5️⃣	feat	Autorización por roles y protección de rutas

🧪 Pruebas rápidas con cURL

## Crear usuario admin
bash
curl -X POST http://127.0.0.1:5000/register \
 -H "Content-Type: application/json" \
 -d '{"email":"admin@example.com","password":"123456","role":"admin"}'

## Obtener token
bash
curl -X POST http://127.0.0.1:5000/login \
 -H "Content-Type: application/json" \
 -d '{"email":"admin@example.com","password":"123456"}'

## Eliminar moto (solo admin)
bash
curl -X DELETE http://127.0.0.1:5000/motorcycles/1 \
 -H "Authorization: Bearer TU_TOKEN_ADMIN"


👨‍💻 Autor
Daniel Moreno
Desarrollado como parte de un proyecto académico de desarrollo backend con Flask.