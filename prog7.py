# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

file = input("Enter the file: ")
file_extension = file.split('.')
print("The extension is: ",file_extension[1])