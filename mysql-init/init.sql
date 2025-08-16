CREATE TABLE application (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(50),
    company VARCHAR(50),
    date DATE,
    status TINYINT,
    job_board VARCHAR(50)
);