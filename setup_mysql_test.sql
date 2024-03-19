-- Script that prepares a MySQL Test server for the project.
--    creates a Database hbnb_test_db.
--    creates a User hbnb_test with password hbnb_test_pwd in local host
--    Grants all privileges for hbnb_test on hbnb_test_db.
--    Grants SELECT privilege for hbnb_test on performance_schema.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';