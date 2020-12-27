version: '3'

services:
  web:
    restart: always
    build: ./web
    expose:
      - "8000"
    links:
      - postgres:postgres
      - mongodb:mongodb
    volumes:
      - web-data:/usr/src/app/static
    env_file: 
      - .env
    command: /usr/local/bin/gunicorn -w 2 -b :8000 app:app

  nginx:
    restart: always
    build: ./nginx
    ports:
      - "80:80"
    volumes:
      - .:/www/static
      - web-data:/usr/src/app/static
    links:
      - web:web

  data:
    image: postgres:latest
    volumes:
      - db-data:/var/lib/postgresql/data
    command: "true"

  postgres:
    restart: always
    image: postgres:latest
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    ports:
      - "5432:5432"

  mongodb:
    image: mongo:4.0.8
    restart: unless-stopped
    command: mongod --auth
    environment:
      MONGO_INITDB_ROOT_USERNAME: mongodbuser
      MONGO_INITDB_ROOT_PASSWORD: mdb_user
      MONGO_INITDB_DATABASE: edgedb
      MONGODB_DATA_DIR: /data/db
      MONDODB_LOG_DIR: /dev/null
    volumes:
      - mongodbdata:/data/db
    ports:
      - "27017:27017"
#    networks:
#      - backend

volumes:
  db-data:
  web-data:
  mongodbdata:
