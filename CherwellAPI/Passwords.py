from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_message(file_name,message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    with open("{}.key".format(file_name), "wb") as key_file:
        key_file.write(encrypted_message)

    return encrypted_message

def decrypt_message(file_name):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    encrypted_message = open("{}.key".format(file_name), "rb").read()
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()