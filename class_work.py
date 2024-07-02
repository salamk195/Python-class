user_inputed_value = int(input("PLease select Card type 1. Regular, 2. Silver, 3. Gold, 4. Platinum" ))
S = "Silver"
G = "Gold"
P = "Platinum"
R = "Regular"
total_amount_of_goods_bought = int(input("enter the amount of goods you bought"))
if user_inputed_value ==  1:
 discount = 0
 amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
 
 if total_amount_of_goods_bought > 1000 :
  discount = 5
  amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
  
  if total_amount_of_goods_bought > 2000 :
   discount = 10
   amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
print(amount_paid)
   
   


if user_inputed_value ==  2:
 discount = 5
 amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
 
 if total_amount_of_goods_bought > 1000 :
  discount = 10
  amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
  
  if total_amount_of_goods_bought > 2000 :
   discount = 15
   amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
print(amount_paid)







if user_inputed_value ==  3:
 discount = 10
 amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
 
 if total_amount_of_goods_bought > 1000 :
  discount = 15
  amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
  
  if total_amount_of_goods_bought > 2000 :
   discount = 20
   amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
print(amount_paid)
   




if user_inputed_value ==  4:
 discount = 15
 amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
 
 if total_amount_of_goods_bought > 1000 :
  discount = 20
  amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
  
  if total_amount_of_goods_bought > 2000 :
   discount = 25
   amount_paid = total_amount_of_goods_bought - (total_amount_of_goods_bought * discount / 100)
print(amount_paid)


