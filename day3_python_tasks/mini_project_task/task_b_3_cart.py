#Shopping Cart Program
'''
Add item + price
Calculate total
Apply 10% discount if total > 1000
'''

def Shopping_cart_entry() -> dict:
    my_data={}
    
    print("type '=' if all items entered")
    
    while True:
        data=input("Enter the item name & price (Format : item price):")
        print(data)
        
        if data == "=":
            break
        
        item,price = data.split()
        price=int(price)
        
        my_data[item]=price
    
    return my_data

def discount_amt(tot_amount:int,discount=10) -> int:
    dis_amount=tot_amount-(tot_amount*discount/100)
    return int(dis_amount)

def total(data:dict):
    tot_amount = sum(data.values())
    
    if tot_amount > 1000:
        return tot_amount,discount_amt(tot_amount)  
    else:
        return tot_amount,False
    
        
    
data = Shopping_cart_entry()

price,discount_price=total(data)

if discount_price != False:
    print(f"Total Amount = {price}/- | On applying 10% discount = {discount_price}/-")
else:
    print(f"Total Amount = {price}/- | No discount Applied under rupees 1000")


