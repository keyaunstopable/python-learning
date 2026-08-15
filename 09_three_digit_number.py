num=int(input("Enter your fav 3 digit number: "))
hunds_digit=num//100
tens_digit = (num // 10)%10
ones_digit = num % 10
print("Hundreds digits: ",hunds_digit)
print("Tens digit: ",tens_digit )
print("Units digit: ",ones_digit )
print("The sum of the three digits: ",hunds_digit + tens_digit + ones_digit )
print("The product of the digits: ",hunds_digit * tens_digit * ones_digit )
