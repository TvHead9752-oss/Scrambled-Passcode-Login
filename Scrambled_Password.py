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
    print("File content read successfully:")
    print(content)
    
    username, password = extract_credentials(content)
    print(f"Extracted username: {username}")
    print(f"Extracted password: {password}")


    # If credentials are valid...
    write_creds(username, password)

    # login
    while True:
        input_username = input("Username: ")
        input_password = input("Password: ")

        # Check if username and password match the extracted one
        if input_username == username and input_password == password:
            
            # Write success/failure log
            with open("logfile.log", "a") as log_file:  # append success log
                log_file.write("SUCCESS | Username: " + input_username + " | Password: " + input_password + "\n")
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
            
            with open("logfile.log", "a") as log_file:  # append failure log
                log_file.write("FAILURE | Username: " + input_username + " | Password: " + input_password + "\n")

# Run the login
login()
