import subprocess
import Passwords as pd
# import time
def unlock_device_with_password(password):
    # Input the password via adb shell input text
    cmd_input_password = f"adb shell input text {password}"
    subprocess.run(cmd_input_password, shell=True)

    # Simulate pressing the Enter key via adb shell input keyevent
    cmd_press_enter = "adb shell input keyevent 66"
    subprocess.run(cmd_press_enter, shell=True)

    # Wait for a brief moment (adjust as needed)
    # time.sleep(1)
def choose_Type():
    a = chr(9673)
    b = chr(9445)
    print(f"{a} For unlocking 4-digit Number :- 1")
    print(f"{a} For unlocking 6-digit Number :- 2")
    print(f"{a} For unlocking small alphabet :- 3")
    print(f"{a} For unlocking Big alphabet :- 4")
    print(f"{a} For unlocking Mixed-digit alphabet :- 5")
    user_input = int(input(f"{b} Enter your unlock Mode: "))
    if user_input == 1:
        while True:
            four = pd.Four_digit()
            unlock_device_with_password(four)
    elif user_input == 2:
        while True:
            six = pd.Six_digit()
            unlock_device_with_password(six)
    elif user_input == 3:
        lenth = int(input("What is the length of your password:- "))
        while True:
            Small = pd.Small_Chractes(lenth)
            unlock_device_with_password(Small)
    elif user_input == 4:
        lenth = int(input("What is the length of your password:- "))
        while True:
            Big = pd.Big_Chractes(lenth)
            unlock_device_with_password(Big)
    elif user_input == 5:
        lenth = int(input("What is the length of your password:- "))
        while True:
            mix = pd.mix_Chractes(lenth)
            unlock_device_with_password(mix)
    else:
        print("Invalid Choice")
choose_Type()