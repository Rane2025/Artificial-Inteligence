import random, re
from colorama import Fore, init
init(autoreset = True)

dest = {
"beaches": ["Bali", "Maldives", "Phuket"],
"mountains": ["Alps", "Rockies", "Himalayas"],
"cities": ["Tokyo", "Paris", "NYC"]
}

jokes = [
"Programmers hate nature—too many bugs!",
"Computer sick? Must be a virus!",
"Travelers are warm from hot spots!"
]

clean = lambda t: re.sub(r"\s+", " ", t.lower().strip())


def recommend():
    p = clean(input(Fore.CYAN + "Beaches, mountain or cities"))
    if p in dest:
        print(Fore.GREEN + f"Try {random.choice(dest[p])}!")
    else:
        print(Fore.RED + "Not an option.")

def pack():
    d = clean (input(Fore.CYAN + "How many days?"))
    print(Fore.GREEN + f"Tips for {d} days: clothes, chargers, weather check")

def chat():
    print(Fore.CYAN + "TravelBot (type recommend / pack / joke / exit)")
    while True:
        c = clean(input(Fore.YELLOW + "> "))
        if c == "recommend": recommend()
        elif c == "pack": pack()
        elif c == "joke": print(Fore.YELLOW + random.choice(jokes))
        elif c == "exit": break
        else: print("Try again. ")

chat()
        