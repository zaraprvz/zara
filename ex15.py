
from sys import argv
# need one argument 
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
