SHOW DATABASES;
DROP DATABASE IF EXISTS Electricity_db;
CREATE DATABASE IF NOT EXISTS Electricity_db;
USE Electricity_db;

-- table structure for customer
DROP TABLE IF EXISTS customer;

CREATE TABLE customer 
(
cust_id INT AUTO_INCREMENT,
name VARCHAR(255) NOT NULL, 
address VARCHAR(255) NOT NULL,
city VARCHAR(255) NOT NULL,
state VARCHAR(255) NOT NULL,
PRIMARY KEY (cust_id)
);

-- inserting values into customer table
INSERT INTO customer (cust_id,name,address,city,state) VALUES ('100','Abhay','MG Road','Mysore','Karnataka');
INSERT INTO customer (name,address,city,state) VALUES ('Vishnu','Basaveshwara Nagar','Bangalore','Karnataka');
INSERT INTO customer (name,address,city,state) VALUES ('Anant','HD Kote Road','Mysore','Karnataka');
INSERT INTO customer (name,address,city,state) VALUES ('Vijay','KRS Road','Pune','Maharashtra');
INSERT INTO customer (name,address,city,state) VALUES ('Deekshith','RK Block','Chennai','Tamil Nadu');
INSERT INTO customer (name,address,city,state) VALUES ('Farhaan','Auromira','Ahmedabad','Gujarat');
INSERT INTO customer (name,address,city,state) VALUES ('Ajay','Pamban Bridge Road','Rameshwaram','Tamil Nadu');
INSERT INTO customer (name,address,city,state) VALUES ('Nikhil','HSR Layout','Bangalore','Karnataka');
INSERT INTO customer (name,address,city,state) VALUES ('Tushar','MS Raod','Lucknow','Uttar Pradesh');
INSERT INTO customer (name,address,city,state) VALUES ('Ayushman','Kanakapura Road','Bangalore','Karnataka');
INSERT INTO customer (name,address,city,state) VALUES ('Rohanjit','Bandra','Mumbai','Maharashtra');
INSERT INTO customer (name,address,city,state) VALUES ('Anwesh','DFG Layout','Indore','Madhya Pradesh');
INSERT INTO customer (name,address,city,state) VALUES ('Devash','Edapalli','Kochi','Kerala');
INSERT INTO customer (name,address,city,state) VALUES ('Preetham','AB Block','Ayodhya','Uttar Pradesh');
INSERT INTO customer (name,address,city,state) VALUES ('Sridhar','Gwalior Road','Gwalior','Madhya Pradesh');
INSERT INTO customer (name,address,city,state) VALUES ('Sahil','MG Road','New Delhi','Delhi');


-- table structure for admin
DROP TABLE IF EXISTS admin;
CREATE TABLE admin
(
admin_id INT AUTO_INCREMENT NOT NULL,
name VARCHAR(255) NOT NULL,
customer_id INT NOT NULL,
PRIMARY KEY (admin_id),
FOREIGN KEY (customer_id) REFERENCES customer(cust_id)
);

-- inserting values into admin table
INSERT INTO admin (admin_id, name,customer_id) VALUES ('200','Sahil','100');
INSERT INTO admin (name,customer_id) VALUES ('Karan','101');
INSERT INTO admin (name,customer_id) VALUES ('Rahul','102');
INSERT INTO admin (name,customer_id) VALUES ('Nikhil','103');


-- table structure for electricity board
DROP TABLE IF EXISTS electricity_board;
CREATE TABLE electricity_board
(
eb_id INT AUTO_INCREMENT NOT NULL,
name VARCHAR(255) NOT NULL,
state VARCHAR(255)  NOT NULL,
city VARCHAR(255) NOT NULL,
PRIMARY KEY (eb_id)
);

-- inserting values into electricity board table
INSERT INTO electricity_board (eb_id,name,state,city) VALUES ('300','Chamundeshwari Power Corporation','Karnataka','Mysore');
INSERT INTO electricity_board (name,state,city) VALUES ('Karnataka Power Corporation','Karnataka','Bangalore');
INSERT INTO electricity_board (name,state,city) VALUES ('BESCOM','Karnataka','Bangalore');
INSERT INTO electricity_board (name,state,city) VALUES ('Tamil Nadu Power Corporation','Tamil Nadu','Chennai');
INSERT INTO electricity_board (name,state,city) VALUES ('Uttar Pradesh Power Corporation','Uttar Pradesh','Lucknow');
INSERT INTO electricity_board (name,state,city) VALUES ('Madhya Pradesh Power Corporation','Madhya Pradesh','Indore');


-- table structure for tariff
DROP TABLE IF EXISTS tariff;
CREATE TABLE tariff
(
tariff_id INT AUTO_INCREMENT NOT NULL,
tariff_type VARCHAR(255) NOT NULL,
tariff_cost INT NOT NULL,
PRIMARY KEY (tariff_id),
CONSTRAINT test_column_positive CHECK (tariff_cost > 0)
);

-- inserting values into tariff table
INSERT INTO tariff (tariff_id,tariff_type,tariff_cost) VALUES ('400','Power factor tariff','10');
INSERT INTO tariff (tariff_type,tariff_cost) VALUES ('Peak Load tariff','40');
INSERT INTO tariff (tariff_type,tariff_cost) VALUES ('Two part tariff','18');
INSERT INTO tariff (tariff_type,tariff_cost) VALUES ('Three part tariff','36');


-- table structure for bill
DROP TABLE IF EXISTS bill;
CREATE TABLE bill
(
bill_id INT AUTO_INCREMENT NOT NULL,
board_id INT NOT NULL,
cust_id INT NOT NULL,
meter_no VARCHAR(255) NOT NULL,
units INT NOT NULL,
cost_per_unit INT NOT NULL ,
amount INT NOT NULL,
due_date DATE NOT NULL,
PRIMARY KEY (bill_id),
FOREIGN KEY (board_id) REFERENCES electricity_board(eb_id),
FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
CONSTRAINT amount_per_unit_positive CHECK (cost_per_unit > 0),
CONSTRAINT monthly_units_positive CHECK (units > 0),
CONSTRAINT total_amount_positive CHECK (amount > 0)
);

-- inserting values into bill table
INSERT INTO bill (bill_id,board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('500','300','100','37713','105','10','1050','2023-06-30');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('301','101','22849','187','18','3366','2023-12-16');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('303','102','94853','23','15','345','2023-11-09');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('302','103','36274','43','22','946','2023-10-12');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('303','104','47232','57','28','1596','2023-09-15');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('301','105','12975','67','33','2211','2023-08-18');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('302','106','98985','78','39','3042','2023-12-21');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('303','107','12753','89','44','3920','2023-11-24');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('304','108','75535','98','49','4802','2023-10-27');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('305','109','15821','108','54','5832','2023-09-30');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('300','110','87515','118','59','6962','2024-01-03');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('301','111','95435','128','64','8192','2023-12-06');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('302','112','39839','138','69','9522','2023-11-29');
INSERT INTO bill (board_id,cust_id,meter_no,units,cost_per_unit,amount,due_date) VALUES ('303','113','77378','148','74','10952','2023-11-22');

-- query to find the total amount in each city
SELECT c.city, SUM(b.units) AS total_monthly_units
FROM customer c
JOIN bill b ON c.cust_id = b.cust_id
GROUP BY c.city;

-- query to find the total amount in each state
SELECT c.state, SUM(b.units) AS total_monthly_units
FROM customer c
JOIN bill b ON c.cust_id = b.cust_id
GROUP BY c.state;

-- query to find amount collected by each board
SELECT eb.eb_id, eb.name, SUM(b.amount) AS total_bill_amount
FROM electricity_board eb
JOIN bill b ON eb.eb_id = b.board_id
GROUP BY eb.eb_id, eb.name;

-- query to update the address of a customer
-- UPDATE customer
-- SET address = 'New Address'
-- WHERE cust_id = 101;

-- query to delete a customer
-- DELETE FROM customer
-- WHERE cust_id = 101;

-- correlated query to find customers with bill amount greater than average bill amount for their city
SELECT c.*, b.units
FROM customer c
JOIN bill b ON c.cust_id = b.cust_id
WHERE b.units > (
    SELECT AVG(b2.units)
    FROM bill b2
    JOIN customer c2 ON c2.cust_id = b2.cust_id
    WHERE c2.city = c.city
);

-- nested query to find customer with highest bill amount
SELECT cust_id, name, address, city, state
FROM customer
WHERE cust_id = (
    SELECT cust_id
    FROM bill
    GROUP BY cust_id
    ORDER BY SUM(amount) DESC
    LIMIT 1
);

-- function to find average monthly units for a city
DELIMITER //
CREATE FUNCTION GetAverageMonthlyUnitsForCity(cityNameParam VARCHAR(255))
RETURNS DECIMAL(10, 2)
READS SQL DATA
BEGIN
    DECLARE avgMonthlyUnits DECIMAL(10, 2);
    SELECT AVG(b.units) INTO avgMonthlyUnits
    FROM bill b
    JOIN customer c ON b.cust_id = c.cust_id
    WHERE c.city = cityNameParam;
    RETURN avgMonthlyUnits;
END //
DELIMITER ;

-- procedure to find bill details for a customer
DELIMITER //
CREATE PROCEDURE GetBillDetailsByCustomerID(IN custID INT)
BEGIN
    SELECT * FROM bill WHERE cust_id = custID;
END //
DELIMITER ;

-- trigger to insert bill details into due_bills table when a bill is updated
-- CREATE TRIGGER IF NOT EXIST due_bills_trigger 
-- AFTER UPDATE ON bill 
-- FOR EACH ROW 
-- BEGIN 
-- IF NEW.due_date < CURDATE() 
-- THEN INSERT INTO due_bills (cust_id, meter_no, units, cost_per_unit, amount, due_date, board_id) 
-- VALUES (NEW.cust_id, NEW.meter_no, NEW.units, NEW.cost_per_unit, NEW.amount, NEW.due_date, NEW.board.id); 
-- END IF; 
-- END;


