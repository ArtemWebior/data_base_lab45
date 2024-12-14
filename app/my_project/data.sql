-- Створення бази даних
DROP DATABASE IF EXISTS lab4;
CREATE DATABASE IF NOT EXISTS lab4;
USE lab4;

CREATE TABLE Branch (
    id INT AUTO_INCREMENT PRIMARY KEY,
    branch_code VARCHAR(20) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    region VARCHAR(100),
    postal_code VARCHAR(20)
);

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    user_type ENUM('sender', 'receiver') NOT NULL
);

CREATE TABLE Courier (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    branch_id INT NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES Branch(id)
);

CREATE TABLE Operator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    branch_id INT NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES Branch(id)
);

CREATE TABLE Tariff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weight_limit FLOAT NOT NULL,
    price_per_kg FLOAT NOT NULL,
    region VARCHAR(100) NOT NULL
);

CREATE TABLE Parcel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tracking_number VARCHAR(20) NOT NULL UNIQUE,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    weight FLOAT NOT NULL,
    dimensions VARCHAR(50),
    status ENUM('created', 'in transit', 'delivered', 'returned') NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tariff_id INT NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES User(id),
    FOREIGN KEY (receiver_id) REFERENCES User(id),
    FOREIGN KEY (tariff_id) REFERENCES Tariff(id)
);

CREATE TABLE ParcelMovement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parcel_id INT NOT NULL,
    branch_id INT,
    courier_id INT,
    movement_date DATETIME NOT NULL,
    details TEXT,
    FOREIGN KEY (parcel_id) REFERENCES Parcel(id),
    FOREIGN KEY (branch_id) REFERENCES Branch(id),
    FOREIGN KEY (courier_id) REFERENCES Courier(id)
);

CREATE TABLE DeliverySchedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parcel_id INT NOT NULL UNIQUE,
    courier_id INT NOT NULL,
    delivery_date DATETIME NOT NULL,
    FOREIGN KEY (parcel_id) REFERENCES Parcel(id),
    FOREIGN KEY (courier_id) REFERENCES Courier(id)
);

CREATE TABLE Feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    parcel_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    feedback_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (parcel_id) REFERENCES Parcel(id)
);

CREATE TABLE Payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parcel_id INT NOT NULL,
    amount FLOAT NOT NULL,
    payment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('cash', 'card', 'online') NOT NULL,
    FOREIGN KEY (parcel_id) REFERENCES Parcel(id)
	);

CREATE INDEX idx_tracking_number ON Parcel (tracking_number); 
CREATE INDEX idx_movement_date ON ParcelMovement (movement_date); 
CREATE INDEX idx_delivery_date ON DeliverySchedule (delivery_date);


-- Branch table
INSERT INTO Branch (branch_code, address, city, region, postal_code) VALUES
('B001', '123 Main St', 'Kyiv', 'Kyiv Oblast', '01001'),
('B002', '456 Elm St', 'Lviv', 'Lviv Oblast', '79000'),
('B003', '789 Oak St', 'Odesa', 'Odesa Oblast', '65000'),
('B004', '321 Pine St', 'Dnipro', 'Dnipro Oblast', '49000'),
('B005', '654 Birch St', 'Kharkiv', 'Kharkiv Oblast', '61000'),
('B006', '987 Maple St', 'Zaporizhzhia', 'Zaporizhzhia Oblast', '69000');

-- User table
INSERT INTO User (full_name, phone_number, email, user_type) VALUES
('John Doe', '1234567890', 'john.doe@example.com', 'sender'),
('Jane Smith', '2345678901', 'jane.smith@example.com', 'receiver'),
('Alice Johnson', '3456789012', 'alice.johnson@example.com', 'sender'),
('Bob Brown', '4567890123', 'bob.brown@example.com', 'receiver'),
('Charlie White', '5678901234', 'charlie.white@example.com', 'sender'),
('Diana Black', '6789012345', 'diana.black@example.com', 'receiver');

-- Courier table
INSERT INTO Courier (full_name, phone_number, branch_id) VALUES
('Courier 1', '1234509876', 1),
('Courier 2', '2345609876', 2),
('Courier 3', '3456709876', 3),
('Courier 4', '4567809876', 4),
('Courier 5', '5678909876', 5),
('Courier 6', '6789009876', 6);

-- Operator table
INSERT INTO Operator (full_name, phone_number, branch_id) VALUES
('Operator 1', '1111111111', 1),
('Operator 2', '2222222222', 2),
('Operator 3', '3333333333', 3),
('Operator 4', '4444444444', 4),
('Operator 5', '5555555555', 5),
('Operator 6', '6666666666', 6);

-- Tariff table
INSERT INTO Tariff (weight_limit, price_per_kg, region) VALUES
(5.0, 10.0, 'Kyiv Oblast'),
(10.0, 8.0, 'Lviv Oblast'),
(15.0, 6.0, 'Odesa Oblast'),
(20.0, 5.0, 'Dnipro Oblast'),
(25.0, 4.0, 'Kharkiv Oblast'),
(30.0, 3.0, 'Zaporizhzhia Oblast');

-- Parcel table
INSERT INTO Parcel (tracking_number, sender_id, receiver_id, weight, dimensions, status, tariff_id) VALUES
('TRACK001', 1, 2, 4.5, '20x30x15', 'created', 1),
('TRACK002', 3, 4, 9.0, '25x35x20', 'in transit', 2),
('TRACK003', 5, 6, 12.0, '30x40x25', 'delivered', 3),
('TRACK004', 1, 6, 18.0, '35x45x30', 'returned', 4),
('TRACK005', 3, 2, 22.5, '40x50x35', 'created', 5),
('TRACK006', 5, 4, 28.0, '45x55x40', 'in transit', 6);

-- ParcelMovement table
INSERT INTO ParcelMovement (parcel_id, branch_id, courier_id, movement_date, details) VALUES
(1, 1, 1, '2024-02-25 20:11:35', 'Received at branch'),
(2, 2, 2, '2024-01-22 20:11:35', 'In transit to destination'),
(3, 3, 3, '2024-04-09 20:11:35', 'Delivered to receiver'),
(4, 4, 4, '2024-04-12 20:11:35', 'Returned to sender'),
(5, 5, 5, '2024-02-23 20:11:35', 'Arrived at sorting center'),
(6, 6, 6, '2024-01-03 20:11:35', 'Out for delivery');

-- DeliverySchedule table
INSERT INTO DeliverySchedule (parcel_id, courier_id, delivery_date) VALUES
(1, 1, '2024-05-12 20:11:35'),
(2, 2, '2024-11-13 20:11:35'),
(3, 3, '2024-05-10 20:11:35'),
(4, 4, '2024-01-21 20:11:35'),
(5, 5, '2024-11-02 20:11:35'),
(6, 6, '2024-08-20 20:11:35');

-- Feedback table
INSERT INTO Feedback (user_id, parcel_id, rating, comment, feedback_date) VALUES
(1, 1, 5, 'Excellent service', '2024-10-16 20:11:35'),
(2, 2, 4, 'Good experience', '2024-07-06 20:11:35'),
(3, 3, 3, 'Average service', '2023-12-14 20:11:35'),
(4, 4, 2, 'Below expectations', '2024-04-26 20:11:35'),
(5, 5, 1, 'Poor experience', '2024-11-24 20:11:35'),
(6, 6, 5, 'Great delivery!', '2024-06-01 20:11:35');

-- Payment table
INSERT INTO Payment (parcel_id, amount, payment_date, payment_method) VALUES
(1, 50.0, '2024-03-21 20:11:35', 'cash'),
(2, 80.0, '2024-09-28 20:11:35', 'card'),
(3, 100.0, '2024-06-20 20:11:35', 'online'),
(4, 70.0, '2024-09-29 20:11:35', 'cash'),
(5, 110.0, '2024-07-08 20:11:35', 'card'),
(6, 90.0, '2024-01-27 20:11:35', 'online');


-- lab4 
SELECT 
    Branch.city AS branch_city, 
    Courier.full_name AS courier_name
FROM 
    Branch
LEFT JOIN 
    Courier ON Branch.id = Courier.branch_id
ORDER BY 
    Branch.city, Courier.full_name;
    
SELECT 
    Parcel.tracking_number AS parcel_tracking_number,
    Courier.full_name AS courier_name
FROM 
    ParcelMovement
JOIN 
    Parcel ON ParcelMovement.parcel_id = Parcel.id
JOIN 
    Courier ON ParcelMovement.courier_id = Courier.id
ORDER BY 
    Parcel.tracking_number, Courier.full_name;
    
    
-- lab 5 
CREATE TABLE BranchReview (
    id INT AUTO_INCREMENT PRIMARY KEY,
    branch_code VARCHAR(20) NOT NULL,
    review_text TEXT NOT NULL,
    review_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE TRIGGER BeforeInsertBranchReview
BEFORE INSERT ON BranchReview
FOR EACH ROW
BEGIN
    DECLARE branch_exists INT;

    -- Перевірка існування branch_code у таблиці Branch
    SELECT COUNT(*) INTO branch_exists
    FROM Branch
    WHERE branch_code = NEW.branch_code;

    -- Якщо branch_code не існує, викликати помилку
    IF branch_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Branch code does not exist in Branch table';
    END IF;
END $$

DELIMITER ;

INSERT INTO BranchReview (branch_code, review_text)
VALUES ('B000', 'Excellent service!');
DROP TRIGGER IF EXISTS BeforeInsertBranchReview;
SELECT * FROM BranchReview;


-- параментризована вставка
DELIMITER $$

CREATE PROCEDURE InsertIntoSpecifiedTable(
    IN table_name VARCHAR(64),
    IN columns TEXT,
    IN value_list TEXT
)
BEGIN
    SET @query = CONCAT('INSERT INTO ', table_name, ' (', columns, ') VALUES (', value_list, ')');
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$

DELIMITER ;

SHOW PROCEDURE STATUS WHERE Db = 'lab4';

DROP PROCEDURE InsertIntoSpecifiedTable;

CALL InsertIntoSpecifiedTable(
    'Branch', 
    'branch_code, address, city, region, postal_code', 
    "'BR123', '123 Main St', 'Kyiv', 'Kyiv Region', '01001'"
);

CREATE TABLE TestTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);


DELIMITER $$

CREATE PROCEDURE InsertNonameRows(
    IN table_name VARCHAR(64),
    IN column_name VARCHAR(64),
    IN start_number INT
)
BEGIN
    DECLARE i INT DEFAULT 0;

    WHILE i < 10 DO
        SET @row_value = CONCAT('Noname', start_number + i);
        SET @query = CONCAT('INSERT INTO ', table_name, ' (', column_name, ') VALUES (''', @row_value, ''')');
        
        -- Виконання динамічного SQL-запиту
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
        
        SET i = i + 1; -- Збільшення лічильника
    END WHILE;
END $$

DELIMITER ;

CALL InsertNonameRows('TestTable', 'name', 5);
DROP TABLE TestTable;


DELIMITER //

CREATE FUNCTION GetTotalRecords()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_count INT DEFAULT 0;

    -- Підрахунок записів для кожної таблиці
    SELECT 
        (SELECT COUNT(*) FROM Branch) +
        (SELECT COUNT(*) FROM User) +
        (SELECT COUNT(*) FROM Courier) +
        (SELECT COUNT(*) FROM Operator) +
        (SELECT COUNT(*) FROM Tariff) +
        (SELECT COUNT(*) FROM Parcel) +
        (SELECT COUNT(*) FROM ParcelMovement) +
        (SELECT COUNT(*) FROM DeliverySchedule) +
        (SELECT COUNT(*) FROM Feedback) +
        (SELECT COUNT(*) FROM Payment)
    INTO total_count;

    RETURN total_count;
END;
//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAndPrintTotalRecords()
BEGIN
    DECLARE total INT;
    SET total = GetTotalRecords();
    SELECT CONCAT('Total number of records in all tables: ', total) AS result;
END;
//

DELIMITER ;


-- курсор


DELIMITER //

CREATE PROCEDURE CreateDynamicDatabases()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE db_name VARCHAR(100);
    DECLARE table_count INT;
    DECLARE table_name VARCHAR(100);
    DECLARE cur CURSOR FOR SELECT DISTINCT city FROM Branch; -- Взяти унікальні значення зі стовпця `city`.
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO db_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Створення бази даних
        SET @create_db = CONCAT('CREATE DATABASE IF NOT EXISTS `', db_name, '_DB`');
        PREPARE stmt_db FROM @create_db;
        EXECUTE stmt_db;
        DEALLOCATE PREPARE stmt_db;

        -- Випадкова кількість таблиць (від 1 до 9)
        SET table_count = FLOOR(1 + (RAND() * 9));

        WHILE table_count > 0 DO
            -- Генерація назви таблиці
            SET table_name = CONCAT(db_name, '_Table_', table_count);

            -- Динамічний SQL для створення таблиці в конкретній базі
            SET @create_table = CONCAT(
                'CREATE TABLE `', db_name, '_DB`.`', table_name, '` (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    col1 VARCHAR(50),
                    col2 INT,
                    col3 DATE
                )'
            );
            PREPARE stmt_table FROM @create_table;
            EXECUTE stmt_table;
            DEALLOCATE PREPARE stmt_table;

            SET table_count = table_count - 1;
        END WHILE;
    END LOOP;

    CLOSE cur;
END;
//

DELIMITER ;


CALL CreateDynamicDatabases();

DELIMITER $$

CREATE TRIGGER branch_no_double_zero 
BEFORE INSERT ON Branch
FOR EACH ROW
BEGIN
    IF NEW.branch_code LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'branch_code cannot end with two zeros';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER branch_no_double_zero_update 
BEFORE UPDATE ON Branch
FOR EACH ROW
BEGIN
    IF NEW.branch_code LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'branch_code cannot end with two zeros';
    END IF;
END $$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER branch_no_update
BEFORE UPDATE ON Branch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Updating data in Branch table is not allowed';
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER branch_no_delete
BEFORE DELETE ON Branch
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting rows from Branch table is not allowed';
END $$

DELIMITER ;

INSERT INTO Branch (branch_code, address, city, region, postal_code) 
VALUES ('BR100', '123 Main St', 'Kyiv', 'Kyiv Region', '01001');

UPDATE Branch 
SET address = '456 New St'
WHERE id = 1;

DELETE FROM Branch WHERE id = 1;






