original_price = float(input("enter yor original price"))
if original_price > 5000:
    discount = original_price*5/100
    print("you have 5% discount")
    price = original_price - discount
else:
    print("No discount available")
    price = original_pricegit push -f origin main
sub_totall = price+ price*5/100
print(f"your cost is rs{sub_totall} , thank you and come again")
