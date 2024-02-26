"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 5 = Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered. 
"""
#! Cara 1 (Pakek Enter)
number = 0
sum = 0

while number != -1:
    number = int(input("Enter a Number (-1 to end): "))
    if number != -1:
        sum += number
    
print("The Sum of All Numbers Entered is : ", sum)

#! Cara 2 (Pakek Spasi)
# input_str = input("Enter numbers separated by spaces (-1 to end): ")

# numbers = map(int, input_str.split())

# total_sum = 0

# for number in numbers:
#     if number == -1:
#         break
#     total_sum += number

# print("The Sum of All Numbers Entered is:", total_sum)