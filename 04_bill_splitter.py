bill=int(input("Total bill: "))
sh=int(input("Number of people:"))
tip=int(input("Tip percentage: "))
tip=(tip/100)*bill
amt=bill+tip
print("Tip amount: ",tip)
print("Total bill: ",amt)
print("Each person pays: ",amt/sh)
