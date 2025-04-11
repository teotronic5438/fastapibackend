# 🚀 FastAPI - Primer Conexión  
> Alumno: **Elías Orihuela**

Este proyecto es una **práctica de clase** para realizar una primera conexión con FastAPI, usando Alembic como gestor de migraciones y SQLite como base de datos. El objetivo es aprender a levantar un servidor, estructurar una API básica y configurar el entorno correctamente.

---

## 🧠 ¿Qué vas a encontrar en este proyecto?

- 🟢 Una app básica de FastAPI (`main.py`)
- 🗂️ Estructura modular organizada
- 🧪 Base de datos SQLite lista para usar
- ⚙️ Alembic configurado para manejo de esquemas
- 📦 Instalación rápida con `requirements.txt`

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Git (opcional, para clonar el repo)

---

## 🛠️ Instrucciones para levantar la app

### 1. Clonar el repositorio

    git clone https://github.com/tuusuario/tu-repo.git
    cd tu-repo

### 2. Crear y activar el entorno virtual

    # creacion de entorno virtual
    python -m venv env  
    
    # en Windows
    .\env\Scripts\activate

    # en Mac / Linux
    source env/bin/activate

### 3. Instalar las dependencias

    pip install -r requirements.txt

### 4. Ejecutar las migraciones de Alembic (opcional si las incluís)

    alembic upgrade head

### 5. Levantar el servidor

    uvicorn app.main:app --reload
