c_name = input("Enter customer name: ")
p_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quan = int(input("Enter quantity: "))
print("=" * 30)
print("        SHOP RECEIPT")
print("=" * 30)

print("Customer :", c_name)
print("Product :", p_name)
print("Price :", price, "KZT")
print("Quantity :", quan)
print("-" * 30)
subtotal = price * quan
discount = subtotal / 10
if (subtotal <= 5000):
    discount = 0
total = subtotal - discount
print("Subtotal :", subtotal, "KZT")
print("Discount :", discount, "KZT")
print("Total :", total, "KZT")
print("=" * 30)
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", subtotal > 3000)
