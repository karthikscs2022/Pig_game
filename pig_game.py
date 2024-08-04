import random

# Function to return a random value between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Getting the input of how many players would like to play
while True:
    players = input("Enter the number of Players (2-4): ")
    if players.isdigit():  # Checks if the input string is a valid digit or not
        players = int(players)  # Typecasting the string to int
        if 2 <= players <= 4:
            break
        else:
            print("Must be 2-4 players.")
    else:
        print("Invalid number, try again!")

max_score = 50
# Initialize scores to 0 for every player using list comprehension
player_scores = [0 for _ in range(players)]

# Main game loop, runs until one player reaches the max_score
while max(player_scores) < max_score:
    # Loop through each player using their index
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "has started\n")
        print("Your current score is", player_scores[player_idx], "\n")
        current_score = 0  # Current score for this turn is set to 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":  # Convert the string to lower to check for 'y'
                break

            value = roll()
            if value == 1:
                print("You rolled a 1, turn done")
                current_score = 0
                break
            else:
                current_score += value  # Add the rolled value to the current score
                print("You rolled a:", value)

            print("Your score is:", current_score)

        # Add the current score of this turn to the player's total score
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Determine the player with the maximum score
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "is the winner with the score of:", max_score)
