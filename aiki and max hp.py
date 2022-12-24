#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os

def load_scores(score_file):
    # Check if the score file exists
    if not os.path.exists(score_file):
        # If the file doesn't exist, create an empty dictionary
        return {}
    else:
        # If the file exists, read the scores from it
        with open(score_file, "r") as f:
            return json.load(f)

def update_score(score_file, player, aiki, max_hp):
    # Load the scores from the file
    scores = load_scores(score_file)

    # Update the scores for the player
    if player in scores:
        scores[player]["+1 aiki"] += aiki
        scores[player]["-1 max hp"] += max_hp
    else:
        scores[player] = {"+1 aiki": aiki, "-1 max hp": max_hp}

    # Write the updated scores back to the file
    with open(score_file, "w") as f:
        json.dump(scores, f)

def display_scores(score_file):
    # Load the scores from the file
    scores = load_scores(score_file)

    # Print the scores in a tabular format
    print("Player\t+1 aiki\t-1 max hp")
    print("------\t-------\t----------")
    for player, categories in scores.items():
        print("{}\t{}\t\t{}".format(player, categories["+1 aiki"], categories["-1 max hp"]))

def reset_scores(score_file):
    # Wipe the contents of the file by writing an empty dictionary to it
    with open(score_file, "w") as f:
        json.dump({}, f)

def main():
    score_file = "scores.json"

        # Get the player's name and actions
    player = input("Enter player name: ")
    aiki = int(input("Enter +1 aiki action: "))
    max_hp = int(input("Enter -1 max hp action: "))

        # Update the score
    update_score(score_file, player, aiki, max_hp)

        # Display the updated scores
    display_scores(score_file)

        # Check if the user wants to reset the scores
    reset = input("Reset scores? (y/n) ")
    if reset.lower() == "y":
        reset_scores(score_file)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




