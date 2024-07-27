import subprocess
from Passwords import Passwords  # Make sure the Passwords class is in a file named Passwords.py

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
            password = passwd.Four_digit()
            unlock_device_with_password(password)

    elif choice == 2:
        while True:
            password = passwd.Six_digit()
            unlock_device_with_password(password)

    elif choice == 3:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.Small_Chractes(length)
            unlock_device_with_password(password)

    elif choice == 4:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.Big_Chractes(length)
            unlock_device_with_password(password)

    elif choice == 5:
        length = int(input("Enter the length of your password: "))
        while True:
            password = passwd.mix_Chractes(length)
            unlock_device_with_password(password)

    else:
        print("Invalid Choice")

if __name__ == "__main__":
    adb = input("Are you connected with ADB y/n: ").lower()
    if adb == "y":
        unlock_device_menu()
    else:
        pwd = Passwords()
        print(f" Unique Password -{pwd.Unique_password()}")
        print(f" Four Digit - {pwd.Four_digit()}")
        print(f" Six Digit - {pwd.Six_digit()}")
        print(f" Small Character - {pwd.Small_Chractes(10)}")
        print(f" Big Chracter -{pwd.Big_Chractes(10)}")
        print(f" Mix Chracters - {pwd.mix_Chractes(10)}")
        print(f" Random Phone Number - {pwd.Phone_number()}")