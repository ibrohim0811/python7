mson1 = int(input("1 - taxminiy manfiy yoki musbat son kiriting!: "))
mson2 = int(input("2 - taxminiy manfiy yoki musbat son kiriting!: "))
if mson1 < 0:
    print(f"{mson1} manfiy son")
else:
    print(f"{mson1} musbat son")
if mson2 < 0: 
    print(f"{mson2} manfiy son!")
else: 
    print(f"{mson2} musbat son!")
age = int(input("Yoshingizni kiriting!: "))
if age < 18:
    print("yoshingiz yetarli emas!")
else:
    print("Xush kelibsiz!")
son1 = int(input("taxminiy 1ta 1-sonni kiriting!: "))
son2 = int(input("taxminiy 1ta 2-sonni kiriting!: "))
if son1 < son2:
    print(f"{son1} kichik {son2} dan")
else:
    print(f"{son1} katta {son2} dan")
b1 = int(input("1- bahoni kiriting!: "))
b2 = int(input("2- bahoni kiriting!: "))
b3 = int(input("3- bahoni kiriting!: "))
b4 = int(input("4- bahoni kiriting!: "))
b5 = int(input("5- bahoni kiriting!: "))
um = b1 + b2 + b3 + b4 + b5
ums = um / 5
print(f"sizning orta bahoyingiz {ums}!")
login = input("Enter your email: ")
pas = input("Enter your password: ")

if not " " in login and login.endswith("@gmail.com") and len(pas) == 8:
    print("Successful!")
else:
    print("Something went wrong! Please try again later!")
