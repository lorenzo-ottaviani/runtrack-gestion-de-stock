CREATE DATABASE store;

USE store;

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price INT NOT NULL,
    quantity INT,
    id_category INT NOT NULL,
    FOREIGN KEY (id_category) REFERENCES category(id)
);
