import requests
import json
import random

def trivia_fetch(num):
    """
    Fetches trivia about a specific number from numbersapi.com
    
    Args:
        num (int): Number to get trivia about
        
    Returns:
        dict: Dictionary with number trivia (includes 'number' and 'text')
    """
    try:
        response = requests.get(f"http://numbersapi.com/{num}?json")
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trivia: {e}")
        return {"number": num, "text": f"Could not get trivia for number {num}"}

def show_menu():
    """Displays the main quiz menu"""
    print("\n" + "="*40)
    print("   NUMBER TRIVIA QUIZ")
    print("="*40)
    print("\n1. Play with a specific number")
    print("2. Play with a random number")
    print("3. Verify trivia_fetch function")
    print("4. Exit")
    return input("\nSelect an option (1-4): ")

def play_trivia(num=None):
    """
    Interactive number trivia game
    
    Args:
        num (int, optional): Specific number. If None, uses random number.
    """
    if num is None:
        trivia = trivia_fetch(random.randint(1, 1000))
    else:
        trivia = trivia_fetch(num)
    
    print(f"\n🔢 Number: {trivia['number']}")
    print(f"📖 Trivia: {trivia['text']}")
    
    # Mini guessing game
    if num is None:
        input("\nPress Enter to continue...")

def verify_function():
    """Verifies the trivia_fetch function with test cases"""
    print("\n🔍 Verifying trivia_fetch function...")
    print("Test 1 (number 42):", "✅ Passed" if trivia_fetch(42)["number"] == 42 else "❌ Failed")
    print("Test 2 (number 1000):", "✅ Passed" if trivia_fetch(1000)["number"] == 1000 else "❌ Failed")

def main():
    """Main program function"""
    print("\nWelcome to the Number Trivia Quiz!")
    print("Discover interesting facts about numbers.")
    
    while True:
        option = show_menu()
        
        if option == "1":
            try:
                num = int(input("\nEnter a number: "))
                play_trivia(num)
            except ValueError:
                print("Please enter a valid number.")
        elif option == "2":
            play_trivia()  # Random number
        elif option == "3":
            verify_function()
        elif option == "4":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid option. Please choose between 1-4.")

if __name__ == "__main__":
    main()