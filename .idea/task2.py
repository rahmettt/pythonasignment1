c_name = input("Enter customer name: ")
q=0
a=input("Enter product name (or 'done' to finish): ")
t=0
price=0
while (a!="done"):
    price = float(input("Enter price: "))
    q+=1
    t+=price
    a=input("Enter product name (or 'done' to finish): ")
print("-" * 30)





print("Customer :", c_name)
print("Items :", q)
print("Subtotal :",t,"KZT")
print("-" * 30)




if (t<3000):
    print("Discount tier : No discount")
    print("Discount : 0.0 KZT")
    print("Total :",t,"KZT")
elif (t>=3000 and t<7000):
    print("Discount tier : 5% Discount")
    dis=(t*0.05)
    print("Discount :",dis,"KZT")
    print("Total :",t-dis,"KZT")
else:
    print("Discount tier : 15% Discount")
    dis=(t*0.15)
    print("Discount :",dis,"KZT")
    print("Total :",t-dis,"KZT")
print("-" * 30)






print("Name uppercase :",c_name.upper())
print("Name lowercase :",c_name.lower())
print("Name length :",len(c_name))
if(len(c_name)>5): print("Lone name")
else: print("Short name")
