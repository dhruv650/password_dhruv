import random
def Four_digit():
    a = 0
    while True:
        password = str(random.randint(1000, 9999))
        return password
def Six_digit():
    a = 0
    while True:
        rmd = str(random.randint(100000, 999999))
        return rmd
def Small_Chractes(ienth):
    Chractres = "qwertyuiopasdfghjklzxcvbnm"
    a = 0
    def process():
        password = ""
        for i in range(ienth):
            password += random.choice(Chractres)
        return password
    while True:
        # process()
        print(f"Trying :- {process()}")
        return process()

def Big_Chractes(ienth):
    Chractres = "ASDFGHJKLPOIUYTREWQZXCVBNM"
    a = 0
    def process():
        password = ""
        for i in range(ienth):
            password += random.choice(Chractres)
        return password

    while True:
        print(f"Trying :- {process()}")
        return process()

def mix_Chractes(ienth):
    Chractres = "qwertyuiopasdfghjklzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM1234567890-=[]|;'./,<>?:{}+_!@#$%^&*()"
    a = 0
    def process():
        password = ""
        for i in range(ienth):
            password += random.choice(Chractres)
        return password

    while True:
        process()
        print(f"Trying :- {process()}")
        return process()

