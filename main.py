import os
import mysql.connector #type: ignore

# Item class
class Item:
     def __init__(self, name, price):
          self.name = name
          self.price = price

     def calculate_total_with_tax(self, tax_rate):
          return self.price + (self.price * tax_rate)

# Database configuration
db_config = {
     "host": "localhost",
     "user": "root", #Type username, default = root
     "password": "tender_feeling", #Type your connection password, if none, then leave empty
     "database": "billDataBase", #Type database name
     "port": 3306
}

# Global constants
TAX = 0.13
STARTING_BUDGET = 1000.00

# Initialize items
itemArr = [
     Item("Mo:Mo", 100.00),
     Item("Chow-mein", 120.00),
     Item("Thukpa", 150.00),
     Item("Pizza", 200.00),
     Item("Pasta", 250.00),
]

def print_menu(budget):
     os.system("cls")
     print("*" * 30)
     
     for i, item in enumerate(itemArr, start=1):
          print(f"* {i}. {item.name} \t Rs. {item.price:.2f} *")
     
     print("* 6. Exit" + (" " * 20) + "*")
     print("* 7. Confirm Order" + (" " * 11) + "*")
     print(f"\n* Your budget: Rs. {budget:.2f}")
     print("*" * 30)

def print_invoice(orders, tax_rate):
     os.system("cls")
     print("*" * 32)
     
     total = 0.00

     for order in orders:
          item_total = order.calculate_total_with_tax(tax_rate)
          print(f"* {order.name} \t Rs. {item_total:.2f} *")
          total += item_total
     
     print(f"* Total (with VAT): Rs. {total:.2f} *")
     print("*" * 32)
     
     return total

def save_to_database(total_amount, tax, net_amount):
     try:
          connector = mysql.connector.connect(**db_config)
          cursor = connector.cursor()

          # Insert bill details into the table
          query = """
                    INSERT INTO bill(total_amount, tax, net_amount)
                    VALUES(%s, %s, %s)
                  """

          values = (total_amount, tax, net_amount)
          cursor.execute(query, values)
          connector.commit()

          print("\nBill saved to the database successfully!")
          cursor.close()
          connector.close()
     except mysql.connector.Error as e:
          print(f"Error saving to database: {e}")

def main():
     budget = STARTING_BUDGET
     orders = []

     while True:
          print_menu(budget)

          try:
               choice = int(input("Enter your choice (1-7): "))

               if choice == 6:  # Exit
                    confirm = input("Are you sure you want to exit? (y/n): ")
                    if confirm.lower() == "y":
                         print("Thank you for visiting!")
                         break
               
               elif choice == 7:  # Confirm order
                    if orders:
                         total = sum(order.price for order in orders)
                         tax = total * TAX
                         net_amount = total + tax

                         # Print invoice and save to database
                         print_invoice(orders, TAX)
                         save_to_database(total, tax, net_amount)
                         break
                    else:
                         print("No items selected!")
               
               elif 1 <= choice <= 5:  # Add item to orders
                    item = itemArr[choice - 1]
                    
                    if budget >= item.calculate_total_with_tax(TAX):
                         orders.append(item)
                         budget -= item.calculate_total_with_tax(TAX)
                         print(f"Added {item.name} to your order!")
                    else:
                         print("Not enough budget for this item.")
               
               else:
                    print("Invalid choice. Please try again.")
          
          except ValueError:
               print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()