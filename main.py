"""
This is the main file of the password generator
"""

import time
import random
import string
import os
import tqdm
import math
import hashlib

import math

def calculate_password_strength(password):
    # Define the character sets and their corresponding sizes
    char_sets = [
        {"chars": "abcdefghijklmnopqrstuvwxyz", "size": 26},
        {"chars": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "size": 26},
        {"chars": "0123456789", "size": 10},
        {"chars": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~", "size": 32}
    ]

    # Calculate the size of the password's character set
    password_char_set_size = 1
    for char_set in char_sets:
        if any(char in char_set["chars"] for char in password):
            password_char_set_size *= char_set["size"]

    # Calculate the number of possible passwords of the same length
    possible_passwords = password_char_set_size ** len(password)

    # Assume 100 billion attempts per second (a reasonable estimate for modern GPUs)
    attempts_per_second = 1e11

    # Calculate the cracking time in seconds
    cracking_time_seconds = possible_passwords / attempts_per_second

    # Convert the cracking time to years
    cracking_time_years = cracking_time_seconds / (60 * 60 * 24 * 365)

    return cracking_time_years


def generate_password(length):
    """
    Generate a password

    Parameters:
    length (int): The length of the password to generate.

    Returns:
    str: The generated password.
    """
    total_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(total_chars) for _ in tqdm.tqdm(range(length)))
    return password

def main():
    #length = int(input("Length of your password (recommended: 15, normal: 8, easy: 6): ") or 15)
    length = 15
    attempts = 0
    print("Password is generating...")
    while True:
        password = generate_password(length)
        if calculate_password_strength(password) > 2e+16 or attempts > 25:
            print(calculate_password_strength(password))
            break
        attempts += 1
    print("Generated password:", password)

if __name__ == "__main__":
    main()
