import random
from art import logo, vs
from game_data import data


def display_comparison(item_a, item_b, vs_logo):
    """Display the comparison between two items"""
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(vs_logo)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}\n")


def get_user_choice():
    """Get and validate user input"""
    while True:
        answer = input("Who has more followers? Type A or B: ").upper()
        if answer in ['A', 'B']:
            return answer
        print("Please enter A or B only.")


def is_correct_guess(item_a, item_b, user_answer):
    """Check if user's guess is correct"""
    a_followers = item_a['follower_count']
    b_followers = item_b['follower_count']

    if a_followers > b_followers:
        return user_answer == 'A'
    else:
        return user_answer == 'B'


def create_comparison_pair(data_list, used_pairs):
    """Create a new comparison pair that hasn't been used before"""
    max_attempts = 50  # Prevent infinite loops
    attempts = 0

    while attempts < max_attempts:
        item_a = random.choice(data_list)
        item_b = random.choice(data_list)

        # Ensure different items
        if item_a != item_b:
            pair = tuple(sorted([item_a['name'], item_b['name']]))
            if pair not in used_pairs:
                used_pairs.add(pair)
                return item_a, item_b

        attempts += 1

    # Fallback if we've exhausted combinations
    return random.choice(data_list), random.choice(data_list)


def play_round(data_list, used_pairs, vs_logo):
    """Play a single round of the game"""
    item_a, item_b = create_comparison_pair(data_list, used_pairs)
    display_comparison(item_a, item_b, vs_logo)
    user_answer = get_user_choice()
    return is_correct_guess(item_a, item_b, user_answer)


def play_game(data_list, logo, vs_logo):
    """Main game loop"""
    print(logo)
    score = 0
    used_pairs = set()

    while True:
        if play_round(data_list, used_pairs, vs_logo):
            score += 1
            print(f"You're right! Current score: {score}")
            print("\n" * 3)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    return score


# Game execution
if __name__ == "__main__":
    # Assuming these variables exist in your environment
    final_score = play_game(data, logo, vs)
    print("Game over!")