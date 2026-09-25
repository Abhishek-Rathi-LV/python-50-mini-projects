contacts = {}
while True:
    print("===== CONTACT BOOK =====")
    print("Press 1. to Add Contact")
    print("Press 2. to  View Contacts")
    print("Press 3. to Search Contact")
    print("Press 4. to Delete Contact")
    print("Press 5 to exit ")
    choice=int(input("Enter your Choice(1/2/3/4/5):-"))

    if choice==1:
        name=str(input("Enter the name of the person :-"))
        phone=int(input("Enter the phone Number of person :-)"))
        contacts[name] = phone
    elif choice==2:
        for name,phone in contacts.items():
            print(name,phone)
    elif choice==3:
        search=str(input("Enter the name to search"))
        if search in contacts:
            print("The Contact is presnt and the mobile number is ",contacts[search])
        else:
            print("The contact is absent")
    elif choice==4:
        dele=str(input("Enter the Contact name you waana delete :-)"))
        if dele in contacts:

           del contacts[dele]
           print("Deleted Sucessfully")
        else:
            print("Contact not saved")
    elif choice==5:
        print("Thankyou for choosing us :-)")
        break
    else:
        print("Wrong input")
        print("Try again")
