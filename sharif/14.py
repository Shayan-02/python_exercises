import pyfiglet
from termcolor import colored

text = input("enter a text: ")
font = input("enter text font: ")
color = input("enter text color: ")

if font:
    formated_text = pyfiglet.figlet_format(text, font= font)
else:
    formated_text = pyfiglet.figlet_format(text)

if color:
    colored_text = colored(formated_text, color)
    print(colored_text)
else:
    print(formated_text)