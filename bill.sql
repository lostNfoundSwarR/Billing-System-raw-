--Add this code to a SQL management IDE like SQL workbench or recreate this table
--in MS-Access

CREATE DATABASE billDataBase;
USE billDataBase;

CREATE TABLE bill(
	bill_id INT PRIMARY KEY AUTO_INCREMENT,
	bill_date DATETIME DEFAULT NOW(),
     total_amount DECIMAL(10, 2),
     tax DECIMAL(10, 2),
     net_amount DECIMAL(10, 2)
); 	