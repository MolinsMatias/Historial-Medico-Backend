
FROM python:3.10-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install -y \
    libaio1 \
    curl \
    unzip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . .

RUN curl -O https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip && \
    unzip instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip -d /opt/oracle && \
    rm instantclient-basiclite-linux.x64-21.11.0.0.0dbru.zip && \
    ln -s /opt/oracle/instantclient_21_11 /opt/oracle/instantclient

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV TNS_ADMIN=/app/wallet  # ruta donde debes colocar tu wallet en el proyecto


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
