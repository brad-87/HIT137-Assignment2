# Question 1 – Encryption & Decryption

## Overview

This program will read a text file, encrypt it's contents using specific shift rules, then will decrypt the result then verify that the original text is correct.

## Features

* Reads input from `raw_text.txt`
* Runs encryption based on inputs (`shift1`, `shift2`)
* Writes encrypted output to `encrypted_text.txt`
* Decrypts back to `decrypted_text.txt`
* Verifies if the decrypted file matches the original

## How to Run

1. Ensure `raw_text.txt` is in the same directory
2. Run the program:

   ```
   python main.py
   ```
3. Enter values for `shift1` and `shift2` when prompted

## Notes

* Non-alphabetic characters remain unchanged
* The program will notify the user if verification was successful
