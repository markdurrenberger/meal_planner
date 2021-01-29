# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:11:09 2020

@author: mdurr

Functions for the menu of my meal planner application
-- : these are functions still to be created

Functions within this script:
* main_menu()
1: get_recommendation()
2: add_meal()
3: view_meals()

*del_meal()
--meal_details()
"""
# Main Menu
def main_menu():
    import os

    while True:
        os.system('cls')
        print('MAIN MENU')
        print('-----------------\n')
        choice = int(input('''1: Get meal suggestion
2: Add a meal
3: Check my meals
-----------------
What do you want to do? '''))
        if choice not in (1, 2, 3):
            print('\nPlease choose 1, 2 or 3')
            continue
        elif choice == 1:
            get_recommendation()
            break
        elif choice == 2:
            add_meal()
            break
        elif choice == 3:
            view_meals()
            break

# Option 1 - Get Meal Recommendation
def get_recommendation():
    import os
    os.system('cls')

    print('Option 1 - Get Meal Recommendation')

    # Load the current directory of meals
    import pickle
    f = open('meals.pkl', 'rb')
    meals = pickle.load(f)
    f.close()

    # Get user inputs for types of meals
    protein = input("What protein would you like? ").lower().strip()

    ### I'll figure out the protein part first, then expand to cuisines or tags
    # cuisine =
    # tag =

    # Create a subset of all the meals that contain the specified protein
    subset = []
    for meal in meals:
        for ingredient in meal['ingredients'].keys():
            if protein in ingredient:
                subset.append(meal)
                break
            else:
                continue

    # While loop to keep offering meals until user accepts one or run out of options
    import random
    #For changing display message
    ticker = 0

    while True:
        # Get initial recommendation
        recommendation = random.choice(subset)

        # Remove that meal from subset
        subset.remove(recommendation)

        # Display choice and ask for confirmation
        os.system('cls')
        if ticker == 0:
            print("A great meal with {} is: {}".format(protein, recommendation['name']))
        elif not subset:
            print("The last option with {} is: {}".format(protein, recommendation['name']))
        else:
            print("Another great meal with {} is: {}".format(protein, recommendation['name']))
        print("-----------------------------------------------------------")
        print("Do you want to make that meal (y) or get another option(n)?")
        confirm = input("Enter 'y' or 'n': ").lower().strip()

        # Either keep loop going, or end it
        if confirm == 'y':
            # placeholder - will get replaced with meal_details() function
            os.system('cls')
            meal_details(meals.index(recommendation)+1)
            input('Press Enter when done......')
            quit()

        # When the subset of meals is empty, need to get another option
        if not subset:
            os.system('cls')
            print("There are no more meals with {} left.".format(protein))
            print("Maybe you'd prefer something else?")
            input("Press Enter to continue...")
            get_recommendation()

        # update ticker
        ticker += 1


# Option 2 - Add a New Meal
def add_meal():
    '''This function will ask the user for inputs to create a new meal, then add the meal
    to the meals database and print to file.'''
    import os
    os.system('cls')

    print('Option 2 - Add a Meal\n')
    # Load the meals list from file
    import pickle
    f = open('meals.pkl', 'rb')

    meals = pickle.load(f)

    # Create new_meal (a dict that gets populated through inputs) then append to meals at end
    new_meal = dict()

    ### Ask user for inputs (store all as lowercase)
    # Ask user for name
    os.system('cls')
    name = input("What's the name of the meal?\n")
    new_meal['name'] = name.lower()

    # Ask user ingredients, one at a time: ingredient, then amount, then ask if any more
    os.system('cls')
    ingredients = dict()
    i = input("What's the first ingredient?\n").lower()
    j = input("How much to use?\n").lower()
    ingredients[i] = j

    while True:
        more = input("Any more ingredients to add? (y/n) \n").lower()
        if more == 'y':
            os.system('cls')
            i = input("What's the next ingredient?\n").lower()
            j = input("How much to use?\n").lower()
            ingredients[i] = j
            continue
        elif more == 'n':
            break
    new_meal['ingredients'] = ingredients

    # Ask for instructions - first, second third step, etc. (number them)
    os.system('cls')
    step = input("What's the first step to make this meal?\n").lower()
    instructions = dict()
    instructions[1] = step
    i = 2

    while True:
        more = input("Any more steps? (y/n) \n").lower()
        if more == 'y':
            os.system('cls')
            step = input("What's the next step?\n").lower()
            instructions[i] = step
            i += 1
            continue
        elif more == 'n':
            break
    new_meal['instructions'] = instructions

    # Get the type of cuisine
    cuisine = input('''What type of cuisine is this meal?
Separate multiple types with a comma.\n''').lower()

    result = [x.strip() for x in cuisine.split(',')]
    new_meal['cuisine'] = result

    # Get the tags
    tags = input('''What tags should be added to this meal?
Separate multiple types with a comma.\n''').lower()

    tags = [x.strip() for x in tags.split(',')]
    new_meal['tags'] = tags

    # Append the new dict (new_meal) to meals (list of meals)
    meals.append(new_meal)

    # Print the new list of meals to file
    import pickle

    f = open('meals.pkl', 'wb')
    pickle.dump(meals, f)
    f.close()

    main_menu()

# Option 3 - View Saved Meals
def view_meals():
    '''This is the function that will run when someone selects option
    3 from the menu

    Just prints a list of available meals'''
    import os
    os.system('cls')

    print('Option 3 - View Meals\n')

    # Load the saved meals from file
    import pickle
    f = open('meals.pkl', 'rb')

    meals = pickle.load(f)

    print("Here are the meals you have saved:\n")

    for i, meal in enumerate(meals):
        print('{}: {}'.format(i + 1, meal['name']))

    print('--------')
    choice = int(input("Enter the number to view details of a meal\n-1 to delete a meal\n0 to return to menu: "))

    if choice == 0:
        main_menu()
    elif choice == -1:
        del_meal()
    else:
        os.system('cls')
        meal_details(choice)

def del_meal():
    '''Pulls up a numbered list of meals and then allows you to delete based on number.'''

    # Load the saved meals from file
    import pickle
    f = open('meals.pkl', 'rb')

    meals = pickle.load(f)
    os.system('cls')

    print("Delete a meal? Which would you like to delete:\n")

    for i, meal in enumerate(meals):
        print('{}: {}'.format(i + 1, meal['name']))

    print('--------')
    meal_num = int(input("Enter the number of the meal you would like to delete (press 0 to exit): "))

    if meal_num == 0:
        main_menu()

    confirm = input("Delete meal number {}? This cannot be undone, are you sure? (y/n)".format(meal_num)).lower()

    if confirm == 'y':
        # Delete the element based on meal number
        del meals[meal_num - 1]

        # Save the new meals list to file
        f = open('meals.pkl', 'wb')
        pickle.dump(meals, f)
        f.close()

    else:
        main_menu()

    main_menu()

def meal_details(num):
    '''This function takes in the number of a meal (from the menus), and returns the details of the meal in a 
    nice, readable format. Ingredients first followed by instructions.'''
    # Load meals
    import pickle
    f = open('meals.pkl', 'rb')
    meals = pickle.load(f)

    # Print name of meal
    print(meals[num - 1]['name'].title())
    print('------------------------------------')

    # Print ingredients, followed by instructions (like in cookbooks)
    for x, y in meals[num - 1]['ingredients'].items():
        print("{} {}".format(y, x))

    # Separator
    print('------------------------------------')

    # Instructions
    for x, y in meals[num - 1]['instructions'].items():
        print('{}: {}'.format(x, y))








      