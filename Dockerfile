# Imagen base liviana de Python
FROM python:3.10-slim

# Variables de entorno necesarias
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libaio1 \
    curl \
    unzip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear y establecer directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . .

# Descargar e instalar Oracle Instant Client (Lite)
RUN curl -O https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip && \
    unzip instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip -d /opt/oracle && \
    rm instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip && \
    ln -s /opt/oracle/instantclient_21_11 /opt/oracle/instantclient

# Variables de entorno para Oracle
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV TNS_ADMIN=/app/wallet  # ruta donde debes colocar tu wallet en el proyecto

# Instalar dependencias Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ejecutar migraciones y levantar el servidor en producción con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
