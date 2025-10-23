string = input("Enter the String:")
first = string[0]
mod_str = first+string[1:].replace(first,'$')
print(“modified string:”mod_str)