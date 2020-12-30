# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:11:09 2020

@author: mdurr
"""

def view_meals():
    '''This is the function that will run when someone selects option
    3 from the menu
    
    Just prints a list of available meals'''
    
    meals = list(meals_dict['name'].values)
    
    print("Your")

choice = int(input('''What do you want to do?
1: Get a meal suggestion
2: Add new meal
3: Check my meals

What do you want to do? '''))

try:
    if choice == 1:
        # meal suggestion function
    elif choice == 2:
        # meal input function
    elif choice ==3:
        # check meal function

except:
    print("Please choose 1, 2 or 3.")

### Clear the screen when they input their selection

# Stage 1 - limit by protein
print('''Let's make some food
What kind of protein do you have?''')
print('')
protein = input("Protein: ")
protein = protein.lower()

# Remove this - just for checking
print("You're in the mood for {}".format(protein))

# Stage 2 - carb
carb = input("What carb do you have? ")

# Stage 3 - vegetables
veg = input("How about vegetables? ")

# Stage 4 - cuisine
cuisine = input("What type of cuisine are you feeling? ")

# Stage 5 - type of food
kind = input("Lastly, are you feeling like any kind of meal in particular? ")

      