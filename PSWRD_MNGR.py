import random
import string
#imports random and string module, allowing a library of characters to be used and ability to randomly choose those characters

def generate_password(numlength):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(numlength))
    #creates random password by choosing random characters until however long the user inputs
def save_credentials(website, username, password, filename="passwords.txt"):
    try:
        with open(filename, "a") as file:
           #opens a temporary variable 'file' to interact with passwords.txt in append mode which creates the file if there is not already one
            #the with statement automatically opens and closes the file when the program is stopped
            file.write(f"Website: {website}\nUsername/Email: {username}\nPassword: {password}\n{'-'*40}\n")
            #creates a file named passwords.txt to save enteries in a organized human readable format
    except Exception as e:
        print(f"Error saving credentials: {e}")

def delete_entry(filename="passwords.txt"):
    website_to_delete = input("Enter the website name to delete: ").strip()
    # Ask the user for the website name they want to delete, strip extra spaces.

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            # Open the file in read mode and read all lines into a list.

        new_lines = []  #this will hold all lines except the ones we want to delete.
        skip = False    #this flag tells us whether we are skipping over lines (i.e., the block to delete).
        entry_found = False  #this flag helps track if we found the website entry.

        for line in lines:
            if line.startswith(f"Website: {website_to_delete}"):
                #if the line starts with 'Website: <website_to_delete>', we found the block to delete.
                skip = True  #start skipping lines.
                entry_found = True  #mark that we found the entry.
                continue  #skips the current line (the Website line itself).

            if skip and line.strip() == '-'*40:
                #when it reachs the separator line (---------), stop skipping.
                skip = False  #reset skip flag to resume adding lines.
                continue  #skips the separator line as well.

            if not skip:
                new_lines.append(line)
                #if its not skipping, keep adding lines to the new_lines list.

        if entry_found:
            #If the website is found it prints:
            with open(filename, "w") as file:
                for line in new_lines:
                    file.write(line)
                    # Write the remaining lines back to the file, effectively deleting the target block.
            print(f"\nEntry for '{website_to_delete}' deleted.\n")
        else:
            print(f"\nNo entry found for '{website_to_delete}'.\n")
            #lets the user if the website wasn't found.

    except FileNotFoundError:
        print("\nNo entries found. Password file does not exist yet.\n")
        #lets you know if the entry isnt found in the file

    except Exception as e:
        print(f"Error deleting entry: {e}")
        #catch any other exceptions and print the error message.


def add_entry():
    website = input("Enter website name: ").strip()
    username = input("Enter your username/email: ").strip()
    #assigns the variables in save_credentials with user input, also strips any additional 
    numlength = int(input("Enter length you would like your password (minimum 12): "))
    while numlength < 12:
        numlength = int(input("Enter a length of 12 or greater: "))
    password = generate_password(numlength)
    #calls to the generate password function to randomly generate a password
    print(f"\nGenerated Password: {password}")
    save_credentials(website, username, password)
    #calls to the save credentials functions and writes the input given it into the passwords.txt file
    print("Entry Saved!\n")
     #allows you to add an entry/login asking for website name, username, how long you want your password and what the generated password is.


def main():
    while True:
        print("=== SIMPLE PASSWORD MANAGER ===")
        print("1. Add new entry")
        print("2. Delete an entry")
        print("3. Exit")
        choice = input("Choose an option: ")
        #creates the menu that the user is greeted with
        if choice == '1':
            add_entry()
        elif choice == '2':
            delete_entry()
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.\n")

main()
#runs the main menu function
