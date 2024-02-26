"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 4 = Write a program that reads in a number and prints the sum of all values from 1 up to the number. 
    For example, if the user enters 5 the program should display 15. 15 is (1+2+3+4+5).
"""
number = int(input("Enter a Number : "))

sum = 0
for i in range(1, number + 1):
    sum += i

print("The Sum of All Values from 1 up to the Number is : ", sum)