import re

def is_game_possible(game_rounds, max_red, max_green, max_blue):
    # Check if any round in the game exceeds the maximum limits
    for round_info in game_rounds:
        red = green = blue = 0
        # Extract the counts of each color in the round
        if "red" in round_info:
            red = int(re.search(r'(\d+) red', round_info).group(1))
        if "green" in round_info:
            green = int(re.search(r'(\d+) green', round_info).group(1))
        if "blue" in round_info:
            blue = int(re.search(r'(\d+) blue', round_info).group(1))
        
        # Check if any color exceeds the maximum allowed cubes
        if red > max_red or green > max_green or blue > max_blue:
            return False
    return True

def sum_of_possible_game_ids(game_data, max_red, max_green, max_blue):
    total_sum = 0
    for game in game_data:
        # Split the game input into game ID and the list of rounds
        game_id, rounds = game.split(": ")
        game_id = int(re.search(r'\d+', game_id).group(0))  # Extract the game ID
        
        # Split the rounds
        rounds = rounds.split("; ")
        
        # Check if the game is possible
        if is_game_possible(rounds, max_red, max_green, max_blue):
            total_sum += game_id
    
    return total_sum

# Example input
game_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# Maximum number of cubes in the bag
max_red = 12
max_green = 13
max_blue = 14

# Calculate the sum of possible game IDs
result = sum_of_possible_game_ids(game_data, max_red, max_green, max_blue)
print("Total sum of possible game IDs:", result)
