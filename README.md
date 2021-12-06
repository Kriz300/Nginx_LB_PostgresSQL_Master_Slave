# En Desarrollo
Proyecto integrando una API REST con Flask, un Balanceador de cargar utilizando Nginx y realizando una réplica de base de datos con PostgresSQL y Docker
## Ejecución y Comandos 🔧

Instalar [Docker](https://help.wnpower.com/hc/es/articles/360048910771-Cómo-instalar-Docker-en-tu-servidor-con-Ubuntu)
Instalar [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04-es)

### Ejecución Réplica de PostgresSQL
Master.
```
sudo docker run -dti -p 55432:5432 --name postgresql-master \
  -e POSTGRESQL_REPLICATION_MODE=master \
  -e POSTGRESQL_USERNAME=user1 \
  -e POSTGRESQL_PASSWORD=password1 \
  -e POSTGRESQL_DATABASE=my_database \
  -e POSTGRESQL_REPLICATION_USER=user2 \
  -e POSTGRESQL_REPLICATION_PASSWORD=password2 \
  bitnami/postgresql:latest
```
Slave.
```
docker run -dti -p 65432:5432 --name postgresql-slave \
  --link postgresql-master:master \
  -e POSTGRESQL_REPLICATION_MODE=slave \
  -e POSTGRESQL_USERNAME=user3 \
  -e POSTGRESQL_PASSWORD=password3 \
  -e POSTGRESQL_MASTER_HOST=master \
  -e POSTGRESQL_MASTER_PORT_NUMBER=5432 \
  -e POSTGRESQL_REPLICATION_USER=user2 \
  -e POSTGRESQL_REPLICATION_PASSWORD=password2 \
  bitnami/postgresql:latest
```
Creación de Tabla de inventario.
```
create table product
(
    id serial primary key, 
    name varchar, 
    price int
);
```
Ejecucion de Flask.
```
python3 -m flask run --port [portnumber]
```
## Estructura 🛠️

### Construido con:

* **Nginx**
* **Python**
* **Flask**
* **PostgresSQL**
* **Docker**



## Autores ✒️

* **Christian Muñoz I.** [Kriz](https://github.com/Kriz300)
* **Camilo Rubilar** [Niyet](https://github.com/niyetsin)
* **Raimundo Perez** [Raimundo Perez](https://github.com/raimundoperez8)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.
