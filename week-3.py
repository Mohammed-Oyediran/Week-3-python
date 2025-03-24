# Question 1

def calculate_discount(price, discount_percent):
    if(discount_percent >=0.2):
        return (1 - discount_percent) * price
    else:
        return price
    

print(calculate_discount(200,0.5))
print(calculate_discount(200, 0.1))
print(calculate_discount(200, 0.2))


# Question 2

price = input("Enter the price: ")
discount_percent = input("Enter the discount percentage(without % sign): ")
   
def calculate_final_discount(price, discount_percent):
   
    price = float(price)
    discount_percent = float(discount_percent) / 100
    
    if(discount_percent == ""):
        return price
    
    elif(discount_percent >=0.2):
        
        return (1 - discount_percent) * price
    else:
        return price
   

print(calculate_final_discount(price, discount_percent))