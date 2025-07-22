import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("❌ Invalid input. Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n📢 Result: {result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\n🔁 Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n👋 Thanks for playing! Final Score:")
            print(f"🧑 You: {user_score} | 💻 Computer: {computer_score}")
            break

        round_number += 1

# Run the game
play_game()