# BillDataBase:

This database can generally be used for tracking information and saving data regarding bills,
which can generally be used for E-commerce applications.

This database consists of a table called `bill` which keeps track of the information.
It has 5 columns

#1. bill_id:
      Purpose: To keep track of the bill number, it acts as a unique identifier for the
	       bill.

      Config:
             type/s : INT (Integer) & PRIMARY KEY
	     add-on/s : AUTO_INCREMENT

#2. bill_date:
      Purpose: To keep track of when the bill was created.

      Config:
             type/s : DATETIME
	     add-on/s : DEFAULT = NOW() [Current date & time]

#3. total_amount:
      Purpose: To keep track of the total amount of the bill (without tax).

      Config:
             type/s = DECIMAL(10, 2)
	     add-on/s : None

#4. tax:
      Purpose: To keep track of the total amount of tax of each bill.

      Config:
             type/s : DECIMAL(10, 2)
	     add-on/s : None

#5. net_amount:
      Purpose: To keep track of the grand total amount of the bill (with tax).

      Config:
             type/s : DECIMAL(10, 2)
	     add-on/s : None
