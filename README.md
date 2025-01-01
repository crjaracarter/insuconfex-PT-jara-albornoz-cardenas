# INSUCONFEX - Sistema de Gestión Web

E-commerce web desarrollado con Django Framework | Sistema web comercial

## 🔧 Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clonar el repositorio
```bash
git clone [[URL_DEL_REPOSITORIO](https://github.com/crjaracarter/insuconfex-PT-jara-albornoz-cardenas.git)]
cd INSUCONFEX
```

2. Crear y activar entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows
venv\Scripts\activate

# Activar entorno virtual en Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones
```bash
python manage.py migrate
```

5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

6. Iniciar servidor de desarrollo
```bash
python manage.py runserver
```

El sistema estará disponible en `http://127.0.0.1:8000/`

## 📦 Dependencias Principales

```
Django==4.0.4
django-crispy-forms==1.14.0
crispy-bootstrap4==2022.1
asgiref==3.5.2
sqlparse==0.4.2
tzdata==2022.1
whitenoise==6.4.0
gunicorn==20.1.0
```

## 🛠️ Tecnologías Utilizadas

- Django 4.0.4
- Bootstrap 4
- SQLite

## 📁 Estructura del Proyecto

```
INSUCONFEX/
├── media/
├── insucon/
├── INSUCONFEX/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 👥 Autores

- Ignacio
- Izan
- Cristian

## 📄 Licencia

Este proyecto está bajo la Licencia MIT LICENSE

---
⌨️ con ❤️ por Ignacio, Izan y Cristian
