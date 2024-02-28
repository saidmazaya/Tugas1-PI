"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 2 = Write a program that reads in a whole number and divides it by 3 and 
        displays the result with three decimal places if they exist (rounded up). 
"""
number = int(input("Enter a Number : "))

result = number / 3

print(f"The Result of {number} / 3 is : {round(result, 3)}")