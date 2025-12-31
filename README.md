# Spotify Music API 🎵

API desarrollada con Django y Django REST Framework para gestionar usuarios y sus preferencias musicales, integrando Spotify real para obtener top tracks automáticamente.  

Este proyecto me permitió aprender a integrar APIs externas, trabajar con tokens automáticos y manejar datos en JSON dentro de Django. 💚

---

## 📌 Descripción

El proyecto permite:

- Crear, listar, actualizar y eliminar usuarios.
- Crear preferencias musicales para cada usuario.
- Consultar artistas y sus top tracks directamente desde la API de Spotify.
- Guardar automáticamente las canciones principales (`top_tracks`) de cada artista en la base de datos al crear una preferencia.
- Consultar Spotify sin guardar en la base de datos para ver información en tiempo real.

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/nivapeca-art/spotify_music.git
cd spotify_music

## crear entono virtual
python -m venv venv
.\venv\Scripts\activate

## instalar dependencias
pip install -r requirements.txt

## Crear archivo .env con tus credenciales de Spotify
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret

## Ejecutar migraciones 
python manage.py makemigrations
python manage.py migrate

## correr el servidor
python manage.py runserver

---
## 🚀 Endpoints principales
#Usuarios
Endpoint	Método	Descripción
/api/users/	GET	Lista todos los usuarios
/api/users/	POST	Crear un usuario. Body: { "name": "Nicolle", "email": "nicolle@example.com" }
/api/users/<id>/	GET	Obtener un usuario específico
/api/users/<id>/	PUT	Actualizar un usuario
/api/users/<id>/	DELETE	Eliminar un usuario

#Preferencias musicales
Endpoint	Método	Descripción
/api/preferences/	GET	Lista todas las preferencias
/api/preferences/	POST	Crear una preferencia (solo user y artist). top_tracks se llena automáticamente desde Spotify
/api/preferences/<id>/	GET	Obtener una preferencia específica
/api/preferences/<id>/	PUT	Actualizar una preferencia
/api/preferences/<id>/	DELETE	Eliminar una preferencia

#Spotify real (sin guardar en DB)
Endpoint	Método	Descripción
/api/spotify/search/?artist=<nombre>	GET	Busca un artista en Spotify y devuelve su nombre y top tracks. Ejemplo: /api/spotify/search/?artist=Coldplay
---
##📂 Estructura del proyecto
bash
Copiar código
spotify_music/
│
├── spotify_api/        # App para integración con Spotify
│   ├── views.py
│   ├── urls.py
│
├── users/              # App para usuarios y preferencias
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── spotify_music/      # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
---
##📝 Conclusiones
¡Estoy muy contenta con este proyecto! 😄

Logré integrar Django REST Framework con la API real de Spotify para obtener top tracks automáticamente, esto fue un reto ya que no sabia muy bien como hacerlo pero me parecio interesante.

Pude crear un CRUD completo de usuarios y preferencias musicales.

Aprendí a manejar tokens automáticos de la API y a trabajar con JSON en Django.

Este proyecto es la base para futuras mejoras: filtros de artistas, autenticación de usuarios, integración con otras APIs musicales.

— Nicolle Perez 💚
---
##📌 Tecnologías usadas
Python 3.14

Django 6.0

Django REST Framework

SQLite

Requests (para llamadas a la API de Spotify)

python-dotenv (para manejar variables de entorno)













