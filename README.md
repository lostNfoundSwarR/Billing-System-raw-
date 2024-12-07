This project uses `sql.connector`.

# 1 How to add sql.connector

Type the following `pip` command in your terminal:
	```pip install mysql-connector-python```

# 2 Check if it's installed or not

Type the following `pip` command in your terminal:
	```pip show mysql-connector-python```
or type a simple program like:
**import mysql.connector
print("MySQL Connector installed successfully!")**

# 3 BillDataBase:

This database can generally be used for tracking information and saving data regarding bills,
which can generally be used for E-commerce applications.

This database consists of a table called `bill` which keeps track of the information.
It has 5 columns

## 3.1. bill_id:
      Purpose: To keep track of the bill number, it acts as a unique identifier for the
	       bill.

      Config:
             type/s : INT (Integer) & PRIMARY KEY
	     add-on/s : AUTO_INCREMENT

## 3.2. bill_date:
      Purpose: To keep track of when the bill was created.

      Config:
             type/s : DATETIME
	     add-on/s : DEFAULT = NOW() [Current date & time]

## 3.3. total_amount:
      Purpose: To keep track of the total amount of the bill (without tax).

      Config:
             type/s = DECIMAL(10, 2)
	     add-on/s : None

## 3.4. tax:
      Purpose: To keep track of the total amount of tax of each bill.

      Config:
             type/s : DECIMAL(10, 2)
	     add-on/s : None

## 3.5. net_amount:
      Purpose: To keep track of the grand total amount of the bill (with tax).

      Config:
             type/s : DECIMAL(10, 2)
	     add-on/s : None
