import requests
import random
import html

API_BASE = "https://opentdb.com/api.php"
def fetch_trivia(category=None, difficulty=None, qtype="multiple", amount = 5):
    """Fetches trivia questions from the Open Trivia Database API."""
    params  = {"amount" : amount, "type" : qtype}
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    
    try:
        resp = requests.get(API_BASE, params=params, timeout=8)# sec
    except requests.RequestException as e:
        print(f"Error fetching trivia: {e}")
        return []
    
    if resp.status_code != 200:
        print(f"Error: Received status code {resp.status_code}")
        return []
    
    try:
        data = resp.json()
    except ValueError:
        print("Error: Failed to parse JSON response")
        return None
    
    # API returns a response code in the JSON to indicate success or failure
    if data.get("response_code") != 0:
        print(f"API Error: Response code {data.get('response_code')}")
        return None
    
    return data.get("results", [])

def ask_quiz(questions):
    """Asks the user the trivia questions and checks their answers."""
    score = 0
    for q in questions:
        print("\n" + html.unescape(q["question"]))
        options = q["incorrect_answers"] + [q["correct_answer"]]
        random.shuffle(options)
        for i, option in enumerate(options):
            print(f"{i+1}. {html.unescape(option)}")
        
        while True:
            try:
                choice = int(input("Your answer (number): "))
                if 1 <= choice <= len(options):
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        
        if options[choice - 1] == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {html.unescape(q['correct_answer'])}")
    
    print(f"\nYour final score: {score}/{len(questions)}")

def main():
    print("Welcome to the Trivia Quiz!")
    category = input("Enter a category (or leave blank for any): ")
    difficulty = input("Enter difficulty (easy, medium, hard, or leave blank): ")
    
    questions = fetch_trivia(category=category, difficulty=difficulty)
    if questions:
        ask_quiz(questions)
    else:
        print("No questions available. Please try again later.")

if __name__ == "__main__":
    main()