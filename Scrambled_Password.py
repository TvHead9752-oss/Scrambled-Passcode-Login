from datetime import datetime
from zoneinfo import ZoneInfo

# Read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Extract username and password
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

# Write credentials
def write_creds(username, password):
    with open("revealed_passcode.txt", "w") as file:
        file.write(f"Username: {username}\nPassword: {password}\n")

# Log the result
def log_event(event, user, pwd, time, fails=None):
    with open("logfile.log", "a") as log_file:
        if event:
            log_file.write(f"{event} | Username: {user} | Password: {pwd} | Timestamp: {time}\n")
        if fails is not None:  # Log the failure count ONLY at the end (please work)
            log_file.write(f"TOTAL FAILURES: {fails}\n")

# Main login process
def login():
    
    file_path = "scrambled_passcode.txt"
    content = read_file(file_path)
    print("File content read successfully:")
    print(content)

    username, password = extract_credentials(content)
    print(f"Extracted username: {username}")
    print(f"Extracted password: {password}")

    # extracted credentials
    write_creds(username, password)

    # failure tracker
    fails = 0

    while True:
        input_user = input("Username: ")
        input_pwd = input("Password: ")

        # current time
        cur_time = datetime.now(ZoneInfo("EST")).strftime("%Y-%m-%d %H:%M:%S %Z")

        if input_user == username and input_pwd == password:
            print("Login successful!")
            log_event("SUCCESS", input_user, input_pwd, cur_time)
            break
        else:
            print("Invalid username or password. Please try again.")
            fails += 1
            log_event("FAILURE", input_user, input_pwd, cur_time)

    # total failures log
    log_event("", "", "", "", fails)

# login process
login()
