contacts = {

}
while True:
    print("App contact managements")
    print("1:Create contact")
    print("2:View Contact")
    print("3:Update Contact")
    print("4:Delete Contact")
    print("5:Search Contact")
    print("6:Count Contact")
    print("7:Exit Contact")

    choice = input("Enter your choice")
    if choice == "1":
        name = input("Enter your name")
        if name in contacts:
            print(f"contact name {name} alredy exist:")
        else:
            age =input("Enter the age ")
            email =input("Enter the email ")
            mobile =input("Enter the mobile ")
            contacts[name]={'age':int(age),'email':email,'mobile':int(mobile)}
            print(f"{contacts} name has been sucessfully updated ")
    elif choice == "2":
        name = input("Enter the contact name to view")
        if name in contacts:
            contact = contacts[name]
            print(f"'name':{name},'Age':{age},'mobile mobile':{mobile}")
        else:
            print("contacts not found")
    elif choice == "3":
        name = input("Enter the name")
        if name in contacts:
            age =input("Enter the updated age ")
            email =input("Enter the updated email ")
            mobile =input("Enter the updated mobile ")
            contacts[name]={'age':int(age),'email':email,'mobile':int(mobile)}
        else:
            print("contacts not found")
    elif choice == "4":
        name = input("Enter the name you want to delete")
        if name in contacts:
            del contacts[name]
            print(f" contact '{name}' has been deleted")
        else:
            print("tcontacts does not found")
    elif choice == "5":
        search_name = input("Enter the name you want to search")
        for name,contact in contacts.item():
            if search_name.lower() in name.lower():
                print(f"found = name :{name},age:{age},mobile no {mobile}")
                found = True
        if not found:
            print("contact not found")
    elif choice == "6":
        print(f"total contact in the app {len(contacts)}")
    elif choice == "7":
        print("closing the app")
        break
    else:
        print("invalid input")



