import requests
import random
import html

API_BASE = "https://[Log in to view URL]"

def fetch_trivia(category=None, difficulty=None, qtype="multiple", amount=5):
    """Fetches trivia questions from the Open Trivia Database API."""
    
    params = {"amount": amount, "type": qtype}
    
    if category:
        try:
            params["category"] = int(category)  # ensure correct type
        except ValueError:
            print("Invalid category. Ignoring it.")
    
    if difficulty:
        params["difficulty"] = difficulty.lower()

    try:
        resp = requests.get(API_BASE, params=params, timeout=8)
    except requests.RequestException as e:
        print(f"[Network error] {e}")
        return None

    if resp.status_code != 200:
        print(f"[API error] Status code: {resp.status_code}")
        return None

    try:
        data = resp.json()
    except ValueError:
        print("[Parse error] Invalid JSON response")
        return None

    if data.get("response_code") != 0:
        print(f"[API error] response_code={data.get('response_code')}")
        return None

    return data.get("results", [])

# ================================
def ask_quiz(questions):
    """Asks the user trivia questions and checks answers."""
    
    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(opt) for opt in q["incorrect_answers"]] + [correct]

        random.shuffle(options)

        print(f"\nQuestion {i}/{total}: {question}")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

        while True:
            choice = input("Your answer (number): ").strip()
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            
            choice = int(choice)
            if 1 <= choice <= len(options):
                break
            else:
                print("Invalid choice. Try again.")

        selected = options[choice - 1]

        if selected == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {correct}")

    print(f"\nYour final score: {score}/{total}")
    return score, total

def main():
    print("Welcome to the Trivia Quiz!")

    try:
        amount = int(input("How many questions? (default 5): ") or 5)
    except ValueError:
        amount = 5

    amount = max(1, min(20, amount))

    category = input("Enter category ID (or leave blank): ").strip()
    difficulty = input("Enter difficulty (easy, medium, hard or blank): ").strip().lower()

    print("\nFetching questions...")
    questions = fetch_trivia(category=category, difficulty=difficulty, amount=amount)

    if not questions:
        print("No questions available. Try again later.")
        return

    score, total = ask_quiz(questions)

    percentage = round((score / total) * 100)
    print(f"Score Percentage: {percentage}%")


if __name__ == "__main__":
    main()