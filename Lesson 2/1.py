# !IMPORT NECCARY LIBRARYS!
from colorama import Fore, Style, init
from textblob import TextBlob

init()

print(f"{Fore.CYAN}Welcome to the SENTIMENT SPY{Style.RESET_ALL}")
name = input(f"{Fore.MAGENTA}Enter your name{Style.RESET_ALL}").strip() or "Mystery Agent"

history = []

print(f"""{Fore.CYAN} Hello, Agent {name}!
Type a sentence to analyze sentiment.
Commands: 'history', 'reset', 'exit'
{Style.RESET_ALL}""")

def sentiment_info(text):
    p = TextBlob(text).sentiment.polarity
    if p > 0.25: return p, "Postive", Fore.GREEN
    if p < -0.25: return p, "Negative", Fore.RED
    return p, "Neutral", Fore.YELLOW

while True:
    text = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not text:
        print(f"{Fore.RED}Enter valid text.{Style.RESET_ALL}")
        continue

    cmd = text.lower()
    if cmd == "exit":
        print(f"{Fore.BLUE}👋 Goodbye, Agent {name}!{Style.RESET_ALL}")
        break
    if cmd == "reset":
        history.clear()
        print(f"{Fore.CYAN}🧹 History cleared!{Style.RESET_ALL}")
        continue
    if cmd == "history":
        if not history:
            print(f"{Fore.YELLOW}No history yet.{Style.RESET_ALL}")
        else:
            for i, (t, p, s, c, e) in enumerate(history, 1):
                print(f"{i}. {c}{e} {t} ({p:.2f}, {s}){Style.RESET_ALL}")
        continue

    p, s, c, e = sentiment_info(text)
    history.append((text, p, s, c, e))
    print(f"{c}{e} {s} sentiment detected! ({p:.2f}){Style.RESET_ALL}")0