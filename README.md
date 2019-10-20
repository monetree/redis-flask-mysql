# Steps to run this app locally


1. install redis (`https://redis.io/`)
2. install mysql
3. create database with named `dummy` in mongodb
4. `mysqldump -u username -p databasename tableName > user.sql` to import mysql
5. install requiremets using `pip install -r requirements.txt` (You can use virtualenv also as i am using)
6. run `python app.py` in current directory
7. in browser run `http://127.0.0.1:5000/stores`

As django support ORM query we don't have to change our code doesn't matter whatever database we use.
I have added comments properly for each use cases and both db connection and how to use it for the codes.

Here i have used `Flask-MongoAlchemy` for databse query and `redis` client for caching
