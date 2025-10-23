# Laboratorio de Microservicios# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
* **auth-service/**: Autenticación y tokens JWT
* **blog-service/**: Publicaciones, autores y categorías
* **email-service/**: Notificaciones y formularios
* **frontend/**: Interfaz React
* **reverse-proxy/**: Balanceo / Gateway local

### Servicios base:
* PostgreSQL (5432)
* Redis (6379)

## Checklist - Entregables Día 1
* [ ] Repo Git subido a GitHub con estructura base y `.env.example`
* [ ] Docker Compose levanta PostgreSQL y Redis sin errores
* [ ] README documentado (incluye arquitectura y checklist)
* [ ] Captura o video corto mostrando los contenedores en ejecución (`docker ps`)