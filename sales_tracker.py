import json
FILE_NAME = "sales.json"
def load_sales():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
sales = load_sales()
def save_sales(sales):
    with open(FILE_NAME, "w") as file:
        json.dump(sales, file, indent=4)
#.append() adds something to the end of the list 

# total_profit = 0 # before the looop we put total profit.
# for sale in sales: # for creates a loop #everything under is in the loop!
    # profit = sale["price"] - sale["cost"]
    # total_profit = total_profit + profit
    # print(sale["product"], profit)
    
# print("Total profit:", total_profit) # this is outside of the loop, so it will only print once, after the loop is done. 

choice = ""
while choice != "4": 
    print("1. Add sale")
    print("2. View sales")
    print("3. View total profit")
    print("4. Exit")
    choice = input("Choose a number (1-4): ")
    if choice == "1":
        product = input("Enter product name: ")
        price = float(input("Enter Price:"))
        cost = float(input("Enter Cost:"))
        sale = {"product": product, "price": price, "cost": cost}
        save_sales(sales)
        sales.append(sale)
        print("savings files")
        print("Sale added successfully.")
    elif choice == "2":
        for sale in sales:
            print("Product:", sale["product"], "| Price:", sale["price"], "| Cost:", sale["cost"])

    elif choice == "3":
        total_profit = 0
        for sale in sales:
            profit = sale["price"] - sale["cost"]
            total_profit = total_profit + profit
        print("Total profit:", total_profit)
        
    elif choice == "4":
        print("invalid choice. Please choose a number between 1 and 4.")   




