import random
import time
import string
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
password_list = []
def welcome_message():
    """
    Displays the initial welcome message for Hector-PassGen.
    This function sets the professional tone for the application and introduces the brand.
    """
    print("---------------------------------------------------------")
    time.sleep(0.5)
    print("   Welcome to Hector-PassGen - Secure Your Future.      ")
    time.sleep(0.5)
    print("   ---------------------------------------------------   ")
    time.sleep(0.5)
    print("   Powered by Hector Tech © 2026                         ")
    time.sleep(0.5)
    print("   GitHub: https://github.com/Benyamin-Masoumi/Hector-PassGen      ")
    time.sleep(0.5)
    print("---------------------------------------------------------")
    time.sleep(0.5)
    print("   Ready to generate your unbreakable password...        ")
    time.sleep(0.5)
    print("---------------------------------------------------------")
def get_user_preferences():
    # Gets the user's desired criteria for the password (length, characters, etc.)
    letters_count = int(input("How many letters should it contain? "))
    numbers_count = int(input("How many numbers should it contain? "))
    symbols_count = int(input("How many special characters (symbols) should it contain? "))
    return letters_count, numbers_count, symbols_count
def generate_password(letters_count, numbers_count, symbols_count):
    # Generates a secure, randomized password based on user-defined criteria
    for _ in range(letters_count):
        password_list.append(random.choice(letters))
    for _ in range(numbers_count):
        password_list.append(random.choice(numbers))
    for _ in range(symbols_count):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = "".join(password_list)
        
    
    
    
    
    
    
