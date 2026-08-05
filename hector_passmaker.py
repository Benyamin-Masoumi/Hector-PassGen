import random
import time
import string
import pyperclip


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


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
    print("   Powered by Hector Tech ™ © 2026                         ")
    time.sleep(0.5)
    print("   GitHub: https://github.com/Benyamin-Masoumi/Hector-PassGen      ")
    time.sleep(0.5)
    print("---------------------------------------------------------")
    time.sleep(0.5)
    print("   Ready to generate your unbreakable password...        ")
    time.sleep(0.5)
    print("---------------------------------------------------------")


def get_user_preferences():
    """
    Gets the user's desired criteria for the password (length, characters, etc.)
    and validates the inputs to ensure they are valid integers.
    """
    while True:
       try:
          letters_count = int(input("How many letters should it contain? "))
          numbers_count = int(input("How many numbers should it contain? "))
          symbols_count = int(input("How many special characters (symbols) should it contain? "))
          return letters_count, numbers_count, symbols_count
       except ValueError:
           print("\n❌ Error: Please enter valid numbers only!\n")


def generate_password(letters_count, numbers_count, symbols_count):
    # Generates a secure, randomized password based on user-defined criteria
    password_list = []
    for _ in range(letters_count):
        password_list.append(random.choice(letters))
    for _ in range(numbers_count):
        password_list.append(random.choice(numbers))
    for _ in range(symbols_count):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


version = "1.0.2"


def show(password):
    """
    Displays the generated password to the user.
    This function handles the UI presentation layer, ensuring the final output 
    is formatted clearly for a better user experience.
    """
    for _ in range(2):
       print("LOADING")
       time.sleep(0.2)
       print("LOADING.")
       time.sleep(0.2)
       print("LOADING..")
       time.sleep(0.2)
       print("LOADING...")
       time.sleep(0.2)
    print("\n" + "=" * 50)
    time.sleep(0.5)
    print(f"  >>> Generated Password: {password}")
    time.sleep(0.5)
    print("=" * 50)
    time.sleep(0.5)
    print("   📋 Status: Copied to clipboard successfully!       ")
    time.sleep(0.5)
    print("=" * 50)
    print(f"  Powered by Hector Tech | Version: {version}")
    time.sleep(0.5)
    print(f"  GitHub: https://github.com/Benyamin-Masoumi/Hector-PassGen")
    time.sleep(0.5)
    print("="*50 + "\n")


def main():
    welcome_message()
    letters_count, numbers_count, symbols_count = get_user_preferences()
    password = generate_password(letters_count, numbers_count, symbols_count)
    pyperclip.copy(password)
    show(password)
    

if __name__ == "__main__":
    main()
    
    
     
    
    
    
    

    
    
    
    
    
    
    
