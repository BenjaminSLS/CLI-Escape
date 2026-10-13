# Import the dialog_options.py, locations.py, and keys.py files as modules.
import gameplay_elements.locations
import gameplay_elements.dialog_options
import gameplay_elements.keys

# Import the os and sys modules.
import os
import sys

# A clear terminal helper.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Process user inputs.
def user_prompt(response):
    answer = input(response).strip().lower()

    # Check if the input is 'exit'.
    if answer == "exit":
        sys.exit()

    # Return the answer.
    return answer

# CLI-Escape Main()
def main(locations, dialog_options, keys):
    # Simplify the references to the locations module.
    rooms = locations.location_text()
    room_images = locations.location_images()
    
    # Simplify the reference to dialog options module.
    dialog = dialog_options.available_dialog()
    played_dialog = dialog_options.played_dialog()

    # Simplify the reference to the keys module.
    key_locations = keys.keys()
    locked_doors = keys.locked_doors()

    # The players current collection of items.
    inventory = []

    # The users current, and starting, location.
    current_location = "bedroom"

    # The game itself running under a while loop.
    while True:
        clear_screen()

        # Collect all of the available locations.
        location_choices = list(rooms[current_location])

        # Show player the unplayed dialog.
        if current_location in dialog and current_location not in played_dialog:
            location_dialog = list(dialog[current_location])

            # Play all the dialog in a location.
            for talk in location_dialog:
                # Check if the user wants to exit.
                user_prompt(f"{talk}\n\nContinue?: ")

                clear_screen()

            # Append played dialog.
            played_dialog.append(current_location)

        # Exits the game if the player has reached a certain location.
        if current_location in ("front door", "firewood"):
            clear_screen()

            # Print a winning message
            print("You escaped!\n")

            user_prompt("\nExit?: ")

        # Show user inventory once they collect the first item.
        if inventory:
            print(f"Inventory: {inventory}\n")

        # Print the location the player is currently in.
        print(f"You are in the {current_location.capitalize()}\n")
        
        # Print all available locations.
        print("All Available Locations")

        for door_num, room in enumerate(location_choices, start=1):
            print(f"{door_num}. {room.capitalize()}")
        print()
        
        # Display the location image.
        for i in room_images[current_location]:
            print(i)
        
        # Ask the user which location they want to move to.
        choice = user_prompt("\nChoose your next location: ")
        
        # Try converting the answer to an integer if possible and pass if not.
        try:
            choice_number = int(choice)

            if 1 <= choice_number <= len(location_choices):
                choice = location_choices[choice_number - 1]

        except ValueError:
            pass
        
        # Detect if a location is available to move to.
        if choice in location_choices:
            clear_screen()

            # Check if door is locked or if a key can be obtained.
            if choice in locked_doors and locked_doors[choice] not in inventory:
                user_prompt(f"{choice.capitalize()} is locked.\n\nContinue?: ")

            else:
                # Check if the user is in a location with an unobtained key.
                if choice in key_locations and key_locations[choice] not in inventory:
                    new_key = key_locations[choice]

                    inventory.append(new_key)

                    user_prompt(f"You found the {new_key.capitalize()} key!\n\nContinue?: ")

                # Set the current_location to the new location if it is available.
                current_location = choice
        else:
            clear_screen()
            
            # Print that a location is not available.
            user_prompt(f"{choice.capitalize()} is not an available location.\n\nContinue?: ")

# Check if the main() function exists and if the user has exited the program.
if __name__ == "__main__":
    try:
        # Invoke the main() function.
        main(gameplay_elements.locations, gameplay_elements.dialog_options, gameplay_elements.keys)

    except SystemExit:
        clear_screen()

        # Print the ending statement.
        print("Thank you for playing my command line interface escape game!")

    except KeyboardInterrupt:
        clear_screen()

        # Print the ending statement if ctrl+c is used.
        print("Thank you for playing my command line interface escape game!")

    except Exception:
        clear_screen()

        # Print an error message.
        print("The game may have crashed.  If the crash is directly related to my own code feel free to contact me.")
        raise
