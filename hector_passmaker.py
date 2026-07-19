import random
import time
import string
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
    length = input("How many characters would you like your password to be? ")
    letters = input("How many letters should it contain? ")
    numbers = input("How many numbers should it contain? ")
    symbols = input("How many special characters (symbols) should it contain")

    
    
    
    
