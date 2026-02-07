"""
sum & reverse of number
"""

number = int(input("enter a 2 digits number: "))

yekan = number % 10
dahgan = number // 10

sumDigits = yekan + dahgan
reversedNumber = int(str(yekan) + str(dahgan))

print("sum of digits:", sumDigits, "\nreversed number:", reversedNumber)