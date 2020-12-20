import sys
import os



def start_screen():
    print("Welcome to Eliot Password Profiler\n")
    print("     1. Creat a profile")
    print("     2. Load a profile")
    print("     3. Help")
    print("     4. Exit\n")
    mode = 0
    while True:
        try:
            choice = int(input("        > Enter a Choice: "))
            if choice == 1:
                mode = 1
                break
            elif choice == 2:
                mode = 2
                break
            elif choice == 3:
                mode = 3
                break
            elif choice == 4:
                mode = 4
                break
            else:
                continue
        except:
            continue
    return mode


def create_wordlist():
    profile = {}
    os.system("clear")
    profile["name"] = input(" > First Name: ").lower()
    profile["surname"] = input(" > Surname: ").lower()
    profile["nickname"] = input(" > Nickname: ").lower()
    birthdate = input(" > Birthdate(DDMMYYYY): ")

    while len(birthdate) != 8 and len(birthdate) != 0:
        birthdate = input(" > Birthdate(DDMMYYYY): ")

    profile["birthdate"] = str(birthdate)
    profile["child"] = input(" > Childs Name: ").lower()
    childs_birthdate = input(" > Childs Birthdate(DDMMYYYY): ")

    while len(childs_birthdate) != 0 and len(childs_birthdate) != 8:
        childs_birthdate =  input(" > Childs Birthdate(DDMMYYYY): ")

    profile["childs_birthdate"] = str(childs_birthdate)
    profile["ped"] = input(" > Ped: ").lower()
    profile["company"] = input(" > Company: ").lower()
    choice = 0
    while True:
        value = input(" > Do you want to add some more information[Y][N]: ").lower()
        if value == "y":
            choice = 1
            break
        elif value == "n":
            choice = 2
            break
        else:
            print("[!] Choice not excepted")
            continue

    if choice == 1:
        words = input(" > Please enter the words comma separated [hacker,mrrobot,evilcorb]: ")
        profile["more_words"] = words.split(",")
    if choice == 2:
        print("Ok")
    choice = 0
    while True:
        value = input(" > Do you want to add some special characters[Y][N]: ").lower()
        if value == "y":
            choice = 1
            break
        elif value == "n":
            choice = 2
            break
        else:
            print("[!] Choice not excepted")
            continue
    profile["specialchars"] = value
    return profile



def generate_wordlist_from_profile(profile):
    print("\n")
    print("\n")
    print("\n")
    print("[*] Generating wordlist from the victim ...")
    specialchars = []
    if profile["specialchars"] == "y":
        specialchars.append("!")
        specialchars.append("?")
    birthdate_pwd = []
    birthdate_pwd.append(profile["birthdate"])
    birthdate_pwd.append(profile["birthdate"[-2:]])
    birthdate_pwd.append(profile["birthdate"[-3:]])
    birthdate_pwd.append(profile["birthdate"[-4:]])
    birthdate_pwd.append(profile["birthdate"[2:4]])
    birthdate_pwd.append(profile["birthdate"[1:4]])
    birthdate_pwd.append(profile["birthdate"[1:2]])
    birthdate_pwd.append(profile["birthdate"[1:4]])








def main():
    mode = 0
    mode = start_screen()
    if mode == 4:
        sys.exit(0)
    elif mode == 1:
        profile = create_wordlist()
    generate_wordlist_from_profile(profile)

if __name__ == "__main__":
    main()

