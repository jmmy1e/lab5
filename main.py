"""
LAB #5
    09/24/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    Rolodex: Loads contacts from addresses.txt, lets the user display, add, search, and
    modify entries, then saves and exits. Uses Contact for the data model and
    check_input for simple menu validation.
"""

from contact import Contact
import check_input

def read_file():
    """Load contacts from 'addresses.txt' and return a list sorted by last, then first"""
    contacts = []
    with open("addresses.txt") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 6:
                contacts.append(Contact(parts[0], parts[1], parts[2],
                                        parts[3], parts[4], parts[5]))
    contacts.sort()  # uses Contact.__lt__ (last, then first)
    return contacts


def write_file(contacts):
    """Save all contacts to 'addresses.txt'"""
    with open("addresses.txt", "w") as f:
        for c in contacts:
            f.write(repr(c) + "\n")

    # Uncomment to test writing without overwriting addresses.txt
    #with open("temp_addresses.txt", "w") as f:
    #    for c in contacts:
    #        f.write(repr(c) + "\n")

def get_menu_choice():
    """Display main menu 1-5 and get user input"""
    print("Rolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")
    return check_input.get_int_range("> ", 1, 5)


def modify_contact(cont):
    """Modify a contact’s fields until user hits Save (7)"""
    print("\n" + str(cont) + "\n")
    choice = 0
    while choice != 7:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")
        choice = check_input.get_int_range("> ", 1, 7)

        if choice == 1:
            cont.fn = input("Enter new first name: ")
        elif choice == 2:
            cont.ln = input("Enter new last name: ")
        elif choice == 3:
            cont.ph = input("Enter new phone number: ")
        elif choice == 4:
            cont.addr = input("Enter new address: ")
        elif choice == 5:
            cont.city = input("Enter new city: ")
        elif choice == 6:
            cont.zip = input("Enter new zip code: ")
            

def main():
    """Run the Rolodex: load data, show menu loop, save, then exit."""
    contacts = read_file()

    while True:
        choice = get_menu_choice()

        # 1) Display Contacts
        if choice == 1:
            print(f"Number of contacts: {len(contacts)}")
            for idx, c in enumerate(contacts, start=1):
                print(f"{idx}. {str(c)}\n")

        # 2) Add Contact (all strings)
        elif choice == 2:
            print("Enter new contact:")
            first = input("First name: ")
            last = input("Last name: ")
            phone = input("Phone #: ")
            addr = input("Address: ")
            city = input("City: ")
            zip_code = input("Zip: ")
            contacts.append(Contact(first, last, phone, addr, city, zip_code))
            contacts.sort()
            print()

        # 3) Search by last name or zip
        elif choice == 3:
            print("Search:")
            print("1. Search by last name")
            print("2. Search by zip")
            s_choice = check_input.get_int_range("> ", 1, 2)

            if s_choice == 1:
                target = input("Enter last name: ")
                matches = [c for c in contacts if c.ln == target]
            else:
                target = input("Enter zip code: ")
                matches = [c for c in contacts if c.zip == target]

            if matches:
                for c in matches:
                    print(str(c) + "\n")
            else:
                print(f'No matches found for "{target}".')

        # 4) Modify a contact by first and last name
        elif choice == 4:
            first = input("Enter first name: ")
            last = input("Enter last name: ")

            found = False
            for c in contacts:
                if c.fn == first and c.ln == last:
                    found = True
                    print("\n" + str(c) + "\n")
                    modify_contact(c)
                    contacts.sort()
                    break
            if not found:
                print("\nCouldn't find contact\n")

        # 5) Save and Quit
        elif choice == 5:
            print("Saving File...")
            write_file(contacts)
            print("Ending Program")
            break

if __name__ == "__main__":
    main()