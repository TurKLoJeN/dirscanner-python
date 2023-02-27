import pyfiglet
import requests
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("|| Welcome ||")

print(ascii_banner)

print(colored("All responsibility belongs to the user","red"))

url = input("Please enter a url example "+colored("(https://google.com): ","green"))
secim = input("1- Big List \n2- Medium List \n3- Medium List(2) \n4- Small List \n5- Exit\nChoose: ")

while True:
    try: 
        if secim == "1":
            with open("list/big.txt", "r") as f:
                dizinler = f.read().splitlines()

            for dizin in dizinler:
                test_url = f"{url}/{dizin}/"
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(colored(f"{test_url} OK","green"))
                else:
                    print(colored(f"{test_url} NOT WORKING","red"))
        elif secim == "2":
            with open("list/medium.txt", "r") as f:
                dizinler = f.read().splitlines()

            for dizin in dizinler:
                test_url = f"{url}/{dizin}/"
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(colored(f"{test_url} OK","green"))
                else:
                    print(colored(f"{test_url} NOT WORKING","red"))
        elif secim == "3":
            with open("list/medium2.txt", "r") as f:
                dizinler = f.read().splitlines()

            for dizin in dizinler:
                test_url = f"{url}/{dizin}/"
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(colored(f"{test_url} OK","green"))
                else:
                    print(colored(f"{test_url} NOT WORKING","red"))
        elif secim == "4":
            with open("list/small.txt", "r") as f:
                dizinler = f.read().splitlines()

            for dizin in dizinler:
                test_url = f"{url}/{dizin}/"
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(colored(f"{test_url} OK","green"))
                else:
                    print(colored(f"{test_url} NOT WORKING","red"))
        elif secim=="5":
            break
    except ValueError:
        print(colored("Incorrect selection or URL","yellow"))
