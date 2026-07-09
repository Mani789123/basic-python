# Sales Management Program

product = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity Sold: "))

total_sales = price * quantity

print("\n------ Sales Report ------")
print("Product Name :", product)
print("Price        :", price)
print("Quantity     :", quantity)
print("Total Sales  :", total_sales)

if total_sales >= 1000:
    print("Performance  : Excellent Sales")
else:
    print("Performance  : Good Sales")