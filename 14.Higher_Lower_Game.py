import art
print(art.logo)
import random
import game_data

chosen1 = random.choice(game_data.data)
score = 0
game_over = False
while not game_over:
    chosen2 = random.choice(game_data.data)
    if chosen1 == chosen2:
        chosen2 = random.choice(game_data.data)
    print(f"Compare A: {chosen1['name']}, a {chosen1['description']}, from {chosen1['country']}.")
    print(art.vs)
    print(f"Against B: {chosen2['name']}, a {chosen2['description']}, from {chosen2['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if chosen1['follower_count'] > chosen2['follower_count'] and answer == "a":
        score += 1
        print(f"You are right! Current score: {score}")
    elif chosen2['follower_count'] > chosen1['follower_count'] and answer == "b":
        score += 1
        print(f"You are right! Current score: {score}")
        chosen1 = chosen2
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
