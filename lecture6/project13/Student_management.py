student_val ={
    
}

def add_student(name,number):
    student_val[name]=number
    print(f"Added {name} with the {number}")

def update_student(name,number):
    if name in student_val:
        student_val[name]=number
        print(f"{name} with the marks are {number} updated")
    else:
        print(f"{name} does not found")

def delete_student(name):
    if name in student_val:
        del student_val[name]
        print(f"{name} has been deleted")
    else:
        print(f"{name} does not found")

def view_student():
    if student_val:
        for name ,number in student_val.items():
            print(f" '{name}' : '{number}'")
    else:
        print("No student found ")

def main():
    while True:
        print('\n Student GradeManagement System')
        print("1:Add student")
        print("2:Update student")
        print("3:Delete student")
        print("4:View student")
        print("5:Exit")

        choice = input("Enter your choice =")
        if choice == "1":
            name = input("Enter the Student Name =")
            number = int(input("Enter the Student Number ="))
            add_student(name,number)
        elif choice =="2":
            name = input("Enter the student name you can update =")
            number = int(input("Enter the student grade you can update ="))
            update_student(name,number)
        elif choice =="3":
            name = input("Enter the name you can delete =")
            delete_student(name)
        elif choice =="4":
            view_student()
        elif choice =="5":
            print("----closing the app")
            break
        else:
            print("invalid input ")

if __name__ == "__main__":
 main()
