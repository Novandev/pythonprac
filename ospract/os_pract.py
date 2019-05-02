import os

print(os.getcwd()) # this gets the current directory

print(os.path.abspath('.')) # this also prints the absolute path

# to rename a file, drop the string to the absolute path and use this function:
os.rename('name2.name', 'name2.name')


print(os.listdir('.')) # will print all files in the directory