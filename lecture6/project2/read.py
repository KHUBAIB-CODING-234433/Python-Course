file = open("File_management.txt",'r')
content = file.read()
file.close()
print(f"the content of the file id {content}")