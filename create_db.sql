CREATE DATABASE employeedb;
USE employeedb;
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    post VARCHAR(50),
    salary FLOAT
);
