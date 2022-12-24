#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

def save_data(data, filename):
    # Save the data to a file
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    # Load the data from the file
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def print_data(data):
    # Print the data in a tabular format
    print("Player\t\t\tAttacks\t\tAbility Checks\t\tSaving Throws")
    print("-" * 70)
    for player, rolls in data.items():
        print("{}\t\t{} nat20s, {} nat1s\t{} nat20s, {} nat1s\t{} nat20s, {} nat1s".format(player, rolls['atk']['nat20'], rolls['atk']['nat1'], rolls['abc']['nat20'], rolls['abc']['nat1'], rolls['svt']['nat20'], rolls['svt']['nat1']))

def main():
    # Load the data from the file, or create an empty dictionary if the file doesn't exist
    try:
        data = load_data('dice_rolls.json')
    except FileNotFoundError:
        data = {}

    
        # Get the player's name and the roll from the user
    player = input("Enter the player's name: ")
    roll_type = input("Enter 'atk' for an attack, 'abc' for an ability check, or 'svt' for a saving throw: ")
    roll = input("Enter 'nat20' for a natural 20 or 'nat1' for a natural 1: ")

        # Increment the count for the player's rolls
    if player in data:
        if roll_type == 'atk':
            if roll == 'nat20':
                data[player]['atk']['nat20'] += 1
            elif roll == 'nat1':
                data[player]['atk']['nat1'] += 1
        elif roll_type == 'abc':
            if roll == 'nat20':
                data[player]['abc']['nat20'] += 1
            elif roll == 'nat1':
                data[player]['abc']['nat1'] += 1
        elif roll_type == 'svt':
            if roll == 'nat20':
                data[player]['svt']['nat20'] += 1
            elif roll == 'nat1':
                data[player]['svt']['nat1'] += 1
    else:
        if roll == 'nat20':
            data[player] = {'atk': {'nat20': 1, 'nat1': 0}, 'abc': {'nat20': 0, 'nat1': 0}, 'svt': {'nat20': 0, 'nat1': 0}}
        elif roll == 'nat1':
            data[player] = {'atk': {'nat20': 0, 'nat1': 1}, 'abc': {'nat20': 0, 'nat1': 0}, 'svt': {'nat20': 0, 'nat1': 0}}
        
        
    save_data(data, 'dice_rolls.json')
    saved = load_data('dice_rolls.json')
    print_data(saved)
    
if __name__ == "__main__":
    main()


# In[ ]:


write()


# In[ ]:





# In[ ]:




