import random

class Passwords:
    def __init__(self):
        self._lower_number = '0123456789'
        self._lower_letter = 'abcdefghijklmnopqrstuvwxyz'
        self._upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._symbols = '!@#$%^&*()_+=-'
        self._mix_number = "qwertyuiopasdfghjklzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM1234567890-=[]|;'./,<>?:{}+_!@#$%^&*()"
        self._phone_number = [90, 96, 99, 80, 62, 85]

    def Four_digit(self):
        return str(random.randint(1000, 9999))


    def Six_digit(self):
        return str(random.randint(100000, 999999))

    def Small_Chractes(self, length):
        return ''.join(random.choice(self._lower_letter) for _ in range(length))

    def Big_Chractes(self, length):
        return "".join(random.choice(self._upper_letter) for _ in range(length))
        
    def mix_Chractes(self, length):
        return "".join(random.choice(self._mix_number) for _ in range(length))
        
    def Phone_number(self):
        return f"+91{str(random.choice(self._phone_number)) + str(random.randint(10000000, 99999999))}"

    def Unique_password(self, password_for="Google"):
        chr = "#@*& "
        length = len(password_for)
        a = random.choice(chr)
        alg = length * (length-1)
        alg2 = int(alg / 2)

        b = random.choice(chr)
        total = f"{password_for}-{a*3}{alg2}{b*3}"
        return total


if __name__ == "__main__":
    passwd = Passwords()
