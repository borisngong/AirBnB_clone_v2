-- Script to create a MySQL server
-- Create database hbnb_test_db
-- Create the user if it doesn't exist
-- Grant privileges to the user on the database
-- Grant SELECT privilege on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Apply changes immediately without needing to restart MySQL
FLUSH PRIVILEGES;