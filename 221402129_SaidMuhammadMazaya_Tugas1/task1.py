"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 1 = Write a program using Python that reads in the user's salary and divides the number by 12 months. 
        The monthly salary should be output to the console with 0 decimal places rounded up. 
"""
import math

salary = float(input("Enter Your Salary : "))

monthlySalary = math.ceil(salary / 12)

print("Your Monthly Salary is : ", monthlySalary)