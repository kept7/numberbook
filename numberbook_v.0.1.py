

# main part of my number book

print("Welocme to the Numberbook by kept7 ver. 1.0")
print("Menu:\n1. Reveal contacts of the Numberbook\n2. Add the contact to the Numberbook\n3. Delete the contact from the Numberbook\n0. Shut down of the Numberbook")
print("Select the desired action")

number_of_action = int(input())

# print("The selected number of the action is " + str(number_of_action)) - upgraded to string down below
print(f'Selected number action is {number_of_action}')

contact_1 = {
    "№": "1", 
    "First name": "Denis",
    "Second name": "Gorodetskiy",
    "Phone number": "+7-800-555-35-35"
}

contact_2 = {
    "№": "2",
    "First name": "Eduard",
    "Second name": "Kudinov",
    "Phone number": "+7-902-023-33-44"
}

contact_3 = {
    "№": "3",
    "First name": "Mikhail",
    "Second name": "Chesnovskiy",
    "Phone number": "+44-233-333-23-33"
}

list_of_contacts = [contact_1, contact_2, contact_3]

def reveal_list_of_contacts():
    print(list_of_contacts)

def add_contact_in_list_of_contacts():
    print("Write first name of contact:")
    first_name = input()
    print("Write second name of contact:")
    second_name = input()
    print("Write phone number of contact:")
    phone_number = input()
    new_contact = dict(first_name = first_name, second_name = second_name, phone_number = phone_number)
    print(new_contact)
    print("Do you want to add this contact in your Numberbook? Answer Yes or No.")
    answer = input()
    if answer.lower() == "yes":
        list_of_contacts.append(new_contact)
        print("The contact was added to Your Numberbook\n", list_of_contacts)
    else:
        print("The contact not added to Your Numberbook\n", list_of_contacts)
    
def delete_contact_from_list_of_contacts():
    print("Write the number of contact to remove it from Numberbook")
    position_of_contact_in_list_of_contacts = int(input())
    if position_of_contact_in_list_of_contacts <= len(list_of_contacts):
        list_of_contacts.pop(position_of_contact_in_list_of_contacts - 1)
        print(list_of_contacts)
    else:
        print("Contact doesn't exist")

def shut_down():
    print("Thank you. Shut down")


while number_of_action != 0:

    if number_of_action == 1:
        reveal_list_of_contacts()
        
    elif number_of_action == 2:
        new_contact = add_contact_in_list_of_contacts()
        
    elif number_of_action == 3:
        delete_contact_from_list_of_contacts()

    print("Press Enter to continue")
    input()
    print("Menu:\n1. Reveal contacts of the Numberbook\n2. Add the contact to the Numberbook\n3. Delete the contact from the Numberbook\n0. Shut down of the Numberbook")
    print("Select the desired action")
    number_of_action = int(input())

else:
    shut_down()
