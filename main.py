from contact import Contact


def read_file():
    # Assumme the path is constant
    file = open("./addresses.txt").readlines()
    contact_list = []
    for line in file:
        list_version = line.rstrip("\n").split(",")
        contact = Contact(list_version[0], list_version[1], list_version[2],list_version[3],list_version[4],list_version[5])
        contact_list.append(contact)
    
    contact_list.sort(key=lambda x: x.ln )
    return contact_list



def write_file(contacts):
    # Temporarly write to a temp version of addresses.txt to prevent fucking everything up
    with open("temp_addresses.txt", "w+") as file:
        for contact in contacts:
            file.write(contact.__repr__())

def get_menu_choice():
    valid_input = ["1" , "2", "3" , "4", "5"]
    while True:
         
        user_input = input("Rolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit\n> ")
        if user_input in valid_input:
             break
        else:
            print("Invalid Input: Please enter a number 1-5")
    return user_input

        
        # Display Contacts
        

def modify_contact(cont):
    print("\n"+cont.__str__()+"\n")
    user_input = input("Modify Menu:\n1. First name\n2. Last name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save")




def main():
    contacts = read_file()
    while True:
        user_input = get_menu_choice()
        # ! Safe to assume its 1-5

        # Display Contacts
        if user_input == "1":
                index = 1
                for contact in contacts:
                    print(f"{str(index)}. {contact.__str__()}")
                    index +=1
        # Add Contact
        # ! THERE IS NO PARSING VERIFICATION TO AUTHENTICATE PROPER INPUT OF CHARACTERS
        elif user_input == "2":

                print("New Contact")
                first_name = input("Contacts First Name: ")


                last_name = input("Contacts Last Name: ")


                phone_number = input("Contacts Phone Number: ")

                address = input("Contacts Address: ")
                city = input("Contacts City: ")
                zip  = input("Contacts Zip: ")
                new_contact = Contact(first_name, last_name, phone_number, address, city, zip)
                contacts.append(new_contact)
                
        # Search Contact
        elif user_input == "3":
            # Prompt user to search by last name OR zip
            while True:
                user_input = input("How would you like to search this contact? \n1. Last Name\n2. Zip Code\n> ")
                if user_input == "1" or user_input == "2":
                    break
                else:
                    print("Invalid Input: Please select 1 or 2")

                # Conduct Last Name search
            if user_input == "1":
                last_name = input("Enter the contacts last name: ")
                valid_contacts = []
                for contact in contacts:
                    if contact.ln == last_name:
                        valid_contacts.append(contact)
                if valid_contacts.__len__() > 0:
                    print("Found Contact(s)\n")
                    for contact in valid_contacts:
                        print(contact.__str__() + "\n")
                else:
                    print(f"Couldn't find any contact with the last name \"{last_name}\"")
            # Conduct Zip Code search
            else:
                zip = input("Enter the contacts zip code: ")
                valid_contacts = []
                for contact in contacts:
                    if contact.zip == zip:
                        
                        valid_contacts.append(contact)
                if valid_contacts.__len__() > 0:
                    print("Found Contact(s)\n")
                    for contact in valid_contacts:
                        print(contact.__str__() + "\n")
                else:
                    print(f"Couldn't find any contact with the zip code \"{zip}\"")
        elif user_input == "4":
            #full_name = input("Please enter the contacts full name (ie. First name Last name): ").split(' ')
            first = input("Enter the contacts first name: ") #full_name[0]
            last = input("Enter the contacts last name: ")# full_name[1]
            #print(f"First is {first} last is {last}")
            current_contact: Contact
            for contact in contacts:
                if contact.fn == first and contact.ln == last:
                    print("Contact found")
                    modify_contact(contact)


                    break


          
    write_file(contacts)


if __name__ == "__main__":
    main()
