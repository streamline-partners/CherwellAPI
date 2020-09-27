from cryptography.fernet import Fernet
import pickle

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    outfile = open("secret.key", "wb")
    pickle.dump(key,outfile)

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    infile = open("secret.key", "rb")
    key = pickle.load(infile)

    return key

def encrypt_message(file_name,message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    outfile = open("{}.key".format(file_name), "wb")
    pickle.dump(encrypted_message,outfile)

    return encrypted_message

def decrypt_message(file_name):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    infile = open("{}.key".format(file_name), "rb")
    encrypted_message = pickle.load(infile)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()

def create_encrypted_cherwell_credentials(password, client_key):
    """
    Generates a key and save it into a file
    """
    generate_key()
    client_key = encrypt_message("cherwell_api_key",client_key)
    password = encrypt_message("cherwell_password",password)