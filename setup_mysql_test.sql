-- Script to create a MySQL server
-- Create database hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user on the database

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply changes immediately without needing to restart MySQL

FLUSH PRIVILEGES;