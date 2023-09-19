-- prepares a MySQL server for test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_db'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test_db'@'localhost';
FLUSH PRIVILEGES;