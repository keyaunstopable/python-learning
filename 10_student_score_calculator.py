name=str(input("Enter your name: "))
math=float(input("Enter your maths marks out of 100here: "))
phy=float(input("Enter your physics marks out of 100 here: "))
chem=float(input("Enter your chemistry marks out of 100 here: "))
tl=math+phy+chem
print("Your total marks out of 300 is: ",tl)
avg=tl/3
print("Your average marks are: ",avg)
percent=(tl/300)*100
print("Your percentage is: ",percent,"%")
