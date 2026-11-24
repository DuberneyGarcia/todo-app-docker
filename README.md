Todo App Docker

Proyecto desarrollado con Flask y MySQL utilizando Docker y Docker Compose.

Tecnologías Utilizadas
Python 3.11
Flask
MySQL 8
Docker
Docker Compose
Git
GitHub
Estructura del Proyecto
todo-app
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .env
Construir y Ejecutar los Contenedores
Desde la carpeta del proyecto ejecutar:

docker compose up --build
Verificar que los Contenedores Están Activos
docker ps
Se deben visualizar:

todo-app-web-1
todo-app-db-1
Acceder a la Aplicación
Abrir el navegador en:

http://localhost:5000
Resultado esperado:

Conexion exitosa entre Flask y MySQL
Detener los Contenedores
docker compose down
Arquitectura
Usuario
   │
   ▼
Contenedor Flask
   │
   ▼
Contenedor MySQL
Repositorio GitHub
https://github.com/DuberneyGarcia/todo-app-docker

Autor
Duberney García Osorio

Proyecto académico para la asignatura Integración Continua.