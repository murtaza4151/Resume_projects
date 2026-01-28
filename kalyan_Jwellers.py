# Kalyan Jwelles project

discount = 0

name = input("Enter your name=")
Gender = input("Enter your Gender=")
Age = int(input("Enter your Age="))
product = input("Enter your product=")
product_gram = int(input("Enter your product_gram="))

current_gold_price_1gram = 5752
Total_gold_rate = current_gold_price_1gram * product_gram
print("Total Gold Rate=",Total_gold_rate)

making_charges = 845
Total_making_charges = product_gram * making_charges
print("Total making charges=",Total_making_charges)
Total_Amount = Total_gold_rate + Total_making_charges

if Gender == "m" or Gender == "M":
    if Age > 65:
        if Total_Amount > 21000 and Total_Amount <=31000:
            discount = 20
        elif Total_Amount > 31000 and Total_Amount <=51000:
            discount = 30
        elif Total_Amount > 51000:
            discount = 35
    else:
        if Total_Amount > 21000 and Total_Amount <=31000:
            discount = 10
        elif Total_Amount > 31000 and Total_Amount <=51000:
            discount = 20
        elif Total_Amount > 51000:
            discount = 25
if Gender == "f" or Gender == "F":
    if Age > 65:
        if Total_Amount > 21000 and Total_Amount <= 31000:
            discount = 25
        elif Total_Amount > 31000 and Total_Amount <= 51000:
            discount = 35
        elif Total_Amount > 51000:
            discount = 40
    else:
        if Total_Amount > 21000 and Total_Amount <= 31000:
            discount = 15
        elif Total_Amount > 31000 and Total_Amount <= 51000:
            discount = 25
        elif Total_Amount > 51000:
            discount = 30

Discount_Amount = Total_Amount * (discount / 100)
final_price = Total_Amount - Discount_Amount

print("\n---------- BILL SUMMARY ----------")
print("Enter your name=",name)
print("Enter your Gender=",Gender)
print("Enter your Age=",Age)
print("Enter your product name=",product)
print("Enter your product_Gram=",product_gram)
print("Total Amount=",Total_Amount)
print("Discount Applied=",discount)
print("Final Price=",final_price)