# joke fetcher using the Official Joke API
import requests
API_URL = "https://official-joke-api.appspot.com/random_joke"

def get_random_joke():
    """Fetches a random joke from the API and returns it as a string."""
    try:
        resp = requests.get(API_URL, timeout = 5)   # set a timeout to avoid hanging
    except requests.RequestException as e:
        # network error or request problem
        return f"An error occurred: {e}"
    
    if resp.status_code != 200:
        return f"Error: Received status code {resp.status_code}"
    
    try:
        data = resp.json() # parse JSON into python dict
    except ValueError:
        return "Error: Failed to parse JSON response"
    
    # Safely get the fields we expect
    setup = data.get("setup", "No setup found")
    punchline = data.get("punchline", "No punchline found")
    if not setup or not punchline:
        return "Error: Joke data is incomplete"
    
    return f"{setup} {punchline}"

def main():
    print("Random Joke Generator (press ENTER to get a joke, or type 'exit' to quit)")
    while True:
        user_input = input("Press ENTER for a joke or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        joke = get_random_joke()
        print(joke)
if __name__ == "__main__":
    main() 