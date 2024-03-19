-- Script to create a MySQL server
-- Create database hbnb_test_db
-- Create the user if it doesn't exist
-- Grant privileges to the user on the database
-- Grant SELECT privilege on performance_schema

-- Create a cursor object to execute queries
cursor = db.cursor()

-- Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")

-- Create the user if it doesn't exist and set the password
cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'")

-- Grant all privileges on hbnb_test_db to hbnb_test
cursor.execute("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'")

-- Grant SELECT privilege on performance_schema to hbnb_test
cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'")

-- Flush privileges to apply the changes
cursor.execute("FLUSH PRIVILEGES")

-- Close the cursor and database connection
cursor.close()
db.close()
