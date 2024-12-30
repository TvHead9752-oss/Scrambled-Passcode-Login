def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Extract the username and password
def extract_credentials(content):
    username_start = content.find('u')
    username_end = content.find('r', username_start) + 1
    username = content[username_start:username_end]

    password = ""
    for i in range(len(content) - 3):
        if content[i:i+4].isdigit():
            password = content[i:i+4]
            break

    return username, password


def write_creds(username, password):
    with open("revealed_passcode.txt", "w") as file:
        file.write(f"Username: {username}\nPassword: {password}\n")

# Main login
def login():
    file_path = "scrambled_passcode.txt"
    content = read_file(file_path)
    print(content)
    username, password = extract_credentials(content)

    if not username or not password:
        with open("logfile.log", "w") as log_file:
            log_file.write("FAILURE | Username: " + (username or "N/A") + " | Password: " + (password or "N/A") + "\n")
        return

    #  revealed_passcode.txt
    write_creds(username, password)
    
    while True:
        input_username = input("Username: ")
        input_password = input("Password: ")

        if input_username == username and input_password == password:
            # Write success log
            with open("logfile.log", "w") as log_file:
                log_file.write("SUCCESS | Username: " + input_username + " | Password: " + input_password + "\n")
            print("Login successful!") 
            break
        else:
            print("Invalid username or password. Please try again.")

# Run the login
login()
