import os

def create_file(filename):
    try:
        with open(filename,'x')as f:
            print(f"file name {filename} created succcessfully")
    except FileExistsError:
        print("file already exist ")
    except Exception as e:
        print("An Error accured")

def view_file():
    files = os.listdir() 
    if not files:
        print("no file found")
    else:
        print("files in directries")     
        for file in files:
            print(files)  

def del_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been delete successfully")
    except FileNotFoundError:
        print("file dosen't found")
    except Exception as e:
        print("An error accured")

def read_file(filename):
    try:
        with open("File_management.txt",'r')as f:
            content = f.read()
            #  f.close()
            print(f"the content of the file id {filename} \n {content} ")
    except FileNotFoundError:
        print("file does not found")
    except Exception as e:
        print("An error acurred")

def edit_file(filename):
    try:
        with open("File_management.txt",'a')as f:
            content = input("Enter the file name :")
            f.write(content +"\n")
            print("content added to {filename} successfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("An error acurred")

def main():
    while True:
        print("--file management app")
        print("--1: create file")
        print("--2: view All files")
        print("--3: Delete files")
        print("--4: Read files")
        print("--5: Edit files")
        print("-- 6: Exit")
        choice = input("Enter choice =")
        if choice == "1":
            filename=input("Enter the filename to create =")
            create_file(filename)
        elif choice =="3":
            filename = input("Enter the name of the file to delete =")
            del_file(filename)
        elif choice == "2":
            view_file()
        elif choice == "4":
            filename = input("Enter the file name to read =")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the file name you Edit =")
            edit_file(filename)
        elif choice == "6":
            print("closing the app")
            break
        else:
            print("invalid input please enter the valid input between the range of the 1 to 6")
        
if __name__ == "__main__":
    main()          







