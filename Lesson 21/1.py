import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            fact_data = response.json()
            fact = fact_data.get("text").lower()

            # Check if it's a technology-related fact
            
            keywords = ["technology", "computer", "internet", "software", "hardware", "programming", "AI", "artificial intelligence"]

            if any(keyword in fact for keyword in keywords):
                print(f"Random Technology Fact: {fact}")
                break
        else:
            print(f"Error fetching fact: {response.status_code}")
            break
while True:
    user_input = input("Press enter to get a random technology fact: ")
    if user_input.lower().strip() == "q":
        print("Exiting the program.")
        break
    get_random_fact()