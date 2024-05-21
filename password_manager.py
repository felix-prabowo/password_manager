from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, encrypted_pwd = data.split("|")
            print("User:", user, "| Password:", 
                  fer.decrypt(encrypted_pwd.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    pwd_bytes = pwd.encode()
    encrypted_pwd = fer.encrypt(pwd_bytes).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add?), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue