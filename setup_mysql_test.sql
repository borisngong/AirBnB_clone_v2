--Script to create a MySQL server
--    Create database hbnb_test_db
--    Create the user if it doesn't exist
--    Grant privileges to the user on the database
--    Grant SELECT privilege on performance_schema

CREATE DATABASE if NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'borodidier';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'borodidier';
-- We use FLUSH PRIVILEGES to apply changes immediately without neeeding to restart Mysql
FLUSH PRIVILEGES;
