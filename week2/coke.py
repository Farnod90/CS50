amount_due =50
while amount_due > 0 :
   print(f"amount_due: {amount_due}\n")
   vending_machine = int(input("inesert coin :"))
   if vending_machine in [5,10,25]:
        amount_due -= vending_machine
print(f"change owed:,{abs(amount_due)}")
