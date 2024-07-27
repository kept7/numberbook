import os
import json
import signal

from pathlib import Path 

NUMBERS_DIRECTORY = f"{Path.home()}/.kept-numberbook"
NUMBERS_FILE = os.path.join(NUMBERS_DIRECTORY, "numbers.json")



MENU = """Menu:
1. Reveal contacts of the Numberbook
2. Add the contact to the Numberbook
3. Delete the contact from the Number book
0. Shut down of the Numberbook
Select the desired action"""

print("Welocme to the Numberbook by kept7 ver. 1.0")

list_of_contacts = []

class Contact:
    def __init__(self, first_name, second_name, phone_number):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        

    def __str__(self) -> str:
        return f"""First Name: {self.first_name}
Second Name: {self.second_name}
Phone Number: {self.phone_number}"""


def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J", end="")


def load_numbers():
    global list_of_contacts

    if not os.path.exists(NUMBERS_FILE):
        return

    with open(NUMBERS_FILE) as f:
        json_list_of_contacts = json.load(f)
        list_of_contacts = list(map(lambda x: Contact(**x), json_list_of_contacts))


def dump_numbers():
    with open(NUMBERS_FILE, "w") as f:
        json.dump(list(map(lambda x: x.__dict__, list_of_contacts)), f, indent=2)


def reveal_list_of_contacts():
    for i, c in enumerate(list_of_contacts):
        print(f"№{i+1}", c, sep="\n")


def add_contact_in_list_of_contacts():
    print("Write first name of contact:")
    first_name = input()
    print("Write second name of contact:")
    second_name = input()
    print("Write phone number of contact:")
    phone_number = input()
    new_contact = Contact(first_name, second_name, phone_number)
    print(new_contact)
    print("Do you want to add this contact in your Numberbook? Answer Yes or No.")
    answer = input()
    if answer.lower() in ["yes", "y", ""]:
        list_of_contacts.append(new_contact)
        print("The contact was added to Your Numberbook")
        reveal_list_of_contacts()
    else:
        print("The contact not added to Your Numberbook")
        reveal_list_of_contacts()


def delete_contact_from_list_of_contacts():
    print("Write the number of contact to remove it from Numberbook")
    contact_idx = int(input())
    try:
        list_of_contacts.pop(contact_idx-1)
    except IndexError:
        print("Contact not found")
    
    reveal_list_of_contacts()


def shut_down(*_, **__):
    print("\nThank you. Shut down")
    dump_numbers()
    exit(0)

signal.signal(signal.SIGINT, shut_down)

actions = [
    shut_down,
    reveal_list_of_contacts,
    add_contact_in_list_of_contacts,
    delete_contact_from_list_of_contacts
]

def main():
    if not os.path.exists(NUMBERS_DIRECTORY):
        os.mkdir(NUMBERS_DIRECTORY)

    load_numbers()

    while True:
        clear_screen()
        print(MENU)
        number_of_action = int(input())
        try:
            actions[number_of_action]()
        except IndexError:
            print("Unknown action")
        print("Press Enter to continue", end="")
        input()


def test():
    contact1 = Contact(first_name="Denis", second_name="Gorodetski", phone_number="123")
    print(contact1)

    contact2 = Contact(first_name="Mike", second_name="Ches", phone_number="1234")
    print(contact2)

if __name__ == "__main__":
    main()
