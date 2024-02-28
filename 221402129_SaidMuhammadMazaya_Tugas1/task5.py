"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 5 = Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered. 
"""

number = 0
sum = 0

while number != -1:
    number = int(input("Enter a Number (-1 to end): "))
    if number != -1:
        sum += number
    
print("The Sum of All Numbers Entered is : ", sum)