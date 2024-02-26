"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 3 = Write a program that reads in a number and prints the either Small, 
        Medium or Large depending on if the number is below 100 or above 200. 
"""
number = int(input("Enter a Number : "))

if number < 100:
    print("Small")
elif number > 200:
    print("Large")
else:
    print("Medium")