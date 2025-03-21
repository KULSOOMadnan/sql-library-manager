CREATE DATABASE IF NOT EXISTS library_db;

USE library_db;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INT,
    genre VARCHAR(100),
    read_status BOOLEAN
);
