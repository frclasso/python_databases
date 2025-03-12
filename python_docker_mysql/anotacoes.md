# Build
docker-compose up --build


# connect to databse
docker exec -it mysql_container bash

# login
mysql -u testuser -p
mysql -u root -p

# DATABASES
SHOW DATABASES;

USE testdb;
SHOW TABLES;


# You can also connect to MySQL from your local machine using:
docker exec -it mysql_container mysql -u testuser -p testdb


# creating tables
docker exec -it python_app bash
cd /app
python createtables.py

or
docker exec -it python_app python /app/createtables.py


# 
docker ps -a
docker start python_app


# rebuild
docker-compose down
docker-compose up --build -d

